import zmq

context = zmq.Context()

#  Socket to talk to server
print("Connecting to hello world server…")
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:1178")

socket.send_json({"name":"Reza Noori","age":21})
message = socket.recv()
print( message)