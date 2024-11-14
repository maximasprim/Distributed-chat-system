# Distributed-Chat-App

Overview
This is a simple distributed chat application built to demonstrate the principles of distributed computing. The system allows multiple clients to connect to a server, send and receive messages in real-time, and continue communication even if one server node fails.

The application uses TCP sockets for client-server communication and handles basic fault tolerance to ensure that clients can reconnect to a functioning server if one fails.

Features
Real-time messaging between multiple clients.
Message broadcasting from one client to all connected clients.
Basic fault tolerance, including client reconnection to a secondary server upon failure.
Supports multiple server nodes for distributed communication.
System Architecture
The chat application consists of two main components:

Server Node: Manages client connections and broadcasts messages between clients.
Client: Connects to a server to send and receive messages.
Communication is handled using TCP sockets, and threads are used to manage multiple clients and maintain the real-time message flow.

Requirements
Python 3.x
Libraries: Standard Python libraries (socket, threading, time), so no additional installations are required.
Getting Started
1. Setting up the Server
Save the server code in a file called server.py.
Run the server by executing:
bash
Copy code
python server.py
The server will start listening on 127.0.0.1:12345 for incoming connections and display new client connections in the console.
2. Setting up the Client
Save the client code in a file called client.py.

Run the client by executing:

bash
Copy code
python client.py
The client will attempt to connect to the server at 127.0.0.1:12345. If the server is down, it will retry every 5 seconds.

Type a message into the client interface to broadcast it to all connected clients.

3. Running Multiple Clients
You can start multiple instances of the client by running client.py in separate terminal windows to simulate a multi-client environment.

How to Use the Chat Application
Start at least one instance of the server (server.py).
Start one or more instances of the client (client.py).
Each client can type and send messages that will be broadcasted to all other connected clients.
If the server goes down, clients will attempt to reconnect every 5 seconds.
Fault Tolerance
The application includes basic fault tolerance:

Server Failover: If the server is down, clients will keep retrying every 5 seconds until a server is available.
Client Reconnection: If the client disconnects due to network issues or server unavailability, it will attempt to reconnect automatically.
Testing the System
To test the system:

Start one or more server instances.
Connect multiple clients.
Send messages from each client to verify they broadcast correctly.
Simulate a server failure by stopping a server instance, and check that clients reconnect to another available server.
Directory Structure
server.py - Server-side code to handle client connections and message broadcasting.
client.py - Client-side code for connecting, sending, and receiving messages.
Troubleshooting
Connection Failure: If a client cannot connect, check that the server is running and accessible at 127.0.0.1:12345.
Message Not Received: Ensure all clients are connected to the same server and running.
Future Improvements
Enhance fault tolerance by adding a server heartbeat to detect and respond to failures more quickly.
Implement persistent message logging to recover chat history after server restarts.
Develop a GUI for a more user-friendly client experience