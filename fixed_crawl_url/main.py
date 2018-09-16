from spider import Spider
from general import *
from list_definition import *
from matching_products import matchingProduct

def main():
    PROJECT_NAME = "URL"
    tikiSpider = Spider(PROJECT_NAME, "tiki")
    adayroiSpider = Spider(PROJECT_NAME, "adayroi")

    write_phone_to_list(PROJECT_NAME)
    tikiMatching = matchingProduct(PROJECT_NAME,'adayroi')
    tikiMatching.matching()

if __name__ == "__main__":
    main()
