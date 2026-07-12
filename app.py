import cv2

from camera import get_camera
from detector import detect_objects
from scene import analyze_scene
from decision import decide_path
from voice import speak

cap = get_camera()



print("GuardianPath AI Started")

while True:

    success, frame = cap.read()

    if not success:
        break

    detections = detect_objects(frame)

    frame_width = frame.shape[1]

    
    scene = analyze_scene(detections, frame_width)

   
    instruction = decide_path(scene)
   
    speak(instruction)
      
    
    for obj in detections:

        x1, y1, x2, y2 = obj["box"]

        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

        cv2.putText(
            frame,
            obj["name"],
            (x1, y1 - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.6,
            (0, 255, 0),
            2
        )

    cv2.imshow("GuardianPath AI", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()