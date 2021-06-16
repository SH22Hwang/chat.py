from threading import *
from socket import *

import cv2
import numpy as np
from PIL import ImageGrab
from PyQt5.QtCore import Qt, pyqtSignal, QObject


class ScreenCrop:
    def __init__(self):
        img = ImageGrab.grab()
        img_np = np.array(img)  # this is the array obtained from conversion
        self.img = cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB)

        cv2.namedWindow('image')
        cv2.setMouseCallback('image', self.draw_rectangle)

        self.click = False
        self.x1, self.y1 = -1, -1
        self.x2, self.y2 = -1, -1

        while True:
            cv2.imshow('image', self.img)
            k = cv2.waitKey(1) & 0xFF
            if k == 27:
                break
        cv2.destroyAllWindows()

    def draw_rectangle(self, event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN:  # 마우스를 누른 상태
            self.click = True
            self.x1, self.y1 = x, y
            print("왼쪽 위: (" + str(self.x1) + ", " + str(self.y1) + ")")

        elif event == cv2.EVENT_LBUTTONUP:
            self.click = False  # 마우스를 때면 상태 변경
            self.x2, self.y2 = x, y
            print("오른쪽 아래: (" + str(self.x2) + ", " + str(self.y2) + ")")
            cv2.rectangle(self.img, (self.x1, self.y1), (self.x2, self.y2), (0, 255, 0), 5)


if __name__ == "__main__":
    s = ScreenCrop()
    s
