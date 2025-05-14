import os
import numpy as np
import cv2

# Dataset path
DATASET_PATH = "dataset_dfdc"
IMAGE_SIZE = (128, 128)

def load_and_process_images(folder_path, label):
    data = []
    labels = []
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        image = cv2.imread(file_path)
        if image is not None:
            image = cv2.resize(image, IMAGE_SIZE)
            image = image / 255.0
            data.append(image)
            labels.append(label)
    return np.array(data), np.array(labels)

def create_dataset():
    real_path = os.path.join(DATASET_PATH, "real")
    fake_path = os.path.join(DATASET_PATH, "fake")

    real_data, real_labels = load_and_process_images(real_path, 1)
    fake_data, fake_labels = load_and_process_images(fake_path, 0)

    data = np.concatenate([real_data, fake_data])
    labels = np.concatenate([real_labels, fake_labels])

    return data, labels

if __name__ == "__main__":
    data, labels = create_dataset()
    print(f"Data shape: {data.shape}")
    print(f"Labels shape: {labels.shape}")
