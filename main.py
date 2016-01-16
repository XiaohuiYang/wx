##-*- coding: utf-8 -*-
# encoding=utf8  
import schedule
import time
import subprocess
import mylog
import ConfigParser

from crawler import run


cf = ConfigParser.ConfigParser()
 
cf.read("config.conf")
names = cf.get("wx", "names")

logger = mylog.logger


# fh = logging.FileHandler('test.log') 
# fh.setLevel(logging.DEBUG) 
# formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s') 
# fh.setFormatter(formatter)

# logger = logging.getLogger('main')
# logger.addHandler(fh)

counter = 0;
# print names[counter]

def crawler():
    global counter 
    counter += 1
    counter = counter % len(names)
    # print 'aaa'
    print names[counter]
    logger.info("启动casper抓取账号" + names[counter]+ " at "+ time.ctime())
    CASPERJS_EXECUTABLE = "casperjs" # <-- here you put the path to you casperjs executable
    CASPERJS_SCRIPT = "./js/dy_crawler.js" # this is the name of the script that casperjs should execute
    stdout_as_string = subprocess.Popen([CASPERJS_EXECUTABLE, CASPERJS_SCRIPT, names[counter]])
    # print 'bbb'
    # print stdout_as_string
def analysis():
    logger.info("开始分析" + time.ctime())
    run()

schedule.every(10).minutes.do(crawler)
schedule.every().day.at("15:06").do(analysis)

while True:
    schedule.run_pending()
    time.sleep(1)





