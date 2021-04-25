##############################################
# Multithreading example
##############################################

import logging
import socket
logging.basicConfig(format='%(levelname)s - %(asctime)s: %(message)s', datefmt='%H:%M:%S', level=logging.DEBUG)

# TCP server
# blocking server
def server(ip, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    address = (ip, port)

    logging.info(f'Bind: {ip}:{port}')
    s.bind(address)

    logging.info('Listening')
    s.listen(1) # how many things we want to listen for
    con, addr = s.accept()  # pick up the connection

    logging.info(f'Connected: {addr}')

    while True:
        data = con.recv(1024)
        if len(data) == 0:
            logging.info(f'Exiting')
            con.close()
            break
        logging.info(f'Data: {data}')

    logging.info('Closing the server')
    s.close()


def main():
    logging.info('App Start')
    server('127.0.0.1', 2607)
    
    logging.info('App Finished')

if __name__ == "__main__":
    main()