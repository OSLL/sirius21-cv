import cv2 as cv
import numpy as np
from math import *

file_names = ['img/1red.jpg', 'img/1red_small.jpg','img/3red.jpg', 'img/3red_small.jpg', 'img/5red.jpg', 'img/5red_small.jpg', 'img/nored.jpg', 'img/nored_small.jpg', 'img/size_balls.jpg', 'img/size_balls_small.jpg']
color_limits = [(0, 12), (13, 17), (18, 23), (25, 40), (50, 70), (85, 100), (101, 109), (110, 135), (136, 150)]

def main():

    image_number = int(input('Type image number: '))
    color_number = int(input('Type color number: '))

    img = cv.imread(file_names[image_number], 3)
    hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)

    mask = cv.inRange(hsv, (color_limits[color_number][0], 50, 50), (color_limits[color_number][1], 255, 255))

    kernel = np.ones((7, 7), 'uint8')
    mask = cv.dilate(mask, kernel, iterations = 2)
    mask = cv.erode(mask, kernel, iterations = 4)
    mask = cv.dilate(mask, kernel, iterations = 2)

    contours, hierarchy = cv.findContours(mask, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    cv.drawContours(img, contours, -1, (0, 255, 0), 2)

    balls_coordinates = []
    balls_sizes = []

    for line in contours:
        x, y, w, h = cv.boundingRect(line)
        cv.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 1)
        balls_coordinates.append((x + w/2, y + h/2))
        balls_sizes.append(round(pi * w/2 * h/2, 1))

    balls_number = len(contours)

    print('Quantity of balls:', balls_number)
    print('Coordinates of balls: ', balls_coordinates)
    print('Sizes of balls: ', balls_sizes)

    if balls_number > 2:

        r_min = sqrt(img.shape[0] ** 2 + img.shape[1] ** 2)
        r_max = 0

        for i in range(balls_number):
            x1, y1 = balls_coordinates[i][0], balls_coordinates[i][1]
            for j in range(i+1, balls_number):
                x2, y2 = balls_coordinates[j][0], balls_coordinates[j][1]
                r = round(sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2), 1)
                if r < r_min:
                    r_min = r
                    x_min_1, y_min_1 = int(x1), int(y1)
                    x_min_2, y_min_2 = int(x2), int(y2)
                if r > r_max:
                    r_max = r
                    x_max_1, y_max_1 = int(x1), int(y1)
                    x_max_2, y_max_2 = int(x2), int(y2)

        cv.line(img, (x_min_1, y_min_1), (x_min_2, y_min_2), [255, 0, 0], 2)
        cv.line(img, (x_max_1, y_max_1), (x_max_2, y_max_2), [255, 0, 0], 2)

        print('Minimal distance: ', r_min)
        print('Maximal distance: ', r_max)

    cv.imshow('Img', img)
    cv.waitKey(0)

if __name__ == "__main__":
    main()