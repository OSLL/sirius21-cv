import cv2 as cv
import os.path

def main():
    path_file = input("Bведите путь к файлу:")
    while (not os.path.exists(path_file)):
        print("Такой файл не существует")
        path_file = input("Bведите путь к файлу:")
    img = cv.imread(path_file, 1)
    cv.imshow("win1", img)

if __name__ == "__main__":
    main()
