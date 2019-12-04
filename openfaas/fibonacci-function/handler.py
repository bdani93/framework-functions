import logging
import datetime

logging.basicConfig(level=logging.INFO)

def handle(req):
    logging.basicConfig(filename='measure.log',level=logging.DEBUG)
    start_time = datetime.datetime.now()
    logging.info('Invoke Started at: ' + str(start_time.time()))
    a = 0
    b = 1
    num = int(req)
    global eredmeny
    if num < 0:
        print("Incorrect input\n")
    elif num == 0:
        print(str(a))
    elif num == 1:
        print(str(b))
    else:
        for i in range(1,num):
            c = a + b
            a = b
            b = c
        eredmeny = b
        finish_time = datetime.datetime.now()
        logging.info('Invoke Finished at: ' + str(finish_time.time()))
        logging.info('Invoke Duration: ' + str(finish_time - start_time))
        return (str(eredmeny))

