from ultralytics import YOLO

def main():
    model = YOLO("yolov8n.pt")

    model.train(data="data_1.yaml", epochs=50, imgsz=640, batch=16, device=0,
        workers=8, project="result/train", name="yolov8n_model", exist_ok=True,
        pretrained=True, optimizer="AdamW", lr0=0.001, amp=False, save=True, save_period=10,
        val=True, verbose=True, cache=True, plots=True)

if __name__ == "__main__":
    main()
