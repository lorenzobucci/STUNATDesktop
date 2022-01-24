import random
import threading

from PyQt5.QtCore import QObject, pyqtSignal

from model.Model import Model
from view.STUNATView import STUNATView


class Controller:

    def __init__(self, stuNatView: STUNATView, model: Model):
        self.view = stuNatView
        self.model = model

        self.view.startButton.clicked.connect(self._startButtonHandler)

        self.view.sourceIPComboBox.insertItems(0, self.model.localIPList)
        self.view.sourceIPComboBox.setCurrentIndex(0)

        self.view.setNatRepresentation("UnknownNAT.png")
        self.view.serverHostnameField.setText("stun.sipgate.net")
        self.view.serverPortField.setText("3478")
        self.view.localPortField.setText(str(random.randint(10000, 65000)))

    def _startButtonHandler(self):
        self.view.startButton.setDisabled(True)
        self.view.setBusyCursor()
        self.view.setNatRepresentation("Loading.gif")

        worker = STUNWorker()
        threading.Thread(target=worker.startTest, args=(self.view, self.model)).start()
        worker.finished.connect(lambda: {
            self.view.setNatRepresentation(self.model.testResults["natRepresentationImage"]),
            self.view.natTypeResultLabel.setText(self.model.testResults["natType"]),
            self.view.extIPResultLabel.setText(self.model.testResults["extIP"]),
            self.view.extPortResultLabel.setText(str(self.model.testResults["extPort"])),
            self.view.startButton.setEnabled(True),
            self.view.unsetCursor()
        })


class STUNWorker(QObject):
    finished = pyqtSignal()

    def startTest(self, view, model):
        model.startTest(view.serverHostnameField.text(), view.serverPortField.text(),
                        view.sourceIPComboBox.currentText(), view.localPortField.text())
        self.finished.emit()
