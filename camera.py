import cv2

CAMERA_URL = "http://10.108.213.157:8080/videofeed"


def get_camera():
    cap = cv2.VideoCapture(CAMERA_URL)

    if not cap.isOpened():
        raise Exception("Could not connect to phone camera.")

    return cap