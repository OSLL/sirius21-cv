import cv2 as cv

# Начало кода решения
def open_image_in_hsv(path):
    img = cv.cvtColor(cv.imread(path), cv.COLOR_RGB2HSV)
    return img
# Конец кода решения


def main(): # в функции main ничего изменять не надо
    path = r'img\1red.jpg'

    image = open_image_in_hsv(path)
    cv.imshow("HSV source image", image)

    cv.waitKey(0)


if __name__ == "__main__":
    main()
