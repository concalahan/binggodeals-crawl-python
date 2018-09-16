from spider import Spider
from general import *
from list_definition import *
from matching_products import matchingProduct

def main():
    PROJECT_NAME = "URL"
    tikiSpider = Spider(PROJECT_NAME, "tiki")
    adayroiSpider = Spider(PROJECT_NAME, "adayroi")

    write_phone_to_list(PROJECT_NAME)
<<<<<<< HEAD
    tikiMatching = matchingProduct(PROJECT_NAME,'adayroi')
    tikiMatching.matching()
=======
    # tikiMatching = matchingProduct(PROJECT_NAME,'tiki')
    # tikiMatching.matching()
>>>>>>> f8d43e8d341cc23818caafa0eeaf224a6d6856ef

if __name__ == "__main__":
    main()
