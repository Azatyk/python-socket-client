import socketio
from threading import Timer

sio = socketio.Client()


def close_fridge():
    sio.emit("close_fridge")


@sio.event
def connect():
    print('connection established')


@sio.event
def open_fridge():
    print("fridge opened")
    timer = Timer(5, close_fridge)
    timer.start()


@sio.event
def disconnect():
    print('disconnected from server')


sio.connect("http://localhost:3002")
sio.wait()
