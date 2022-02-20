import argparse
import file_reader as reader

def write_list_to_file(output_file, lst):
    with open(output_file, 'w') as f:
        [f.write(word + "\n") for word in lst]
    reader.print_file_content(output_file) 

if __name__ == '__main__':
    '''Excercise 1.2'''
    parser = argparse.ArgumentParser(description='A program that writes the typed to a given file')
    parser.add_argument('file_path', help='The files path from where you get content from')
    parser.add_argument('input', help='Write what it should say in the file', type=lambda sentence: [str(word) for word in sentence.split(',')])
    args = parser.parse_args()
    write_list_to_file(str(args.file_path), [str(word) for word in args.input])


