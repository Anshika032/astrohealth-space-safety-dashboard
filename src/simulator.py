# src/simulator.py
import paho.mqtt.client as mqtt
import json, time, random

def simulate_astronaut():
    client = mqtt.Client()
    client.connect("broker.hivemq.com", 1883, 60)
    while True:
        payload = {
            "astronaut": "Alice",
            "heart_rate": random.randint(60, 100),
            "oxygen_level": random.uniform(92, 99),
        }
        client.publish("space/astronauts/vitals", json.dumps(payload))
        print("Published:", payload)
        time.sleep(2)

if __name__ == "__main__":
    simulate_astronaut()
 
