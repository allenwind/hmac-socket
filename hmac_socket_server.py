import hmac
import os
import hashlib
from socket import socket, AF_INET, SOCK_STREAM

def server_hmac_authenticate(conn, authkey):
    message = os.urandom(64)
    conn.send(message)
    dsg = hmac.digest(authkey, message, hashlib.md5)
    resp = conn.recv(len(dsg))
    return hmac.compare_digest(dsg, resp)

def run_server(address):
    server = socket(AF_INET, SOCK_STREAM)
    server.bind(address)
    server.listen(5)
    while True:
        conn, addr = server.accept()
        if not server_hmac_authenticate(conn, authkey=b"querty"):
            conn.close()
            continue
        print("accept {}...".format(addr))
        print("authenticate is ok...")
        while True:
            msg = conn.recv(8192)
            if not msg:
                break
            conn.sendall(msg)

if __name__ == "__main__":
    run_server(("localhost", 8080))
