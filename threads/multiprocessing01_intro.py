# intro to multiprocessing
# a process has its own memory space and its own threads

import logging
import multiprocessing
from multiprocessing import process
import time

# starting function for our process
def run(num):
    name = process.current_process().name
    logging.info(f'Running: {name} as {__name__}')
    time.sleep(num*2)
    logging.info(f'Finish: {name}')

#basic process usage
def main():
    #logging.basicConfig(format='%(levelname)s - %(asctime)s.%(msecs)03d: %(message)s', datefmt='%H:%M:%S', level=logging.DEBUG)
    name = process.current_process().name
    logging.info(f'Running: {name} as {__name__}')

    processes = []
    for x in range(5):
        p = multiprocessing.Process(target=run, args=[x], daemon=True)
        processes.append(p)
        p.start()

    # wait for the processes to finish
    for p in processes:
        p.join()

    logging.info(f'Finish: {name}')


logging.basicConfig(format='%(levelname)s - %(asctime)s.%(msecs)03d: %(message)s', datefmt='%H:%M:%S', level=logging.DEBUG)
if __name__ == "__main__":
    main()