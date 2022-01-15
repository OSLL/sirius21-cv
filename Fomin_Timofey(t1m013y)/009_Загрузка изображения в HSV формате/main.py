import cv2 as cv
import numpy


# Начало кода решения
def open_image_in_hsv(image_path: str) -> numpy.ndarray:
    img = cv.imread(image_path)
    img = cv.cvtColor(img, cv.COLOR_BGR2HSV)
    return img
# Конец кода решения


def main():  # в функции main ничего изменять не надо
    path = 'img/1red.jpg'

    image = open_image_in_hsv(path)
    cv.imshow("HSV source image", image)

    cv.waitKey(0)


if __name__ == "__main__":
    main()
