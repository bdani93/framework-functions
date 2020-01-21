from flask import request
from flask import current_app
import logging
import datetime

def Fibonacci(n):
    global eredmeny
    if n < 0:
        return "Incorrect input\n"
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return Fibonacci(n-1)+Fibonacci(n-2)

def main():
    logging.basicConfig(filename='measure.log',level=logging.DEBUG)
    start_time = datetime.datetime.now()
    current_app.logger.info('Invoke Started at: ' + str(start_time.time()))
    n = int(request.args.get('num'))
    ered = Fibonacci(n)
    finish_time = datetime.datetime.now()
    current_app.logger.info('Invoke Finished at: ' + str(finish_time.time()))
    current_app.logger.info('Invoke Duration: ' + str((finish_time - start_time).microseconds))
    return str(ered)