##-*- coding: utf-8 -*-
# encoding=utf8  
import schedule
import time
import subprocess
import logging
from crawler import run

logger = logging.getLogger('main')
names = ['36Kr股权投资', '优投网', '高新园区金融平台', '天使汇', '中关村创业大街',  '真格基金', '无界空间','清华校友tmt协会',  '国银基金', '清创孵化器', '创伙伴', 'IC咖啡']
counter = 0;
# print names[counter]

def crawler():
    global counter 
    counter += 1
    counter = counter % len(names)
    # print 'aaa'
    print names[counter]
    logger.info("I'm working..." + time.ctime())
    CASPERJS_EXECUTABLE = "casperjs" # <-- here you put the path to you casperjs executable
    CASPERJS_SCRIPT = "./js/dy_crawler.js" # this is the name of the script that casperjs should execute
    stdout_as_string = subprocess.Popen([CASPERJS_EXECUTABLE, CASPERJS_SCRIPT, names[counter]])
    # print 'bbb'
    # print stdout_as_string
def analysis():
    logger.info("I'm working..." + time.ctime())
    run()

schedule.every().minutes.do(crawler)
schedule.every().day.do(analysis)

while True:
    schedule.run_pending()
    time.sleep(1)





