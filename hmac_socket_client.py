import hashlib
import hmac
import time
import random
from socket import socket, AF_INET, SOCK_STREAM

def client_hmac_authenticate(conn, authkey):
    msg = conn.recv(64)
    dsg = hmac.digest(authkey, msg, hashlib.md5)
    conn.send(dsg)

def run_client(address):
    authkey = b"querty"
    client = socket(AF_INET, SOCK_STREAM)
    client.connect(address)
    client_hmac_authenticate(client, authkey)
    while True:
        client.send(b"hmac")
        resp = client.recv(1024)
        print(resp)
        time.sleep(1)

if __name__ == "__main__":
    run_client(("localhost", 8080))
