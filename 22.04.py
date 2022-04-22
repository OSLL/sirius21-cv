import cv2 as cv
import numpy as np


def find_line(image, lower, upper):
    hsv = cv.cvtColor(image, cv.COLOR_RGB2HSV)
    mask = cv.inRange(hsv, lower, upper)

    edges = cv.Canny(mask, 50, 100)
    line = cv.HoughLines(edges, 1, np.pi / 180, 70)

    return line


def draw_lines(img, lines):
    for line in lines:
        rho = line[0][0]
        theta = line[0][1]
        x_min, y_min = 0, 0
        (y_max, x_max, z) = img.shape

        if theta == 0:
            x_min = int(rho)
            x_max = int(rho)
        else:
            y_min = int(-np.cos(theta) / np.sin(theta) * x_min + rho / np.sin(theta))
            y_max = int(-np.cos(theta) / np.sin(theta) * x_max + rho / np.sin(theta))

        cv.line(img, (x_min, y_min), (x_max, y_max), (255, 0, 0), 1)


img = cv.imread('img/road.jpg', 1)

white_lower = np.array([0, 0, 150])
white_upper = np.array([255, 10, 255])

yellow_lower = np.array([50, 50, 50])
yellow_upper = np.array([200, 200, 200])

lines_white = find_line(img, white_lower, white_upper)
lines_yellow = find_line(img, yellow_lower, yellow_upper)

draw_lines(img, lines_white)
draw_lines(img, lines_yellow)

cv.imshow('img', img)
cv.waitKey(0)
cv.destroyAllWindows()
