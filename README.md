## About
TCP and UDP socket programming in a client-server environment using python.
Refer to the Assignment specification file (pdf).
## How to run:  
1. Run the server first:  
    > python3 server.py <req_code>  

2. The server will print out the port number for its socket.  

3. Run the client second:  
    python3 client.py <server address> <n_port> <req_code> <message>  

    ->  <server address> is the ip address of the server  
    ->  <n_port> is obtained from step 2.  
    ->  <message> is the message that will be reversed by the server  

4. The client will print the message in reversed order and print to stdout.  



The program was tested on linux.student.cs.uwaterloo.ca server by sshing into two differnt
servers.  
