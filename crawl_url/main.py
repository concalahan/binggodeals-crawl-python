import threading
from queue import Queue
from spider import Spider
from general import *
from json_export import *
import sys

def main():
    # Get the argument
    arg_len = len(sys.argv)

    if(arg_len != 3):
        print("Arguments must be in format: python3 main.py HOMEPAGE CATEGORY_URL")
        return

    # HOMEPAGE = 'tiki.vn'
    # CATEGORY_URL = 'https://tiki.vn/dien-thoai-may-tinh-bang/c1789'

    HOMEPAGE = sys.argv[1]
    CATEGORY_URL = sys.argv[2]

    # This sub-project is to crawl all the url in some sites and export to file
    QUEUE_FILE = HOMEPAGE + '/queue.txt'
    CRAWLED_FILE = HOMEPAGE + '/crawled.txt'
    NUMBER_OF_THREADS = 8

    #queue = Queue()
    Spider(HOMEPAGE, CATEGORY_URL)
    #export_to_json(PROJECT_NAME)

if __name__== "__main__":
    main()