# main.py
import os
import schedule
import time

from api_calls import listFuturesContracts
from message_broker import publishResult

def updateListFuturesContract():
    result = listFuturesContracts()
    publishResult(result, 'futureContracts')

# Schedule the job to run every minute
schedule.every(1).minutes.do(updateListFuturesContract)

while True:
    schedule.run_pending()
    time.sleep(1)