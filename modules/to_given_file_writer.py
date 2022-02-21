import argparse
from pydoc import describe
import file_reader as reader
import os
import file_writer as writer

class empty_file(Exception):
    pass

def validate_writing(from_file, new_file):
        if(os.path.exists(new_file) & os.path.exists(from_file)):
                with open(from_file) as f:
                    words = [word for word in f]
                writer.write_list_to_file(new_file, words)
        elif(os.path.exists(from_file)): 
            reader.print_file_content(from_file) 
        else: 
            print("One or both does'nt has the right path - try again")

if __name__ == '__main__':
    '''Excercise 2.1 + 2.2'''
    parser = argparse.ArgumentParser(description='The program takes a existing file and copy content to another given file or print it to console')
    parser.add_argument('file_path', help='The files path from where you get content from')
    parser.add_argument('--file', help='Write what it should say in the file')
    args = parser.parse_args()
    parser.print_help()
    validate_writing(str(args.file_path), str(args.file))
    


