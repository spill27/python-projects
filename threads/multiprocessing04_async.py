# async code
# ASYNC CODE RUNNING IN THE SAME PROCESS AND SAME THREAD 
# ASYNC CODE RUNNING IN THE SAME PROCESS AND SAME THREAD 
# async uses CoRoutines which run on the same thread


import logging
import threading
import multiprocessing
import asyncio
import time
import random
logging.basicConfig(format='%(levelname)s - %(asctime)s.%(msecs)03d: %(message)s', datefmt='%H:%M:%S', level=logging.DEBUG)

def display(msg):
    threadname = threading.current_thread().name
    processname = multiprocessing.current_process().name
    logging.info(f'{processname}/{threadname}: {msg}')

# async function
# the sync keyword marks a function for asyncronous operation
async def work(name):
    display(name + ' starting')
    # do something
    await asyncio.sleep(random.randint(1,10))
    display(name + ' finished')

async def run_async(max):
    tasks = []
    for x in range(max):
        name = "Item" + str(x)
        tasks.append(asyncio.ensure_future(work(name)))
    
    await asyncio.gather(*tasks)

def main():
    display('App started')
    
    loop = asyncio.get_event_loop()

    # loop until an async task is done
    loop.run_until_complete(run_async(50))

    # this will never stop untile the application is stopped
    #loop.run_forever()

    # free-up resources
    loop.close()

    display('App finished')


if __name__ == "__main__":
    main()