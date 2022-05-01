def main():
    import cv2 as cv
    import os.path

    print("Hello World!")
    path_file = input("Bведите путь к файлу:")
    if os.path.exists(path_file):
        img = cv.imread(path_file, 1)
        mask_low, mask_hi = (55, 100, 100), (255, 255, 255)
        img_mask = cv.inRange(img, mask_low, mask_hi)
        cv.imshow("win1", img)
        cv.imshow("win2", img_mask)
        cv.waitKey(0)
        cv.destroyAllWindows()
    else:
        print("Такой файл не существует")

if __name__ == "__main__":
    main()