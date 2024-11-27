import cv2
import numpy as np
import os

def clahe_defogging(image):
    lab = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
    l, a, b = cv2.split(lab)
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
    l = clahe.apply(l)
    lab = cv2.merge((l, a, b))
    return cv2.cvtColor(lab, cv2.COLOR_LAB2BGR)

def dark_channel_defogging(image, omega=0.95):
    dark_channel = np.min(image, axis=2)
    dark_channel = np.expand_dims(dark_channel, axis=2)
    dark_channel = np.repeat(dark_channel, 3, axis=2)
    return cv2.addWeighted(image, omega, dark_channel, 1 - omega, 0)
    
def apply_defogging(image_path, output_path, method="clahe"):
    image = cv2.imread(image_path)
    if method == "clahe":
        processed = clahe_defogging(image)
    elif method == "dark_channel":
        processed = dark_channel_defogging(image)
    else:
        raise ValueError("Unknown defogging method!")
    
    os.makedirs(output_path, exist_ok=True)
    output_file = os.path.join(output_path, os.path.basename(image_path))
    cv2.imwrite(output_file, processed)
