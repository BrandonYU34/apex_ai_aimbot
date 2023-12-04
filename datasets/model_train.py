import ultralytics
from ultralytics import YOLO
import multiprocessing

if __name__ == '__main__':
    multiprocessing.freeze_support()
    model = YOLO('models/yolov8n.pt')

    result = model.train(
        data='data.yaml',
        imgsz=640,
        epochs=100,
        batch=16,
        project='apex_yolo_v8n',
        name='exp640_'
    )
