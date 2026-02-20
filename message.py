import time
import cv2
import numpy as np
from PIL import ImageGrab


def get_screen_roi(bbox=None):
    """截取屏幕（可选指定区域）并预处理"""
    if bbox is None:
        img = ImageGrab.grab()
    else:
        img = ImageGrab.grab(bbox=bbox)
    # 转为BGR格式（OpenCV默认）+ 灰度图 + 高斯模糊去噪
    img_cv = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
    img_gray = cv2.cvtColor(img_cv, cv2.COLOR_BGR2GRAY)
    img_gray = cv2.GaussianBlur(img_gray, (5, 5), 0)
    return img_gray


def detect_screen_change(initial_img, threshold=30):
    """
    检测界面变化
    :param initial_img: 初始灰度图
    :param threshold: 差异阈值（越小越灵敏）
    :return: 是否变化、差异图（可选）
    """
    new_img = get_screen_roi()
    # 计算差分图
    diff = cv2.absdiff(initial_img, new_img)
    # 二值化：超过阈值的像素设为255（白色）
    _, thresh = cv2.threshold(diff, threshold, 255, cv2.THRESH_BINARY)
    # 计算白色像素占比（变化区域）
    change_ratio = np.sum(thresh) / (255 * thresh.size)
    # 占比超过1%则判定为变化（可根据需求调整）
    return change_ratio > 0.01, thresh


if __name__ == "__main__":
    initial = get_screen_roi()
    print("开始监控界面变化...")
    while True:
        is_changed, diff_img = detect_screen_change(initial)
        if is_changed:
            print("界面发生变化！")
            initial = get_screen_roi()  # 更新快照
        time.sleep(1)