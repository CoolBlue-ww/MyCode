import torch
import load_test
from yolov5 import train
config = {
    'imgsz': 320,  # 输入图像大小
    'batch_size': 1,  # 批处理大小
    'epochs': 300,  # 训练轮数
    'data': '/home/SayMyName/桌面/STUDY/deep_learning/YoLov5n/yolov5n_dataset/yolov5n_dataset.yaml',  # 数据集路径
    'cfg': '/home/SayMyName/桌面/STUDY/deep_learning/YoLov5n/yolov5n_dataset/yolov5n_dataset.yaml',  # 模型配置文件路径
    'weights': 'yolov5n.pt',  # 预训练权重路径
    'name': 'yolov5s',  # 项目名称
    'optimizer': 'adam',  # 优化器
    'lr': 0.001,  # 学习率
    'final_lr': 0.0001,  # 最终学习率
    'freeze': 0,  # 冻结层数
    'workers': 8,  # 工作线程数
    'project': 'runs/train',  # 项目路径
    'entity': None,  # 实体
    'cache_images': False,  # 缓存图像数据
    'conf_thres': 0.001,  # 置信度阈值
    'iou_thres': 0.6,  # 交并比阈值
    'classes': 80,  # 类别数
    'agnostic_nms': False,  # 非通用NMS
    'augment': False,  # 图像增强
    'half': False,  # 半精度运算
    'device': 'cpu',  # 设备
    # 'device': 'cpu'  # 设备
    'patience': 10,  # 早停轮数
    'checkpoint': None,  # 断点路径
    'noval': False,  # 不验证
    'noautoanchor': False,  # 不自动生成anchors 
    'exist_ok': False,  # 存在则跳过
    'rect': False,  # 矩形框
    'nosave': False,  # 不保存模型
    'notest': False,  # 不测试
    'export': False,  # 导出ONNX模型
    'weights_only': False,  # 只导出权重
}


if __name__ == '__main__':
    print("开始YoLov5训练...")

    print(f"开始使用设备： {config['device']}")

    train.run(
        weights=config['weights'],
        data=config['data'],
        epochs=config['epochs'],
        imgsz=config['imgsz'],
        batch_size=config['batch_size'],
        device=config['device']
    )