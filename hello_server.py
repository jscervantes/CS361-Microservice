#!/usr/bin/env/python3

#
#   Microservice CS 361
#   Binds REP socket to tcp://*:5555
#   Expects b"Hello" from client, replies with b"World"
#

import time, zmq, json
from pybaseball import standings

def main():
    while True:
        # --- Data formatting ---
        return_array = []
        data = standings()
        # Convert list of dataframes to json
        for division in data:
            item = division.to_json(orient="split")
            parsed = json.loads(item)
            return_array.append(parsed)
        return_data = json.dumps(return_array, indent=4)

        if return_data:
          print("data ready")
        else:
          print("no go")

        # --- ZeroMQ messaging ---
        context = zmq.Context()
        socket = context.socket(zmq.REP)
        socket.bind("tcp://*:5000")

        #  Wait for next request from client
        message = socket.recv()
        print(f"Received request: {message}")
    
        #  Do some 'work'
        time.sleep(1)
    
        #  Send reply back to client
        socket.send_string(f"{return_data}")

if __name__ == "__main__":
    main()
