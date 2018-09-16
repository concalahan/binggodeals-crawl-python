# encoding=utf8

from html.parser import HTMLParser
from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib import parse
import datetime
import sys
import os, os.path

sys.path.append(os.path.realpath('..'))

def create_project_dir(directory):
    if not os.path.exists(directory) :
        print('Create directory : ' + directory)
        os.makedirs(directory)
    else:
        print(directory + ' is already created !')

# pre-processing the url for save as file name
def preprocessing_url(url):
    # delete every thing after ?, ex: ?src="bla bla"
    url = url.split('?', 1)[0]

    # delete the protocol
    if 'https://' in url:
        url = url[8:]
    else:
        url = url[7:]

    # delete .
    for ch in ['.vn/','.com/', '.net/']:
        if ch in url:
            url = url.replace(ch, "|")

    return url

def main():
    if(len(sys.argv) != 2):
        print("Arguments must be in format: python3 main.py HOMEPAGE")
        return

    PROJECT_NAME = sys.argv[1]

    # read from another project
    READ_DIR = '../crawl_url/' + PROJECT_NAME + '/'

    now = datetime.datetime.now()

    # save to this directory
    WRITE_DIR = '../data/' + str(now.year) + '/' + str(now.month) + '/' + str(now.day) + '/raw/'

    # create the directory if not empty
    create_project_dir(WRITE_DIR)

    with open(READ_DIR + "queue.txt") as fp:
        for url in fp:
            print("Processing file " + str(url))

            soup = BeautifulSoup(urlopen(url))

            url = preprocessing_url(url)
            
            # if the url ending with .html (ex: tiki.vn)
            if '.html' in url and '/' not in url:
                # the example result:
                # tiki|bo-dien-thoai-nokia-x5-32gb-3gb.html
                with open(WRITE_DIR + str(url), 'w') as the_file:
                    the_file.write(str(soup))
            elif '/' not in url:
                with open(WRITE_DIR + str(url) + '.html', 'w') as the_file:
                    the_file.write(str(soup))
            
if __name__== "__main__":
    main()