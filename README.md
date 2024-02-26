# Daily MLB Standings 

This microservice provides the daily MLB standings in JSON string format. This uses sockets and ZeroMQ with a classic request-reply set upt to communicate.

## How to Request Data

After creating a ZeroMQ context:

`context = zmq.Context()`

create a socket with a ZeroMQ request:

`socket = context.socket(zmq.REQ)`.

Finally, connect this socket to `localhost:8888`:

`socket.connect("tcp://localhost:8888")`


## How to Receive Data

Create a message variable to hold the response, using `.recv_json()` ZMQ method:

`message = socket.recv_json()`

Congrats, you now have the daily standings in JSON format stored in `message`!


## UML Diagram
![UML diagram showing request-response pattern](https://github.com/jscervantes/CS351-Microservice/image.jpg?raw=true)
