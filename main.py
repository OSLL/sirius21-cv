import sys

def main():
    if len(sys.argv) == 1:
        print("Invalid arguments.\n\nType -h or --help to get help")
        return
    if sys.argv[1] == '--help' or sys.argv[1] == '-h':
        print("Use flag -p or --path to specify path to file")
        return
    elif sys.argv[1] == '--path' or sys.argv[1] == '-p':
        path = sys.argv[2]
    else:
        print("Invalid arguments.\n\nType -h or --help to get help")
        return

    print(path)


if __name__ == "__main__":
    main()
