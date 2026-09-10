import socket
# Create an IPv4 TCP socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# AF_INET: Specifies the address family as IPv4 (Internet Protocol version 4). 
# SOCK_STREAM: Specifies the socket type as TCP (Transmission Control Protocol)


# Bind to a specific IP and port
HOST = '127.0.0.1'
PORT = 65432

s.bind((HOST, PORT))
print(f"Socket bound to {HOST}:{PORT}")

# Optional: Start listening for connections
s.listen()


while True:
    # conn, addr -> socket, address
    client_socket, client_address = s.accept()
    print(f"Connected by {client_address}")
    
    # Handle client...

    # recv() -> receive data from the client
    data = client_socket.recv(1024)
    # sendall() -> send all data
    client_socket.sendall(data)
    
    client_socket.close()








