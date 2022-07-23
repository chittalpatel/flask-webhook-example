from flask_socketio import SocketIO

from constants import WebSocketResponseEvent, WebSocketNamespacePath


def send_connected_message(socketio: SocketIO):
    """Send `Connected` message to all connected clients every 60 seconds."""
    while True:
        socketio.sleep(60)
        socketio.emit(
            WebSocketResponseEvent.MY_RESPONSE,
            {"data": "Connected"},
            namespace=WebSocketNamespacePath.INDEX,
        )
