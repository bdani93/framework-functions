
import logging
import datetime

logging.basicConfig(level=logging.INFO)

def handle(req):
    logging.basicConfig(filename='measure.log',level=logging.DEBUG)
    start_time = datetime.datetime.now()
    logging.info('Invoke Started at: ' + str(start_time.time()))
    finish_time = datetime.datetime.now()
    logging.info('Invoke Finished at: ' + str(finish_time.time()))
    logging.info('Invoke Duration: ' + str(finish_time - start_time))
    print("Hello Openfaas!")
