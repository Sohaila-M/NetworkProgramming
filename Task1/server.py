from socket import *

# Create a TCP/IP socket
s = socket(AF_INET, SOCK_STREAM)

# Define the host and port
host = '127.0.0.1'
port = 40674

# Bind the socket to the address and port
s.bind((host, port))
print("Socket successfully binded to", port)

# Listen for incoming connections
s.listen(5)
print("Socket is listening")
c, addr = s.accept()
print('Got connection from', addr)
# Main server loop
while True:        
        # Receive data from the client
        while True:
            data = c.recv(1024)  # Receive data with a buffer size of 1024
            if not data:
                break  # Break the loop if no more data is received
            print("Received:", data.decode('utf-8'))
        # Send a welcome message to the client
        message = "Thank you for connecting"
        c.sendall(message.encode('utf-8'))

        # Close the connection with the client
c.close()
