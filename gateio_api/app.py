# main.py
import schedule
import time

from mb import publishMessage
from api_calls import listFuturesContracts


def updateListFuturesContract():
    result = listFuturesContracts()
    publishMessage(result, 'futureContracts')

# Schedule the job to run every minute
schedule.every(1).minutes.do(updateListFuturesContract)

while True:
    schedule.run_pending()
    time.sleep(1)