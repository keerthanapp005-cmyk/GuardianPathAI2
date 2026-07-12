import cv2
import pyttsx3
import time
from ultralytics import YOLO


engine = pyttsx3.init()
engine.setProperty("rate", 170)

print("Loading YOLO model...")
model = YOLO("yolov8n.pt")
print("Model loaded successfully!")


cap = cv2.VideoCapture("http://10.108.213.157:8080/videofeed")

if not cap.isOpened():
    print("Error: Could not open camera stream.")
    exit()

print("Press 'q' to quit.")

last_spoken = ""
last_time = 0

while True:

    success, frame = cap.read()

    if not success:
        print("Failed to read frame.")
        break

    
    results = model(frame, verbose=False)

    
    for result in results:
        for box in result.boxes:

            class_id = int(box.cls[0])
            object_name = model.names[class_id]

            current_time = time.time()

            if object_name != last_spoken or current_time - last_time > 3:
                print("Detected:", object_name)

                engine.say(object_name)
                engine.runAndWait()

                last_spoken = object_name
                last_time = current_time

                
                break
        else:
            continue
        break

    
    annotated_frame = results[0].plot()

    cv2.imshow("GuardianPath AI", annotated_frame)

    
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()