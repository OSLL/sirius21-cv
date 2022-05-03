import sys
from os.path import exists
import cv2 as cv

def open_image_in_hsv(path_of_image):
    img = cv.imread(path_of_image)
    img = cv.cvtColor(img,cv.COLOR_BGR2HSV)
    return img

def main():

    if(len(sys.argv)<=1):
        print('incorrect input')
        print('Type -h or --help to get help')
        exit()

    if (sys.argv[1] == '-h' or sys.argv[1] == '--help'):
        print('Use flag -p or --path to specify path to file')
        exit()
    elif (sys.argv[1] == '-p' or sys.argv[1] == '--path'):
        path=sys.argv[2]
    else:
        print('Invalid arguments.')
        print('Type -h or --help to get help')
        exit()

    file_exists = exists(path)
    if (file_exists==False):
        print('Invalid file path. Type correct path')
        exit()
    else:
        print("File exists. Path OK") #
    image = open_image_in_hsv(path)
    cv.imshow("HSV source image", image)
    cv.waitKey(0)

if __name__ == "__main__":
    main()