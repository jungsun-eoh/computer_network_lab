# file: server.py
# handles client connections
# Please do not modify this file in this lab. You will create a customized server in lab 3.

import socket
import pickle

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 12000       # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print("Listening at " + HOST + "/" + str(PORT))
    conn, addr = s.accept() # accepts new clients
    with conn: # for each client that connects
        client_id = addr[1]
        serialized_data = pickle.dumps(client_id) # creates a stream of bytes
        conn.send(serialized_data)
        while True:
            raw_data = conn.recv(1024) # receives data from this client
            if not raw_data:
                break
            data = pickle.loads(raw_data) # deserializes the data from the client
            student_name = data['student_name']
            github_username = data['github_username']
            sid = data['sid']
            log = "Connected: Student: " + student_name + ", Github Username: " + github_username + ", sid: " + str(sid)
            print(log)

