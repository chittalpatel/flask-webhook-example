from enum import Enum


class WebSocketResponseEvent(str, Enum):
    MY_RESPONSE = "my_response"


class WebSocketNamespacePath(str, Enum):
    INDEX = "/"


class AppRoutes(str, Enum):
    ROOT = "/"
