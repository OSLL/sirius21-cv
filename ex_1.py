import cv2 as cv
import numpy as np

def test(way):
    img = cv.imread('%s' % way)
    if img is None:
        print('File does not exist')
        exit()

def open(way):
    img = cv.imread('%s' % way)
    return img

way, save = input().split()
test(way)
img = open(way)
lower_range = np.array([50,50,50])
upper_range = np.array([200,200,200])
mask = cv.inRange(img, lower_range, upper_range)
cv.imwrite('%s' % save, mask)