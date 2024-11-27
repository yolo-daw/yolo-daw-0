import os
from code.yolo_detection import run_yolo
from code.defogging_methods import apply_defogging

DATA_DIR = "data/test/images"
RESULTS_DIR = "results"
MODEL_PATH = "yolov8s.pt"

def main():
    # Step 1: Run YOLO on original images
    original_results_dir = os.path.join(RESULTS_DIR, "original")
    run_yolo(MODEL_PATH, DATA_DIR, original_results_dir)

    # Step 2: Apply defogging and YOLO on processed images
    for method in ["clahe", "dark_channel"]:
        processed_dir = os.path.join(RESULTS_DIR, f"defogged_{method}")
        os.makedirs(processed_dir, exist_ok=True)
        for img_file in os.listdir(DATA_DIR):
            img_path = os.path.join(DATA_DIR, img_file)
            apply_defogging(img_path, processed_dir, method)

        run_yolo(MODEL_PATH, processed_dir, os.path.join(RESULTS_DIR, f"detection_{method}"))

    # Step 3: Analyze results
    # Placeholder: Compare metrics and save results in comparisons/
    print("Pipeline execution completed. Results are stored in the results/ directory.")

if __name__ == "__main__":
    main()
