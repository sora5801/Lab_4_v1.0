import tkinter as tk
import socket
import sqlite3
from matplotlib import pyplot as plt
import json



class Client:
    def __init__(self,nport):
        self.host = socket.gethostname()  # as both code is running on same pc
        self.port = nport  # socket server port number
        self.client_socket = socket.socket()  # instantiate
        self.client_socket.connect((self.host, self.port))  # connect to the server
        self.year = []
        self.values = []
    def Connect(self, message):

        self.client_socket.send(message.encode())

        # self.client_socket.send(message.encode())  # send message
        data = self.client_socket.recv(1720).decode()  # receive response
        print('Received from server: ' + data)  # show in terminal
        listdata = json.loads(data)
        country = listdata[0][0]
        for i in listdata:
            self.year.append(i[1])
            self.values.append(i[2])

        self.XYplot(self.year, self.values, country)
        self.year = []
        self.values = []

    def XYplot(self, *args):
        plt.title(str(args[2]) + " Year vs Values")
        plt.plot(self.year, self.values)
        plt.show()



if __name__ == '__main__':
    client = Client(5000)
    client.Connect()

