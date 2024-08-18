from ultralytics import YOLO

# Load a pretrained YOLOv8 model (e.g., YOLOv8n)
model = YOLO("yolov8n.pt")

# Train the model
model.train(data="potholes.yaml", epochs=50, imgsz=378)

results = model.predict(source='/path_to_your_test_images', save=True)

metrics = model.val()
