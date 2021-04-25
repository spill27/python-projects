# thread locking
# race condition: the same resource used by different threads
# deadlock: multiple threads waiting on the same resource
# GIL = Global Interpreter Lock

import logging
import threading
from concurrent.futures import ThreadPoolExecutor
import time
import random

counter = 0

#Test function
def test(count):
    global counter
    threadname = threading.current_thread().name
    logging.info(f'Starting: {threadname}')

    for x in range(count):
        logging.info(f'Count: {threadname} += {count}')
        
        # # the GIL in action  (bad way of writing code, but still works in pyhton thanks to GIL)
        # counter += 1

        # # locking (old schoold way)
        # lock = threading.Lock()
        # lock.acquire()
        # try:
        #     counter += 1
        # finally:
        #     lock.release()

        # locking simplified (new school, python style)
        lock = threading.Lock()
        with lock:
            logging.info(f'Locked: {threadname}')
            counter += 1
            time.sleep(2)


    logging.info(f'Completed: {threadname}')


def main():
    logging.basicConfig(format='%(levelname)s - %(asctime)s.%(msecs)03d: %(message)s', datefmt='%H:%M:%S', level=logging.DEBUG)
    logging.info('App Starting')
    # do something here

    workers = 2
    with ThreadPoolExecutor(max_workers=workers) as ex:
        for x in range(workers*2):  # more works than workers
            v = random.randrange(1,5)
            ex.submit(test, v)  #calling a function with a parameter

    print(f'Counter: {counter}')
    logging.info('App Finished')

if __name__ == "__main__":
    main()