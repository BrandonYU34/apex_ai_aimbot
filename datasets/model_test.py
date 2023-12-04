import ultralytics
from ultralytics import YOLO
import multiprocessing

if __name__ == '__main__':
    model = YOLO('apex_yolo_v8n/exp640_/weights/best.pt')

    result = model.predict(
        source='test/images',
        conf=0.45,
        save=True,
        save_txt=True,
        save_conf=False,
        save_crop=True,
        visualize=False
    )
