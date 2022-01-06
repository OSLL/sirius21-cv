import cv2 as cv
import numpy as np

# 11111
# 11111
# 11111
# 11111
# 11111

filenames = ['img/1red_small.jpg', 'img/5red_small.jpg']
color_limits = [(0, 12), (88, 104), (10, 23), (106, 150), (17, 50), (42, 87 )]

def main():
    inum = int(input('Type image number: '))

    img = cv.imread(filenames[inum], 3)
    hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)


    
    name = str(input('Type color name(red, blue, orange, purple, yellow, green): '))
    if name == "red":
        colornum = 0
    elif name == "blue":
        colornum = 1
    elif name == "orange":
        colornum = 2
    elif name == "purple":
        colornum = 3
    elif name == "yellow":
        colornum = 4
    elif name == "green":
        colornum = 5


    mask = cv.inRange(hsv, (color_limits[colornum][0], 50, 50), (color_limits[colornum][1], 255, 255))
    cv.imshow('Mask', mask)

    kernel = np.ones((5, 5), 'uint8')
    mask = cv.dilate(mask, kernel, iterations=1)
    cv.imshow('dilated', mask)

    mask = cv.erode(mask, kernel, iterations=2)
    cv.imshow('eroded', mask)

    mask = cv.dilate(mask, kernel, iterations=1)
    cv.imshow('dilated2', mask)

    contours, hierarchy = cv.findContours(mask, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    cv.drawContours(img, contours, -1, (0, 255, 0), 2)

    balls_number = 0

    for line in contours:
        x, y, w, h = cv.boundingRect(line)
        cv.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 1)
        balls_number += 1

    print("balls number: ", balls_number)
    print("conturs: ",len(contours))



    cv.imshow('Img', img)

    cv.waitKey(0)

if __name__ == "__main__":
    main()
