import cv2 as cv
import numpy as np

img = cv.imread('img/lines.jpg', 1)

hsv = cv.cvtColor(img, cv.COLOR_RGB2HSV)

yellow_lower = np.array([50, 50, 50])
yellow_upper = np.array([200, 200, 200])

mask_yellow = cv.inRange(hsv, yellow_lower, yellow_upper)

edges = cv.Canny(mask_yellow, 50, 150)
rho_accuracy = 1
theta_accuracy = np.pi / 180
min_length = 100
lines = cv.HoughLines(edges, rho_accuracy, theta_accuracy, min_length)

for line in lines:
    rho = line[0][0]
    theta = line[0][1]
    x_min, y_min = 0, 0
    (x_max, y_max) = mask_yellow.shape

    if theta == 0:
        x_min = int(rho)
        x_max = int(rho)
    else:
        y_min = int(-np.cos(theta) / np.sin(theta) * x_min + rho/np.sin(theta))
        y_max = int(-np.cos(theta) / np.sin(theta) * x_max + rho/np.sin(theta))

    cv.line(img, (x_min, y_min), (x_max, y_max), (255, 0, 0), 1)

cv.imshow('img', img)
cv.waitKey(0)
cv.destroyAllWindows()
