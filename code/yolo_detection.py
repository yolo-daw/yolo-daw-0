from ultralytics import YOLO
import os

def run_yolo(model_path, image_dir, output_dir):
    model = YOLO(model_path)
    results = model.predict(source=image_dir, save=True, save_txt=True, project=output_dir)
    return results
