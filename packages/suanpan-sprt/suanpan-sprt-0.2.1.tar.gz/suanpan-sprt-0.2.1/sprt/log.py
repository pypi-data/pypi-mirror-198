import sys
import logging


class NodeStreamHandler(logging.StreamHandler):
    def __init__(self, stream=None):
        super().__init__()

    def get_stream(self):
        return sys.stdout

    def set_stream(self, _value):
        ...

    stream = property(get_stream, set_stream)
