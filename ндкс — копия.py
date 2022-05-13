import os.path
import cv2 as cv
import numpy as np
import cv2


def main():
    path = "C:\Golosavanie"
    img = cv.imread("C:\Games\image.png", 2356)
    lower_range = np.array([110, 110, 110])
    upper_range = np.array([255, 255, 255])
    mask = cv.inRange(img, lower_range, upper_range)
    cv.imshow("window", mask)
    cv2.imwrite(os.path.join(path, "awd.png"), mask)
    cv.waitKey(0)
    cv.destroyAllWindows()


if __name__ == "__main__":
    main()