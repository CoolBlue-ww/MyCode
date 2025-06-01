import torch
import sys

sys.path.append('/home/SayMyName/桌面/STUDY/deep_learning/YoLov5n/yolov5')
model = torch.hub.load('/home/SayMyName/桌面/STUDY/deep_learning/YoLov5n/yolov5', 'custom', path='/home/SayMyName/桌面/STUDY/deep_learning/YoLov5n/yolov5n.pt', source='local')

model.eval()

results = model('/home/SayMyName/桌面/STUDY/deep_learning/YoLov5n/yolov5n_dataset/images/train/bffabaa0-dog_9.jpg')
results.show()
results.print()