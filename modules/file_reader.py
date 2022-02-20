import argparse
def print_file_content(file):
    with open(file) as f:
        print(f.name)
        for line in f:
            print(line)

if __name__ == '__main__':
    '''Excercise 1.1'''
    parser = argparse.ArgumentParser(description='A program that gets the content from file')
    parser.add_argument('file_path', help='The files path from where you get content from')
    args = parser.parse_args()
    print_file_content(str(args.file_path))



        