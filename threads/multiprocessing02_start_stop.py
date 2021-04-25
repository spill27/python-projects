# intro to multiprocessing

import logging
import multiprocessing
from multiprocessing.context import Process
import time


# worker process
def work(msg, max):
    name = multiprocessing.current_process().name
    logging.info(f'Started: {name}')
    for x in range(max):
        logging.info(f'{name} {msg}')
        time.sleep(1)
    logging.info(f'Finish: {name}')

#basic process usage
def main():
    logging.info(f'App started')

    max = 2
    worker = Process(target=work, args=['Working', max], daemon=True, name='Worker')
    worker.start()

    time.sleep(5)

    # if the process is running, stop it
    if worker.is_alive():
        worker.terminate()   # kill the process with SIGTERM
    worker.join()

    # exicode == 0 is good
    # anything else is an error
    logging.info(f'App finished: {worker.exitcode}')



logging.basicConfig(format='%(levelname)s - %(asctime)s.%(msecs)03d: %(message)s', datefmt='%H:%M:%S', level=logging.DEBUG)
if __name__ == "__main__":
    main()