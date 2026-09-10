import socket

HOST = '127.0.0.1'
PORT = 65432

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect((HOST, PORT))

message = "Hello, server!"

client.sendall(message.encode('utf-8'))

response = client.recv(4096)
print(f"Server response: {response.decode('utf-8')}")
client.close()