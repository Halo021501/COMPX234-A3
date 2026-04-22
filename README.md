COMPX234-A3: Multi-threaded Tuple Space System
Name: CHEN CHUNHAO      ID: 20243006949
This project implements a client/server networked system that manages a "tuple space" using Python and TCP sockets. 
The server is multi-threaded, allowing it to handle multiple client sessions concurrently by spawning a new thread for each connection.
To run this project, open two terminals: 
first, start the server in one terminal with a specified port (e.g., python TupleSpaceServer_help.py 51234) and leave it running. 
Then, in the second terminal at the project root, run for i in {1..10}; do python TupleSpaceClient_help.py localhost 51234 test-workload/client_$i.txt; done using Git Bash 
(or for /L %i in (1, 1, 10) do python TupleSpaceClient_help.py localhost 51234 test-workload\client_%i.txt for Windows CMD) to automatically test all client requests in sequence.
