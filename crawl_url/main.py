import threading
from queue import Queue
from spider import Spider
from general import *
from json_export import *

# This sub-project is to crawl all the url in some sites and export to file

PROJECT_NAME = 'tiki'
HOMEPAGE = 'https://tiki.vn/dien-thoai-may-tinh-bang/c1789'
QUEUE_FILE = PROJECT_NAME + '/queue.txt'
CRAWLED_FILE = PROJECT_NAME + '/crawled.txt'
NUMBER_OF_THREADS = 8

#queue = Queue()
Spider(PROJECT_NAME, HOMEPAGE)
#export_to_json(PROJECT_NAME)