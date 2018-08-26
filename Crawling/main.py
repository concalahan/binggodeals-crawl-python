import threading
from queue import Queue
from spider import Spider
from domain import *
from general import *


PROJECT_NAME = 'tiki'
HOMEPAGE = 'https://tiki.vn/dien-thoai-may-tinh-bang/c1789?src=mega-menu'
QUEUE_FILE = PROJECT_NAME + '/queue.txt'
CRAWLED_FILE = PROJECT_NAME + '/crawled.txt'
NUMBER_OF_THREADS = 8

#queue = Queue()
Spider(PROJECT_NAME, HOMEPAGE)