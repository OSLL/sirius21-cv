from os.path import exists


def main():
    path = ''  # эту строчку можно изменять для тестирования программы

    # Начало кода решения
    if not exists(path):
        return
    # Конец кода решения

    print("File exists. Path OK")  # эту строчку перемещать и изменять нельзя


if __name__ == "__main__":
    main()
