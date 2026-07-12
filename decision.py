DANGER_OBJECTS = [
    "person",
    "chair",
    "bench",
    "bicycle",
    "motorcycle",
    "car",
    "bus",
    "truck"
]


def decide_path(scene):

   
    blocked = False

    for obj in scene["ahead"]:
        if obj in DANGER_OBJECTS:
            blocked = True
            break

   
    if not blocked:
        return "Continue forward."

   
    if len(scene["left"]) == 0:
        return "Obstacle ahead. Move left."

    
    if len(scene["right"]) == 0:
        return "Obstacle ahead. Move right."

    
    return "Stop. No safe path ahead."