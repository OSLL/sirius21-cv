import cv2 as cv
import numpy as np

def openImg(filepath):
    return cv.imread(filepath, 1)


def getMask(lowerRange, upperRange, img):
    return cv.inRange(img, lowerRange, upperRange)

#def maskImg(mask, img):
#    return cv.

def main():
    img=openImg(input())
    cv.imwrite("output.jpg",getMask(np.array([50, 20, 20]),np.array([255, 255, 255]),img))


if __name__ == "__main__":
    main()
