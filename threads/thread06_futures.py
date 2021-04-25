# Queue and Futures

"""
Queue is like leaving a message
A Future is used for synchronizing program execution
in some concurrent programming languages. They describe and 
objecy taht acts as a proxy for a result that is initially unknown
usually because the computation of its value is not yet complete.
"""

import logging
import threading
from threading import Thread
from concurrent.futures import ThreadPoolExecutor
import time
import random
from queue import Queue

# Queues

def test_que(name, que):
    # code running on the thread
    threadname = threading.current_thread().name
    logging.info(f'Starting: {threadname}')
    time.sleep(random.randrange(1,5))
    logging.info(f'Finish: {threadname}')
    ret = 'Hello ' + name + ' your rnd number is : ' + str(random.randrange(1,10))
    que.put(ret)

def queued():
    que = Queue()
    t = Thread(target=test_que, args=['Bryan', que])
    t.start()
    logging.info('Do something on the main thread')
    t.join()
    ret = que.get()
    logging.info(f'Returned: {ret}')


# test futures
def test_future(name):
    # code running on the thread
    threadname = threading.current_thread().name
    logging.info(f'Starting: {threadname}')
    time.sleep(random.randrange(1,5))
    logging.info(f'Finish: {threadname}')
    ret = 'Hello ' + name + ' your rnd number is : ' + str(random.randrange(1,100))
    return ret

def pooled():
    workers = 20
    ret = []
    with ThreadPoolExecutor(max_workers=workers) as ex:
        for x in range(workers):
            v = random.randrange(1,5)
            future = ex.submit(test_future, 'Bryan ' + str(x))
            ret.append(future)
    logging.info('Do something on the main thread')
    for r in ret:
        logging.info(f'Returned: {r.result()}')



def main():
    logging.basicConfig(format='%(levelname)s - %(asctime)s.%(msecs)03d: %(message)s', datefmt='%H:%M:%S', level=logging.DEBUG)
    logging.info('App Starting')
    # do something here
    pooled()
    logging.info('App Finished')

if __name__ == "__main__":
    main()