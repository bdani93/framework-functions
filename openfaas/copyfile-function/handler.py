from flask import request
from flask import current_app
import logging
import datetime
import os

logging.basicConfig(level=logging.INFO)

def copy(srcfile, destfile):
    with open(srcfile) as source:
        with open(destfile, 'w') as destination:
            for line in source:
                destination.write(line)
    print("File copy is done")

def read(destfile):
    with open(destfile) as destination:
        return destination.read()


def handle(req):
    logging.basicConfig(filename='measure.log',level=logging.DEBUG)
    start_time = datetime.datetime.now()
    logging.info('Invoke Started at: ' + str(start_time.time()))
    current_dir = os.path.dirname(__file__)
    srcfile = str(request.args.get('src'))
    destfile = str(request.args.get('dest'))
    copy(os.path.join(current_dir, srcfile), os.path.join(current_dir, destfile))
    ered = read(os.path.join(current_dir, destfile))
    finish_time = datetime.datetime.now()
    logging.info('Invoke Finished at: ' + str(finish_time.time()))
    logging.info('Invoke Duration: ' + str((finish_time - start_time).microseconds))
    return ered
