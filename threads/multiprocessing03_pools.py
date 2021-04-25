# intro to multiprocessing pool

import logging
import multiprocessing
from multiprocessing.context import Process
import time
import random


# worker process
def work(item, count):
    name = multiprocessing.current_process().name
    logging.info(f'Started: {name} {item}')
    for x in range(count):
        logging.info(f'{name}: {item} = {x}')
        time.sleep(1)
    logging.info(f'Finished: {name}')
    return item + ' is finished'

#main process
def proc_result(result):
    logging.info(f'Result = {result}')

def main():
    logging.info(f'App started')

    max = 5
    pool = multiprocessing.Pool(max)
    results = []
    for x in range(max):
        item = 'Item' + str(x)
        count = random.randrange(1,10)
        # apply_async creates all the processes at once
        r = pool.apply_async(work, [item, count], callback=proc_result)
        results.append(r)

    # wait for the processes
    for r in results:
        r.wait()

    # pool.close() or pool.terminate
    pool.close()
    pool.join()
    
    logging.info(f'App finished')


logging.basicConfig(format='%(levelname)s - %(asctime)s.%(msecs)03d: %(message)s', datefmt='%H:%M:%S', level=logging.DEBUG)
if __name__ == "__main__":
    main()