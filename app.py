from flask import Flask, render_template
from flask_socketio import SocketIO

import settings
from constants import WebSocketNamespacePath, AppRoutes
from namespaces.index import IndexNamespace
from tasks import send_connected_message

app = Flask(__name__)
app.config["SECRET_KEY"] = settings.SECRET_KEY
socketio = SocketIO(app, async_mode="eventlet")

socketio.start_background_task(send_connected_message, socketio=socketio)
socketio.on_namespace(IndexNamespace(WebSocketNamespacePath.INDEX))


@app.route(AppRoutes.ROOT)
def index():
    """Endpoint to render index page."""
    return render_template("index.html")


if __name__ == "__main__":
    """Start the server."""
    socketio.run(app)
