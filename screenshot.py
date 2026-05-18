import cv2
import os

path = "result/track/vehicle_tracking/video.avi"
output = "screenshot"

os.makedirs(output, exist_ok=True)
capture = cv2.VideoCapture(path)

frames = [300, 310, 320, 330]
frame_id = 0

while True:
    ret, frame = capture.read()
    if not ret:
        break
    if frame_id in frames:
        cv2.imwrite(os.path.join(output, f"frame_{frame_id}.jpg"), frame)
    frame_id += 1

capture.release()
