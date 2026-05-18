# 任务2：场景目标检测与视频多目标跟踪

本课程实验项目基于YOLOv8实现：
- 道路车辆目标检测
- 多目标跟踪
- 跟踪ID分配
- 越线计数

---

# 数据集

https://www.kaggle.com/datasets/ashfakyeafi/road-vehicle-images-dataset

---

# 环境配置

实验环境：

- Python 3.12
- PyTorch 2.8
- Ultralytics YOLOv8
- OpenCV

安装依赖：

```bash
pip install ultralytics opencv-python
```

---

# 功能说明

## 1. 模型微调训练

运行：

```bash
python train.py
```

---

## 2. 多目标跟踪

运行：

```bash
python track.py
```
输出Tracking视频。

---

## 3. 越线计数

运行：

```bash
python count.py
```

实现车辆越线检测计数。

---

## 4. 遮挡与ID跳变分析

运行：

```bash
python screenshot.py
```

用于抽取若干帧进行分析。

---
- 道路车辆分析

等场景。
