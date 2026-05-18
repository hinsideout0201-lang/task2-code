import cv2
from ultralytics import YOLO

def main():
    model = YOLO("weights/best.pt")
    results = model.track(source="video.mp4", tracker="bytetrack.yaml", save=True, persist=True,
        show=False, conf=0.3, project="result/track", name="vehicle_tracking",
        exist_ok=True, stream=False)

if __name__ == "__main__":
    main()
