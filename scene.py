def analyze_scene(detections, frame_width):

    scene = {
        "left": [],
        "ahead": [],
        "right": []
    }

    for obj in detections:

        x1, y1, x2, y2 = obj["box"]

        center_x = (x1 + x2) / 2

        if center_x < frame_width / 3:
            scene["left"].append(obj["name"])

        elif center_x < 2 * frame_width / 3:
            scene["ahead"].append(obj["name"])

        else:
            scene["right"].append(obj["name"])

    return scene