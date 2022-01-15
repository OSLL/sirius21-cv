import sys


def main():
    path = ''

    # Начало кода решения
    help_string = "Use flag -p or --path to specify path to file. "
    invalid_args_string = "Invalid arguments. \nType -h or --help to get help. "

    if len(sys.argv) < 2:
        print(invalid_args_string)
        return

    for arg in ['--help', '-h']:
        if sys.argv[1] == arg:
            if len(sys.argv) != 2:
                print(invalid_args_string)
                return
            print(help_string)
            return

    for arg in ['--help', '-h', '--path', '-p']:
        if sys.argv[1] == arg:
            break
    else:
        print(invalid_args_string)
        return

    for arg in ['--path', '-p']:
        if sys.argv[1] == arg:
            if len(sys.argv) != 3:
                print(invalid_args_string)
                return
            path = sys.argv[2]
            break
    # Конец кода решения

    print(path)


if __name__ == '__main__':
    main()
