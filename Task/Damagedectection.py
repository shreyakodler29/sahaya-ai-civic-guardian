from ultralytics import YOLO

model = YOLO("yolov8n.pt")

def detect_damage(image_path):
    results = model(image_path)
    return results[0].boxes
