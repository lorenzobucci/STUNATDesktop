import io
import logging


class STUNLogger:
    def __init__(self):
        self.stream = io.StringIO()
        log = logging.getLogger("pystun3")
        log.setLevel(logging.DEBUG)

        handler = logging.StreamHandler(self.stream)
        handler.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s - %(message)s')
        handler.setFormatter(formatter)
        log.addHandler(handler)

    def getLog(self):
        return self.stream.getvalue()

    def resetLog(self):
        self.stream.truncate(0)
