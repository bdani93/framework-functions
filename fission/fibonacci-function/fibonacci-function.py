from flask import request
from flask import current_app
import logging
import datetime

def Fibonacci(n):
    a = 0
    b = 1
    global eredmeny
    if n < 0:
        return "Incorrect input\n"
    elif n == 0:
        return str(a)
    elif n == 1:
        return str(b)
    else:
        for i in range(1,n):
            c = a + b
            a = b
            b = c
        eredmeny = b
        return str(eredmeny)

def main():
    start_time = datetime.datetime.now()
    current_app.logger.info('Invoke Started at: ' + str(start_time.time()))
    n = int(request.args.get('num'))
    ered = Fibonacci(n)
    finish_time = datetime.datetime.now()
    current_app.logger.info('Invoke Finished at: ' + str(finish_time.time()))
    current_app.logger.info('Invoke Duration: ' + str(finish_time-start_time))
    return ered
