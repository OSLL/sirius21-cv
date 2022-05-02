def main():
    import cv2 as cv
    import os.path

    #path_file = input("Bведите путь к файлу:")
    path_file = '../img/1red.jpg'
    if os.path.exists(path_file):
        img = cv.imread(path_file, 1)
        mask_low, mask_hi = (0, 100, 100), (255, 255, 255)
        img_mask = cv.inRange(img, mask_low, mask_hi)
        cv.imshow("win1", img)
        cv.imshow("win2", img_mask)
        path_file_mask = path_file.replace('.jpg', '_mask.jpg')
        print(path_file_mask)
        cv.imwrite(path_file_mask, img_mask)
        cv.waitKey(0)
        cv.destroyAllWindows()
    else:
        print("Такой файл не существует")

if __name__ == "__main__":
    main()
