 
import numpy as np

def check_collision(traj1, traj2, threshold_km=10.0):
    """
    Check if two trajectories come closer than threshold_km.
    traj1, traj2: numpy arrays of positions [x,y,z] in km
    """
    min_dist = float("inf")
    for p1, p2 in zip(traj1, traj2):
        dist = np.linalg.norm(np.array(p1) - np.array(p2))
        if dist < min_dist:
            min_dist = dist
        if dist < threshold_km:
            return True, dist
    return False, None if min_dist == float("inf") else min_dist
