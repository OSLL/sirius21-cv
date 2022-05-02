import cv2 as cv
import numpy as np
import os.path

filenames = ['img/1red_small.jpg', 'img/3red_small.jpg', 'img/5red_small.jpg', 'img/nored_small.jpg', 'img/size_balls_small.jpg', 'img/1red.jpg', 'img/3red.jpg', 'img/5red.jpg', 'img/nored.jpg', 'img/size_balls.jpg']
color_limits = [(0, 12), (80, 100)]

def main():
    path_dir = '../images/'
    inum = int(input('Type image number: '))
    path_file = path_dir + 'pic' + str(inum) + '.jpg'
    #name, ext = os.path.splitext(path_file)

    img = cv.imread(path_file, 3)
    hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)

    colornum = int(input('Type color number (0- красный, 1- оранжевый, 2- желтый, 3- зеленый, 4- голубой, 5- синий, 6- фиолетовый, 7- темно-красный): '))
    color_limits = [[0, 10], [11, 20], [35, 50], [50, 80], [85, 100], [105, 120], [120, 160], [180, 255]]

    mask = cv.inRange(hsv, (color_limits[colornum][0], 50, 50), (color_limits[colornum][1], 255, 255))
    cv.imshow('Mask', mask)

    kernel = np.ones((10, 10), 'uint8')
    mask = cv.dilate(mask, kernel, iterations=1)
    cv.imshow('dilated', mask)

    mask = cv.erode(mask, kernel, iterations=2)
    cv.imshow('eroded', mask)

    mask = cv.dilate(mask, kernel, iterations=1)
    cv.imshow('dilated2', mask)

    #contours, hierarchy = np.array(cv.findContours(mask, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE))
    contours, hierarchy = cv.findContours(mask, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

    cv.drawContours(img, contours, -1, (0, 0, 255), 2)

    balls_number = 0

    for line in contours:
        x, y, w, h = cv.boundingRect(line)
        cv.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 1)
        balls_number += 1

    print(balls_number)
    print(len(contours))



    cv.imshow('Img', img)

    cv.waitKey(0)

if __name__ == "__main__":
    main()
