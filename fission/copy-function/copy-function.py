from flask import request
from flask import current_app
import logging
import datetime
import sys
import os
import uuid

def read(destfile):
    with open(destfile) as destination:
        return destination.read()


def main():
    logging.basicConfig(filename='measure.log',level=logging.DEBUG)
    start_time = datetime.datetime.now()
    current_app.logger.info('Invoke Started at: ' + str(start_time.time()))
    srcdata = request.args.get('src')
    destfile = str(uuid.uuid4())
    with open(destfile, 'w') as text_file:
        text_file.write("Out: %s" % srcdata)

    finish_time = datetime.datetime.now()
    current_app.logger.info('Invoke Finished at: ' + str(finish_time.time()))
    current_app.logger.info('Invoke Duration: ' + str((finish_time - start_time).microseconds))
    return read(destfile) 
