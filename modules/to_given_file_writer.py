import argparse
import file_reader as reader
import os
import file_writer as writer

class empty_file(Exception):
    pass

def validate_writing(from_file, new_file):
        if(os.path.exists(from_file)):
            with open(from_file) as f:
                words = [word for word in f]
            writer.write_list_to_file(new_file, words)
        else: 
            reader.print_file_content(from_file) 

if __name__ == '__main__':
    '''Excercise 2.1'''
    parser = argparse.ArgumentParser(description='A program that writes the typed to a given file')
    parser.add_argument('file_path', help='The files path from where you get content from')
    parser.add_argument('--file', help='Write what it should say in the file')
    args = parser.parse_args()
    validate_writing(str(args.file_path), args.file)
    


