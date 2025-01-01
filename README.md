# K3-Computer-Vision-Project

Uses the dataset from Roboflow with Yolov11.

## Problems with the dataset

One primary issue of the dataset is the imbalance. Mask and vest classes are under represented in the dataset. 

I attempted to mitigate the impact with data augmentation through albumentations and simpler techniques like oversampling the smaller class.

However, what worked best was using the Weighted Dataloader provided by [Yasin's solution](https://y-t-g.github.io/tutorials/yolo-class-balancing/)