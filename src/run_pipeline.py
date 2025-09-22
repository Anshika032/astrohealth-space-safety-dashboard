"""
Master pipeline script for Space Dashboard
- Propagates satellite & debris orbits
- Detects conjunctions
- Publishes alerts to local Mosquitto (space/alerts/collision)
"""

import os, time, json
import pandas as pd
import numpy as np
import paho.mqtt.client as mqtt

from trajectory import propagate_tle
from debris_classify import train_classifier
from collision import check_collision
from utils import load_tles


def publish_alert(alert_msg: dict):
    """Publish alert to local Mosquitto broker at localhost:1883."""
    try:
        client = mqtt.Client()
        client.connect("localhost", 1883, 60)  # Local broker
        client.publish("space/alerts/collision", json.dumps(alert_msg))
        print("[MQTT] Published alert:", alert_msg)
        client.disconnect()
    except Exception as e:
        print("[ERROR] Could not publish MQTT alert:", e)


def run_bulk_pipeline():
    """Propagate multiple satellites & debris, detect conjunctions."""
    sats = load_tles("data/tle/active.tle", limit=3)   # take 3 active sats
    debris = load_tles("data/tle/debris.tle", limit=3) # take 3 debris objects

    alerts = []
    for sat_name, (sat1, sat2) in sats.items():
        _, traj1 = propagate_tle(sat1, sat2, minutes_ahead=30)

        for deb_name, (d1, d2) in debris.items():
            _, traj2 = propagate_tle(d1, d2, minutes_ahead=30)

            hit, dmin = check_collision(traj1, traj2, threshold_km=10.0)
            if hit:
                alert = {
                    "alert": "Conjunction detected",
                    "object": f"{sat_name} vs {deb_name}",
                    "min_distance_km": float(dmin),
                    "time": time.strftime("%Y-%m-%d %H:%M:%S")
                }
                alerts.append(alert)
    return alerts


def main():
    print("\n=== SPACE DASHBOARD PIPELINE ===")

    # Step 1: Train debris classifier (demo, optional)
    model = train_classifier("data/debris_dataset.csv")
    sample_df = pd.DataFrame([{
        "a": 6870, "e": 0.002, "i": 98.7,
        "raan": 20.1, "argp": 120.3, "mean_motion": 14.9
    }])
    pred = model.predict(sample_df)[0]
    print(f"[INFO] Sample classified as: {'Active Satellite' if pred==1 else 'Debris'}")

    # Step 2: Run propagation + collision detection
    alerts = run_bulk_pipeline()

    # Step 3: Publish alerts
    if alerts:
        for alert in alerts:
            print(f"[ALERT] {alert['object']} at {alert['min_distance_km']:.2f} km")
            publish_alert(alert)
    else:
        print("[OK] No close approaches detected.")

    print("\n=== PIPELINE COMPLETE ===")


if __name__ == "__main__":
    main()
