def load_tles(file_path, limit=5):
    with open(file_path, "r") as f:
        lines = [l.strip() for l in f.readlines() if l.strip()]
    objects = {}
    for i in range(0, min(len(lines), limit*3), 3):
        name = lines[i]
        line1, line2 = lines[i+1], lines[i+2]
        objects[name] = (line1, line2)
    return objects
