# ASYNCIO code to simulate the TetrAMM (server)


import logging
import threading
from threading import Thread
import socket
import multiprocessing
import asyncio
import time
import random
from queue import Queue

logging.basicConfig(format='%(levelname)s - %(asctime)s.%(msecs)03d: %(message)s', datefmt='%H:%M:%S', level=logging.DEBUG)
TETRAMMS = 3
acq = [False for i in range(TETRAMMS)]

# SERVERS #########################################################################
# TetrAMMs
async def tetramm(ip, port, idx):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    address = (ip, port)

    logging.info(f'Bind: {ip}:{port}')
    s.bind(address)


    logging.info('Listening')
    s.listen(1) # how many things we want to listen for
    s.setblocking(False)

    loop = asyncio.get_event_loop()

    con, addr = await loop.sock_accept(s)  # pick up the connection

    logging.info(f'Connected: {addr}')
    logging.info(f'Thread name = {threading.current_thread().name}')

    while True:
        global acq
        data = await loop.sock_recv(con, 1024)
        if len(data) == 0:
            logging.info(f'Exiting')
            con.close()
            break
        elif (data == b'start\r\n'):
            logging.info(f'Start Received: start sending data')
            acq[idx] = True
            # start sending data
        elif (data == b'stop\r\n'):
            logging.info(f'Stop Received: stopping data')
            acq[idx] = False
            # stop sending data
            logging.info(f'Exiting')
            con.close()
            break
        logging.info(f'Data: {data}')

    logging.info(f'Closing the server {threading.current_thread().name}')
    s.close()



def main():
    logging.info('App started')
    
    loop = asyncio.get_event_loop()
    # loop until an async task is done
    x = 0
    ips = ['127.0.0.'+ str(i+10) for i in range(TETRAMMS)]
    loop.run_until_complete(tetramm(ips[x], 10001, x))
    loop.run_forever()
    # # free-up resources
    loop.close()

    # ips = ['127.0.0.'+ str(i+10) for i in range(TETRAMMS)]
    # threads = []
    # for x in range(TETRAMMS):
    #     # start tetramm servers
    #     t = Thread(target=tetramm, args=[ips[x], 10001, x], daemon=True) # this thread stops when the applications stops
    #     threads.append(t)
    #     t.start()

    # for x in range(TETRAMMS):
    #     threads[x].join()

    logging.info('App finished')


if __name__ == "__main__":
    main()