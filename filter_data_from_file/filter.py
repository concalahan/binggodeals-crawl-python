from html.parser import HTMLParser
from bs4 import BeautifulSoup
import html2text
import sys
import os, os.path
import json
import datetime
from parser import Parser

sys.path.append(os.path.realpath('..'))

class Filter:
    READ_DIR = ''
    WRITE_DIR = ''

    def create_project_dir(directory):
        if not os.path.exists(directory) :
            print('Create directory : ' + directory)
            os.makedirs(directory)
        else:
            print(directory + ' is already created !')

    def __init__(self):
        self.boot()
        self.filter_data()

    @staticmethod
    def boot():
        now = datetime.datetime.now()

        # read data from this directory
        READ_DIR = '../data/' + str(now.year) + '/' + str(now.month) + '/' + str(now.day) + '/raw/'

        # read data from this directory
        WRITE_DIR = '../data/' + str(now.year) + '/' + str(now.month) + '/' + str(now.day) + '/json/'

        # save to class variable
        Filter.READ_DIR = READ_DIR
        Filter.WRITE_DIR = WRITE_DIR

        # create the directory if not empty
        Filter.create_project_dir(WRITE_DIR)

    @staticmethod
    def filter_data():

        # get number of files in directory
        export_files_length = len([name for name in os.listdir(Filter.READ_DIR) if os.path.isfile(os.path.join(Filter.READ_DIR, name))])

        for filename in os.listdir(Filter.READ_DIR):
            print("Processing file: " + str(filename))

            with open(Filter.READ_DIR + filename) as fp:
                data = {}

                parser = Parser()
                if 'tiki' in filename:
                    data = parser.parseProductFromTiki(filename, fp)
                elif 'adayroi' in filename:
                    data = parser.parseProductFromAdayroi(filename, fp)

                if '.html' in filename and '/' not in filename:
                    # write that object to json
                    with open(Filter.WRITE_DIR + filename + '.json', 'w') as outfile:
                        json.dump(data, outfile)
                elif '/' not in filename:
                    with open(Filter.WRITE_DIR + filename + '.json', 'w') as outfile:
                        json.dump(data, outfile)

