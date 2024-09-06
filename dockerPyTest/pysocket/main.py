import time
import socket
from sklearn.datasets import load_iris 

data = load_iris()

# Create a TCP server socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("0.0.0.0", 9999))
server.listen()

while True:
    # Accept a client connection
    client, addr = server.accept()
    print("Connection from", addr)
    client.send("You are connected\n".encode())
     # Send the first column of features from the Iris dataset
    client.send(f"{data['data'][:, 0]}\n".encode())
    time.sleep(2)
    client.send("You are being disconected\n".encode())
    client.close()