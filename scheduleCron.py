from crontab import CronTab
import os

dir_path = os.path.dirname(os.path.abspath(__file__))
my_cron = CronTab(user='root')

# crawl the url every day
crawl_url_job = my_cron.new(
    command='cd ' + dir_path + '/fixed_crawl_url; python3 main.py',
    comment='crawl url and store in /fixed_crawl_url/site_name')
crawl_url_job.day.every(1)
my_cron.write()

parse_url_to_html_job = my_cron.new(
    command='cd ' + dir_path + '/parse_url_to_html; python3 main.py',
    comment='read the file contain all url, request and save to disk')
parse_url_to_html_job.day.every(3)
my_cron.write()

filter_data_from_file_job = my_cron.new(
    command='cd ' + dir_path + '/filter_data_from_file; python3 main.py',
    comment='read .html file, filter data and save to .json file')
filter_data_from_file_job.day.every(5)
my_cron.write()

save_db_job = my_cron.new(
    command='cd ' + dir_path + '/save_db; python3 influxdb-app.py',
    comment='read .json file and save to influxdb')
save_db_job.day.every(7)
my_cron.write()

# for stoping the cron task
# my_cron.remove_all()
# my_cron.write()