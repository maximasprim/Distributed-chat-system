import socket
import threading

# Server setup
SERVER_HOST = '127.0.0.1'
SERVER_PORT = 12345

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((SERVER_HOST, SERVER_PORT))
server_socket.listen()

clients = []  # List to keep track of connected clients

def broadcast(message, sender_socket=None):
    # Send the message to all clients except the sender
    for client in clients:
        if client != sender_socket:
            try:
                client.send(message)
            except:
                # Handle client disconnection
                clients.remove(client)

def handle_client(client_socket):
    while True:
        try:
            # Receive message from client
            message = client_socket.recv(1024)
            broadcast(message, client_socket)
        except:
            # Handle client disconnection
            clients.remove(client_socket)
            client_socket.close()
            break

def start_server():
    print(f"Server is running on {SERVER_HOST}:{SERVER_PORT}")
    while True:
        # Accept new client connection
        client_socket, client_address = server_socket.accept()
        print(f"New connection from {client_address}")
        clients.append(client_socket)
        # Start a new thread for handling the client
        threading.Thread(target=handle_client, args=(client_socket,)).start()

if __name__ == "__main__":
    start_server()