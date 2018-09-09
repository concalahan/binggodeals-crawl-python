from crontab import CronTab

cron    = CronTab(user='root')
job = cron.new(command='python hello.py')  
job.day.every(1)
cron.write( 'output.tab' )