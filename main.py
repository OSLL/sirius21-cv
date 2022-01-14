import sys

def main():
    path = ''

    # Начало кода решения
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
    # Конец кода решения

    print(path)


if __name__ == "__main__":
    main()