from spider import Spider
from general import *
from list_definition import *
from matching_products import matchingProduct


def main():
    PROJECT_NAME = "URL"
    tikiSpider = Spider(PROJECT_NAME, "tiki")
    adayroiSpider = Spider(PROJECT_NAME, "adayroi")
    cellphonesSpider = Spider(PROJECT_NAME, "cellphones")
<<<<<<< HEAD
    tgddSpider = Spider(PROJECT_NAME, 'thegioididong')

    create_compare_list_of_phones(PROJECT_NAME)

    tiki_matching = matchingProduct(PROJECT_NAME, 'tiki')
    tiki_matching.matching_by_url()
    adayroi_matching = matchingProduct(PROJECT_NAME, 'adayroi')
    adayroi_matching.matching_by_url()
=======
    
    create_compare_list_of_phones(PROJECT_NAME)
    
    tiki_matching = matchingProduct(PROJECT_NAME, 'tiki')
    tiki_matching.matching()
    # adayroi_matching = matchingProduct(PROJECT_NAME, 'adayroi')
    # adayroi_matching.matching()
>>>>>>> 97aaf61b9778fca6b8f2b18d67f18f2b9ccade21
    cellphones_matching = matchingProduct(PROJECT_NAME, 'cellphones')
    cellphones_matching.matching_by_url()
    thegioididong_matching = matchingProduct(PROJECT_NAME, 'thegioididong')
    thegioididong_matching.matching_by_url()

    print("Program Finish !")


if __name__ == "__main__":
    main()
