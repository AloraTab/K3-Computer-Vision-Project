from ultralytics import YOLO
import cv2
import torch
import ultralytics.data.build as build
from model.class import YOLOWeightedDataset

# Monkey patch method for the weighted dataloader
build.YOLODataset = YOLOWeightedDataset

# Load the YOLO model
model = YOLO("yolo11n.yaml") 
model = model.load("yolo11n.pt") 

# Train the model
def train_model():
    results = model.train(data="/dataset/data.yaml",
                          epochs=200,
                          imgsz=640,
                          resume=False,
                          patience=20,
                          name='Colab-120-weighted')
    return results

if __name__ == "__main__":
    train_model()