from bs4 import BeautifulSoup
from urllib.request import urlopen
from general import write_json_file

def export_to_json(project_name):
    product_name = ''
    product_url = ''
    branch_name = ''
    store = ''
    price = ''
    feature_discription = ''
    table_info = ''
    detail_discription = ''
    
    directory = project_name + '/queue.txt'
    list_infomation = list()
# =============================================================================
#     with open (directory,'r') as file:
#         for url in file:
#             soup = BeautifulSoup(urlopen(url),"lxml")
# =============================================================================
    url = 'https://tiki.vn/dien-thoai-vivo-v9-hang-chinh-hang-p1735843.html?src=category-page'
    list_infomation.append('url : ' + url)
    soup = BeautifulSoup(urlopen(url),"lxml")
    # Get product name
    h1 = soup.find("h1", {"class":"item-name","itemprop":"name","id":"product-name"})
    product_name = h1.get_text()
    list_infomation.append('product_name : ' +  product_name.strip())
    #print(product_name.strip())
    
    #get branch name
    branch_div = soup.find("div", {"class":"item-brand"})
    branch_name = branch_div.find('a').get_text()
    list_infomation.append('branch_name : ' + branch_name)
    #print(branch_name)
    write_json_file('test.json',list_infomation)
    
    
    
    
