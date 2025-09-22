# src/trajectory.py
from sgp4.api import Satrec
from datetime import datetime, timedelta
import numpy as np

def propagate_tle(tle_line1, tle_line2, minutes_ahead=60, step_s=60):
    """
    Propagate satellite orbit from TLE for a given duration.
    Returns (times, positions) where:
      - times is a list of datetime objects
      - positions is a numpy array of [x,y,z] ECI coordinates
    """
    sat = Satrec.twoline2rv(tle_line1, tle_line2)
    start = datetime.utcnow()

    times = []
    positions = []

    for m in range(minutes_ahead):
        t = start + timedelta(minutes=m)
        # Convert datetime to Julian date + fraction
        jd = 367*t.year - (7*(t.year + (t.month+9)//12))//4 + (275*t.month)//9 + t.day + 1721013.5
        fr = (t.hour + t.minute/60 + t.second/3600)/24.0
        e, r, v = sat.sgp4(jd, fr)
        if e == 0:  # valid propagation
            times.append(t)
            positions.append(r)

    return times, np.array(positions)

if __name__ == "__main__":
    tle0 = "1 25544U 98067A   25330.54705324  .00001264  00000-0  33372-4 0  9993"
    tle1 = "2 25544  51.6432 130.2380 0007499  54.0897  13.1610 15.50000091234567"
    t, pos = propagate_tle(tle0, tle1, minutes_ahead=5, step_s=60)
    print("Generated", len(pos), "points. First position:", pos[0])
