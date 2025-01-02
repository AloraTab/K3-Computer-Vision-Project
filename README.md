# K3-Computer-Vision-Project

Uses the dataset from Roboflow with Yolov11.

## How to Run

1. Use docker to containerize the image (Image is published on DockerHub as a10ra/obj-det-image or on this link https://hub.docker.com/repository/docker/a10ra/obj-det-image/general)
2. Run the container on the port like: docker run -d --name obj-det-container -p 127.0.0.1:5000:5000 obj-det-image

## Problems with the dataset

One primary issue of the dataset is the imbalance. Mask and vest classes are under represented in the dataset. 

I attempted to mitigate the impact with data augmentation through albumentations and simpler techniques like oversampling the smaller class.

However, what worked best was using the Weighted Dataloader provided by [Yasin's solution](https://y-t-g.github.io/tutorials/yolo-class-balancing/)

| Class   | Images | Instances | Box (P) | R     | mAP50 | mAP50-95 |
|---------|--------|-----------|---------|-------|-------|----------|
| all     | 15     | 49        | 0.943   | 0.834 | 0.9   | 0.657    |
| helmet  | 14     | 21        | 1       | 0.988 | 0.995 | 0.741    |
| mask    | 7      | 14        | 1       | 0.657 | 0.897 | 0.61     |
| vest    | 9      | 14        | 0.828   | 0.857 | 0.808 | 0.62     |


## Problems I Faced

I faced issues during the model training, where I struggled to get the mean Average Precision to be over 0.5. Trying out different data augmentation, class balancing methods, was also a learning experience for me on this dataset.

Another problem faced was just general build issues - things would work locally but the container wouldn't start or the requirements.txt was missing some dependencies. Overall, I spent a lot more time looking through the documentation and guides from FastAPI, Docker and YOLO.