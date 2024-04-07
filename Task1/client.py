from socket import *

try:
    # Create a socket object
    s = socket(AF_INET, SOCK_STREAM)

    # Define the host and port
    host = "127.0.0.1"
    port = 40674

    # Connect to the server
    s.connect((host, port))
    print("Connected to the server")

    while True:
        # Prompt user for input
        message = input("client: ")

        # Send the message to the server
        s.send(message.encode('utf-8'))

        # Receive data from the server
        while True:
            data = s.recv(2048)
            if not data:
                break
            print("server:", data.decode('utf-8'))

    # Close the connection
    s.close()
