import cv2
from ultralytics import YOLO

def main():
    model = YOLO("weights/best.pt")
    capture = cv2.VideoCapture("video.mp4")
    output = "result/count/trafic_counting.avi"
    out = cv2.VideoWriter(output, cv2.VideoWriter_fourcc(*"XVID"), capture.get(cv2.CAP_PROP_FPS), 
                          (int(capture.get(cv2.CAP_PROP_FRAME_WIDTH)), int(capture.get(cv2.CAP_PROP_FRAME_HEIGHT))))


    history = {}
    counted = set()
    count = 0
    crossline = int(capture.get(cv2.CAP_PROP_FRAME_WIDTH)//2)

    while True:
        ret, frame = capture.read()
        if not ret:
            break
        results = model.track(frame, persist=True, tracker="bytetrack.yaml", conf=0.3, verbose=False)
        frame_plot = results[0].plot()
        cv2.line(frame_plot, (crossline, 0), 
                              (crossline, int(capture.get(cv2.CAP_PROP_FRAME_HEIGHT))), (0, 255, 255), 3)
        boxes = results[0].boxes
        
        if boxes.id is not None:
            for xyxy, boxid in zip(boxes.xyxy.cpu().numpy(), boxes.id.cpu().numpy()):
                x1, y1, x2, y2 = xyxy
                center = int((x1 + x2)/2)
                if boxid in history:
                    previous = history[boxid]
                    if (
                        previous < crossline and center >= crossline
                    ) or (
                        previous > crossline and center <= crossline
                    ):
                        if boxid not in counted:
                            counted.add(boxid)
                            count += 1
                history[boxid] = center

        cv2.putText(frame_plot, f"计数: {count}", (50, 80), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 4)
        out.write(frame_plot)

    capture.release()
    out.release()
    print(f"越线计数: {count}")


if __name__ == "__main__":
    main()
