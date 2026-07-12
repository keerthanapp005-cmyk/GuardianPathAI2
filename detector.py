from ultralytics import YOLO


model = YOLO("yolov8n.pt")

IMPORTANT_OBJECTS = [
    "person",
    "chair",
    "bench",
    "door",
    "bottle",
    "stairs"
]

def detect_objects(frame):

    detections = []

    results = model(frame, verbose=False)

    for result in results:
        for box in result.boxes:

            class_id = int(box.cls[0])

            name = model.names[class_id]

            confidence = float(box.conf[0])

            if name not in IMPORTANT_OBJECTS:
                continue

            x1, y1, x2, y2 = box.xyxy[0]

            detections.append({
                "name": name,
                "confidence": confidence,
                "box": [int(x1), int(y1), int(x2), int(y2)]
            })

    return detections