import argparse

def main():
    parser = argparse.ArgumentParser(description='Compares two comfiguration files and shows a difference.')
    parser.add_argument('-f', '--format', help='set format of output')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    p = parser.parse_args()
    print(p)


if __name__ == '__main__':
    main()