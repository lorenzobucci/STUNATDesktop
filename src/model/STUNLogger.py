import io
import logging

# Logger per la libreria pystun
class STUNLogger:

    def __init__(self):
        """
        Inizializza uno stream per il salvataggio del log avanzato del test STUN
        """
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
