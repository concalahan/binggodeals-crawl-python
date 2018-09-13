from crontab import CronTab
import os

dir_path = os.path.dirname(os.path.abspath(__file__))
my_cron = CronTab(user='root')

PROJECT_NAME = ['tiki.vn', 'adayroi.com']
CATEGORY_URL = ['https://tiki.vn/dien-thoai-may-tinh-bang/c1789', 'https://www.adayroi.com/dien-thoai-di-dong-c323']

for i in range(0,2):
    # crawl the url every day
    crawl_url_job = my_cron.new(
        command='cd ' + dir_path + '/crawl_url; python3 main.py ' + PROJECT_NAME[i] + ' ' + CATEGORY_URL[i],
        comment='crawl url and store in /crawl_url/site_name')
    crawl_url_job.day.every(1)
    my_cron.write()

    parse_url_to_html_job = my_cron.new(
        command='cd ' + dir_path + '/parse_url_to_html; python3 main.py ' + PROJECT_NAME[i],
        comment='read the file contain all url, request and save to disk')
    parse_url_to_html_job.day.every(2)
    my_cron.write()

    filter_data_from_file_job = my_cron.new(
        command='cd ' + dir_path + '/filter_data_from_file; python3 main.py ' + PROJECT_NAME[i],
        comment='read .html file, filter data and save to .json file')
    filter_data_from_file_job.day.every(3)
    my_cron.write()

    save_db_job = my_cron.new(
        command='cd ' + dir_path + '/save_db; python3 influxdb-app.py',
        comment='read .json file and save to influxdb')
    save_db_job.day.every(4)
    my_cron.write()

# for stoping the cron task
# my_cron.remove_all()
# my_cron.write()