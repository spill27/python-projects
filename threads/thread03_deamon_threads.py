# Deamon threads
# runs and executes in the background
# Quitting when we quit the app

import logging
import threading
from threading import Thread, Timer
import time

def test():
    threadname = threading.current_thread().name
    logging.info(f'Starting: {threadname}')
    for x in range(30):
        logging.info(f'Working: {threadname}')
        time.sleep(1.2)
    logging.info(f'Finished: {threadname}')

def stop():
    logging.info('Exiting the application')
    exit(0) # exit as expected -> shut everything down


def main():
    logging.basicConfig(format='%(levelname)s - %(asctime)s: %(message)s', datefmt='%H:%M:%S', level=logging.DEBUG)
    logging.info('Main thread Starting')
    # do something here
    # stop in 3 seconds
    timer = Timer(5, stop)  # in 3 seconds call the function stop
    timer.start()

    # run a thread
    #t = Thread(target=test, daemon=False) # the thread runs on also after the application is closed
    t = Thread(target=test, daemon=True) # this thread stops when the applications stops
    t.start()

    logging.info('Main thread Finished')

if __name__ == "__main__":
    main()