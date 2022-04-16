import sys


def main():
    path = ''

    # Начало кода решения
    data = sys.argv[1:]
    length = len(data)
    if length and (data[0] == "-h" or data[0] == "--help"):
        print("Use flag -p or --path to specify path to file")
    elif length and (data[0] == "-p" or data[0] == "--path"):
        path = data[1]
    else:
        print('Invalid arguments.\nType -h or --help to get help')
    # print(sys.argv)
    # Конец кода решения

    print(path)


if __name__ == "__main__":
    main()
