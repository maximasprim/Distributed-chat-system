import socket
import threading
import time

# Client setup
SERVER_HOST = '127.0.0.1'
SERVER_PORT = 12345

def connect_to_server():
    while True:
        try:
            client_socket.connect((SERVER_HOST, SERVER_PORT))
            print("Connected to the server.")
            return
        except:
            print("Connection failed. Retrying in 5 seconds...")
            time.sleep(5)

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connect_to_server()

def receive_messages():
    while True:
        try:
            # Receive message from server
            message = client_socket.recv(1024).decode('utf-8')
            print(message)
        except:
            # Handle server disconnection
            print("Disconnected from server. Reconnecting...")
            connect_to_server()
            break

def send_messages():
    while True:
        message = input()
        try:
            client_socket.send(message.encode('utf-8'))
        except:
            print("Failed to send message. Disconnected from server.")

if __name__ == "__main__":
    # Start a thread to handle receiving messages
    threading.Thread(target=receive_messages).start()
    # Handle sending messages
    send_messages()