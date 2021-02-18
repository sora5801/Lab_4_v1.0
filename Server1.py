from SQLdatabase import SQLdatabase
import socket
import json


def utf8len(s):
    return len(s.encode('utf-8'))


class Server:
    def __init__(self, port):
        self.SQ = SQLdatabase()
        self.SQ.UNTable()
        self.SQ.insertUNData()
        self.host = socket.gethostname()
        self.port = port  # initiate port no above 1024
        self.server_socket = socket.socket()  # get instance
        self.server_socket.bind((self.host, self.port))  # bind host address and port together

    def Connect(self, nports):
        # configure how many client the server can listen simultaneously
        self.server_socket.listen(nports)
        conn, address = self.server_socket.accept()  # accept new connection
        print("Connection from: " + str(address))
        while True:
            # receive data stream. it won't accept data packet greater than 1720 bytes
            data = conn.recv(1720).decode()
            if not data:
                # if data is not received break
                break
            print("from connected user: " + str(data))
            data2 = self.SQ.Fetch(str(data))
            print(data2)
            conn.send((json.dumps(data2)).encode())  # send data to the client

        conn.close()  # close the connection


if __name__ == '__main__':
    server = Server(5000)
    server.Connect(2)
