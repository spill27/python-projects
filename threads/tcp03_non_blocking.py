# TCP Blocking vs Non-blocking

import logging
import socket
import select
logging.basicConfig(format='%(levelname)s - %(asctime)s: %(message)s', datefmt='%H:%M:%S', level=logging.DEBUG)

# blocking socket
def create_blocking(host, ip):
    logging.info('Blocking creating socket')
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    logging.info('Blocking - connecting')
    s.connect((host, ip))
    logging.info('Blocking - connected')
    logging.info('Blocking - sending ...')

    s.send(b'Hello world\r\n')

    logging.info('Blocking - waiting ...')
    data = s.recv(1024)
    logging.info(f'Blocking data= {len(data)}')
    logging.info('Blocking - closing')

    s.close()

# non-blocking socket
def create_non_blocking(host, port):
    logging.info('NonBlocking creating socket')
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    logging.info('NonBlocking - connecting')
    ret = s.connect_ex((host, port)) #BLOCK

    if ret != 0:
        logging.info('NonBlocking - Failed to connect')    
        return

    logging.info('NonBlocking - connected')
    s.setblocking(False)

    inputs = [s]
    outputs = [s]
    while inputs:
        logging.info('NonBlocking - waiting ...')
        readable, writable, exceptional = select.select(inputs, outputs, inputs, 0.5)

        for s in writable:
            logging.info('NonBlocking - sending ...')
            data = s.send(b'Hello World\r\n')
            logging.info(f'NonBlocking - sent: {data}')
            outputs.remove(s)
        
        for s in readable:
            logging.info('NonBlocking - reading ...')
            data = s.recv(1024)
            logging.info(f'NonBlocking - read: {len(data)}')
            logging.info(f'NonBlocking - closing ...')
            inputs.remove(s)
            break
        
        for s in exceptional:
            logging.info(f'NonBlocking - error')
            inputs.remove(s)
            outputs.remove(s)
            break


def main():
    logging.info('App Start')
    # create_blocking("voidrealms.com", 80)
    create_non_blocking("voidrealms.com", 80)
    
    logging.info('App Finished')

if __name__ == "__main__":
    main()