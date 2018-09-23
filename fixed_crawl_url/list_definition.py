from general import *

SITE_LIST = ["tiki", "adayroi"]

BRAND_LIST = ["apple", "samsung", "oppo", "nokia", "asus", "sony", "xiaomi"]

APPLE_PHONE = ["iphone 6", "iphone 7", "iphone 8", "iphone X"]

SAMSUNG_PHONE = ["galaxy note 9", "galaxy s9", "galaxy note 8", "galaxy s8", "galaxy s7", "galaxy j2", "galaxy j3",
                 "galaxy j4", "galaxy j6", "galaxy j7", "galaxy j8", "galaxy a6", "galaxy a8"]

OPPO_PHONE = ["oppo a3s", "oppo f1s", "oppo f7", "oppo f9", "oppo f3 plus", "oppo a71"]


NOKIA_PHONE = ["nokia 216", "nokia 6", "nokia x5","nokia x6", "nokia 1", "nokia 2", "nokia 3"]

ASUS_PHONE = ['asus zenfone max pro m1', 'asus zenfone max plus m1', 'asus zenfone 4 max']

SONY_PHONE = ["sony xperia l1", "sony xperia xz1", "sony xperia xa1", "sony xperia l2", "sony xperia xzs", "sony xperia xzs"]

XIAOMI_PHONE = ["xiaomi mi max 3", "xiaomi mi max 2", "xiaomi mi 8", "xiaomi redmi note 5", "xiaomi mi 6x", "xiaomi mi a2"
                "xiaomi mi mix 2s"]

def create_compare_list_of_phones(project_name):
    for brand in BRAND_LIST:
        brand_phone = brand.upper() + '_PHONE'
        path = project_name + '/' + brand + '/phones_list.txt'
        print(path + ' is created ...')
        for phone in eval("%s " % brand_phone):
            append_to_file(path,phone)


