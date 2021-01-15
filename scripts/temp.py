import time
from datetime import datetime
import schedule


def job():
    print('some task')


schedule.every(12).hours.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
