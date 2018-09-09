from crontab import CronTab
 
my_cron = CronTab(user='root')

# crawl the url every day
crawl_url_job = my_cron.new(command='python3 crawl_url/main.py')
crawl_url_job.day.every(1)
my_cron.write()

parse_url_to_html_job = my_cron.new(command='python3 parse_url_to_html/main.py')
parse_url_to_html_job.day.every(2)
my_cron.write()

filter_data_from_file_job = my_cron.new(command='python3 filter_data_from_file/main.py')
filter_data_from_file_job.day.every(3)
my_cron.write()

save_db_job = my_cron.new(command='python3 save_db/main.py')
save_db_job.day.every(2)
my_cron.write()

# for stoping the cron task
# my_cron.remove_all()
# my_cron.write()