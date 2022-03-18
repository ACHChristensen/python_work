import argparse
import requests
import json
from concurrent.futures import ThreadPoolExecutor

class NotFoundException(Exception):
    pass

class TextComparer():

    def __init__(self, url_list=[]):
        self.url_list = url_list

    def download(self, url, filename):
        try: 
            content = requests.get(url)
            if(content.status_code == 404):
                raise NotFoundException()
            with open(filename, 'w') as file:
                [file.write(word) for word in str(content.json())]
                print(str(filename))
        except NotFoundException:
            print("404 - Wrong URL!")
    
    def multidownload(self):
        with ThreadPoolExecutor(len(self.url_list)): 
            for url in self.url_list:
                url_splitted = url.split('.')
                self.download(url, url_splitted[1])

    def __iter__(self):
        return self

    def __next__(self):
        #Hvad skal dette ?
        return

    def urllist_generator(self):
        return lambda url: (for url in self.url_list : url)

        
#for url in self.url_list:
        #    self.url_list.remove(url)
        #    if(self.url_list.size_of == 0):
        #        raise StopIteration
        #return url

if __name__ == '__main__':
    '''Only for testing'''
    #parser = argparse.ArgumentParser()
    #parser.add_argument('url_path')
    #parser.add_argument('file_name')
    #args = parser.parse_args()
    #url_lst = []
    #url_lst.append(args.url_path)
    #TextComparer.download(str(args.url_path), str(args.file_name))

    text_comparer = TextComparer(["http://api.openweathermap.org/data/2.5/forecast", "https://api.github.com/search/repositories?q=language:python&sort=stars"])
    text_comparer.multidownload()