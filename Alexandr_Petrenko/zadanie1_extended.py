import cv2
import numpy
import os


def checkFile(path: str) -> bool:
    return os.path.isfile(path)


def cvOpenImg(path: str) -> numpy.ndarray:
    return cv2.imread(path)


def main():
    h1, s1, v1, h2, s2, v2 =  0, 14, 205, 3, 255, 255
    h_min = numpy.array((h1, s1, v1), numpy.uint8)
    h_max = numpy.array((h2, s2, v2), numpy.uint8)
    image_path = os.path.normpath(input("type way to the picture: "))
    if checkFile(image_path) is False:
        print("this file does not exsist ")
        return
    image_dir = os.path.dirname(image_path)
    image_basename = os.path.basename(image_path)
    image_name, image_extension = os.path.splitext(image_basename)
    save_path = input("type way to save the picture: ")
    save_path = os.path.normpath(save_path) if bool(save_path) else fr"{image_dir}\{image_name}_mask{image_extension}"

    img = cvOpenImg(image_path)
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, h_min, h_max)
    print(f"color range HSV: {h_min}-{h_max}")
    mask = cv2.bitwise_and(img, img, mask=mask)
    cv2.imwrite(save_path, mask)
    print(f"picture saved {save_path}")


if __name__ == '__main__':
    main()
    input(" enter to esc. \n")
    exit()
