import logging
from threading import Thread
import time
import random


def longtask(name):
    max = random.randrange(1,10)
    logging.info(f'Task: {name} performing {str(max)} times')
    for x in range(max):
        logging.info(f'Task {name}: {x}')
        time.sleep(random.randrange(1,3))
    logging.info(f'Task: {name}: complete')


def main():
    logging.basicConfig(format='%(levelname)s - %(asctime)s: %(message)s', datefmt='%H:%M:%S', level=logging.DEBUG)
    logging.info('Starting')
    # do something here
    #longtask('main')
    # run this on multiple threads
    threads = []
    for x in range(10):
        t = Thread(target=longtask, args=['thread' + str(x)])
        threads.append(t)
        t.start()

    # wait for all threads to finish
    for t in threads:
        t.join()
    logging.info('Finished all threads')

if __name__ == "__main__":
    main()