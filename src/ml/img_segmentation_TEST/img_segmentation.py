import cv2
import matplotlib.pyplot as plt
import numpy as np

flags = [i for i in dir(cv2) if i.startswith('COLOR_')]

def mask_img(imgpath):
    imgBGR = cv2.imread(imgpath)
    plt.imshow(imgBGR)
    plt.show()

    imgRGB = cv2.cvtColor(imgBGR, cv2.COLOR_BGR2RGB)
    plt.imshow(imgRGB)
    plt.show()

    imgHSV = cv2.cvtColor(imgRGB, cv2.COLOR_RGB2HSV)

    imgHSV2 = cv2.cvtColor(imgBGR, cv2.COLOR_BGR2HSV)

    plt.imshow(imgHSV)
    plt.imshow(imgHSV2)

    light_brown = (202, 221, 234)
    dark_brown = (51, 64, 92)

    # light_white = (238, 246, 249)
    # dark_white = (210, 223, 226)

    light_white = (0, 0, 200)
    dark_white = (145, 60, 255)

    mask = cv2.inRange(imgHSV, light_white, dark_white)

    result = cv2.bitwise_and(imgRGB, imgRGB, mask = mask)

    plt.subplot(1, 2, 1)
    plt.imshow(mask, cmap = 'gray')
    plt.subplot(1, 2, 2)
    plt.imshow(result)
    plt.show()


def main():
    imgpath = 'src\ml\img2.jpg'
    mask_img(imgpath)

