from datetime import datetime
from typing import Dict

from flask import request
from flask_socketio import Namespace, emit, disconnect
from humanize import precisedelta

# To store and manage active clients.
from constants import WebSocketResponseEvent

clients: Dict[str, datetime] = dict()


class IndexNamespace(Namespace):
    def on_get_timestamp(self):
        """Get current server timestamp in UTC timezone."""
        emit(
            WebSocketResponseEvent.MY_RESPONSE,
            {"data": f"Server timestamp (UTC): {str(datetime.utcnow())}"},
        )

    def on_get_clients_count(self):
        """Get the total number of clients connected to the server."""
        global clients
        emit(
            WebSocketResponseEvent.MY_RESPONSE,
            {"data": f"Connected clients: {len(clients)}"},
        )

    def on_get_time_elapsed(self):
        """Get the time elapsed since the client connection."""
        global clients
        elapsed_time = precisedelta(datetime.utcnow() - clients[request.sid])
        emit(
            WebSocketResponseEvent.MY_RESPONSE,
            {"data": f"Time elapsed: {elapsed_time}"},
        )

    def on_disconnect_request(self):
        """Disconnect client event."""
        emit(WebSocketResponseEvent.MY_RESPONSE, {"data": "Client disconnected"})
        disconnect()

    def on_connect(self):
        """Event to handle new client connections. Add new client to clients and
        start a background task to send server event to all clients."""
        global clients
        clients[request.sid] = datetime.utcnow()
        emit(
            WebSocketResponseEvent.MY_RESPONSE,
            {"data": "Client connection established."},
        )

    def on_disconnect(self):
        """Event to handle client disconnects. Remove the client from clients storage"""
        global clients
        clients.pop(request.sid)
