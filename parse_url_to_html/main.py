# encoding=utf8

from html.parser import HTMLParser
from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib import parse
import sys
import os, os.path

sys.path.append(os.path.realpath('..'))

PROJECT_NAME = 'tiki'

# read from another project
READ_DIR = '../crawl_url/' + PROJECT_NAME + '/'

# save to this directory
WRITE_DIR = '../data/raw_products/'

def create_project_dir(directory):
    if not os.path.exists(directory) :
        print('Create directory : ' + directory)
        os.makedirs(directory)
    else:
        print(directory + ' is already created !')

def main():
    # create the directory if not empty
    create_project_dir(WRITE_DIR)

    with open(READ_DIR + "queue.txt") as fp:
        index = 0
        for url in fp:
            soup = BeautifulSoup(urlopen(url),"lxml")

            with open(WRITE_DIR + '[' + PROJECT_NAME + ']raw_' + str(index) + '.html', 'w') as the_file:
                the_file.write(str(soup))
            
            index += 1

if __name__== "__main__":
    main()