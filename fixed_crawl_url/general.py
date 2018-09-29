import os
import json, codecs


# Each website which is crawled is a separated project (folder)
def create_project_dir(directory):
    if os.path.exists(directory):
        print(directory + ' is already created !')
    else:
        print('Create directory : ' + directory)
        os.makedirs(directory)


def create_brand_dir(project_name, brand_name):
    print('Create brand directory ...')
    brand_dir = project_name + '/' + brand_name;
    if os.path.exists(brand_dir):
        print(brand_name + ' is already created !')
    else:
        print('Create brand directory ...')
        os.makedirs(brand_dir)


def create_data_files(project_name, site_name):
    path = project_name + '/' + site_name
    textfile = path + '/' + site_name + '_phone-urls.txt'
    create_project_dir(path)
    if not os.path.isfile(textfile):
        write_file(textfile, '')


def append_urls_to_file(project_name, site_name, links, brand_list):
    for brand_dir in brand_list:
        path = project_name + '/' + brand_dir + '/' + site_name + '/' + site_name + '_phone-urls.txt'
        for brand, url in links.items():
            if brand[0] == brand_dir:
                append_to_file(path, url)
        # Make list of urls in file become to a set and then return to file

        urls = file_to_set(path)
        set_to_file(urls, path)


def write_file(path, data):
    f = open(path, 'w+')
    f.write(data)
    f.close()


def append_to_file(path, data):
    if not os.path.isfile(path):
        f = open(path, 'w+')
        f.write('')
    with open(path, 'a') as file:
        file.write(data + '\n')


def delete_file_contents(path):
    with open(path, 'w'):
        pass


# Read a file then convert each line to set items
def file_to_set(file_name):
    results = set()
    with open(file_name, 'rt') as f:
        for line in f:
            results.add(line.replace('\n', ''))
    return sorted(results)


# Iterate through a set, each item will be a new line in the file
def set_to_file(links, file):
    delete_file_contents(file)
    for link in links:
        append_to_file(file, link)
