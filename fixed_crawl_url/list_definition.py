from general import *

SITE_LIST = ["tiki", "adayroi"]

BRAND_LIST = ["apple", "samsung", "oppo", "nokia", "asus", "sony", "xiaomi"]

APPLE_PHONE = ["iphone 5s", "iphone 6", "iphone 6 plus", "iphone 6s", "iphone 6s plus", "iphone 7", "iphone 7 plus",
               "iphone 8", "iphone 8 plus ", "iphone se",
               "iphone x", "iphone xr", "iphone xs", "iphone xs max"]

SAMSUNG_PHONE = ["galaxy note 9", "galaxy s9", "galaxy note 8", "galaxy s8", "galaxy s7", "galaxy j2", "galaxy j3",
                 "galaxy j4", "galaxy j6", "galaxy j7", "galaxy j8", "galaxy a6", "galaxy a6 plus",
                 "galaxy a7", "galaxy a8",
                 "galaxy s8 plus", "galaxy s9 plus",
                 "galaxy a8 plus", "galaxy a8 star", "galaxy j7 plus", "galaxy j7 pro", "galaxy j6 plus",
                 "galaxy j6 prime", "galaxy j4 plus", "galaxy j4 prime",
                 "galaxy j3 pro"]

OPPO_PHONE = ['oppo find x', 'oppo r7s', "oppo a3s", 'oppo f1 plus', 'oppo f3 lite', 'oppo f3 plus', 'oppo f5',
              'oppo f7 youth', 'oppo a83',
              'oppo f3', "oppo f1s", "oppo f7", "oppo f9", "oppo a71", 'oppo r17']

NOKIA_PHONE = ["nokia 216", "nokia x5", "nokia x6", "nokia 1", "nokia 2", "nokia 3", "nokia 5", "nokia 6", "nokia 7",
               "nokia 8", "nokia 9", 'nokia 105', 'nokia 130', 'nokia 150']

ASUS_PHONE = ['rog phone', 'zenfone 5z', 'zenfone live l1', 'zenfone max m2',
              'zenfone max pro m1',
              'zenfone max plus m1', 'zenfone max pro m2', 'zenfone 4 max']

SONY_PHONE = ["xperia l1", "xperia l2", "xperia xz1", "xperia xa", "xperia xa1 ultra",
              "xperia xa1 plus", "xperia xa2", "xperia l2", "xperia xz dual", "xperia xzs"]

XIAOMI_PHONE = ["mi max 3", "mi max 2", "mi 8", "mi 8 pro", "redmi 6",
                "redmi 6a", "redmi note 6 pro", "redmi s2", "redmi 5 plus", "redmi 5",
                "redmi 5a", "mi 8 se", "mi 8 lite", "redmi note 5", "redmi note 5a",
                "mi 6x",
                "mi a1", "mi a2", "redmi 4x",
                "mi mix 2", "mi mix 2s"]


def create_compare_list_of_phones(project_name):
    for brand in BRAND_LIST:
        brand_phone = brand.upper() + '_PHONE'
        path = project_name + '/' + brand + '/phones_list.txt'
        print(path + ' is created ...')
        for phone in eval("%s " % brand_phone):
            append_to_file(path, phone)

        # sorting products name and then reverse the list from bottom to top
        new_list_product = list()
        product_set = file_to_set(path)
        for item in product_set:
            new_list_product.append(item)

        set_to_file(reversed(new_list_product), path)
