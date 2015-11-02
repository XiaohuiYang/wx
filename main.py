import schedule
import time
import subprocess
import logging
from crawler import run

logger = logging.getLogger('main')

def crawler():
    logger.info("I'm working..." + time.ctime())
    CASPERJS_EXECUTABLE = "casperjs" # <-- here you put the path to you casperjs executable
    CASPERJS_SCRIPT = "./js/dy_crawler.js" # this is the name of the script that casperjs should execute
    stdout_as_string = subprocess.check_output([CASPERJS_EXECUTABLE, CASPERJS_SCRIPT])
    logger.debug(stdout_as_string)
def analysis():
    logger.info("I'm working..." + time.ctime())
    run()

schedule.every(8).hours.do(crawler)
schedule.every().day.do(analysis)

while True:
    schedule.run_pending()
    time.sleep(1)





