import threading

from model.Model import Model
from view.STUNATView import STUNATView


class Controller:
    def __init__(self, stuNatView: STUNATView, model: Model):
        self.view = stuNatView
        self.model = model
        startButtonHandlerThread = threading.Thread(target=self._startButtonHandler)

        self.view.startButton.clicked.connect(
            lambda: {
                self.view.setNatRepresentation("Loading.gif"),
                startButtonHandlerThread.start()
            }
        )
        self.view.sourceIPComboBox.insertItems(0, self.model.localIPList)
        self.view.sourceIPComboBox.setCurrentIndex(0)

        self.view.serverHostnameField.setText("stun.sipgate.net")
        self.view.serverPortField.setText("3478")
        self.view.localPortField.setText(str(random.randint(10000, 65000)))

    def _startButtonHandler(self):
        self.model.startTest(self.view.serverHostnameField.text(), self.view.serverPortField.text(),
                             self.view.sourceIPComboBox.currentText(), self.view.localPortField.text())
        self.view.setNatRepresentation(self.model.testResults["natRepresentationImage"])
        self.view.natTypeResultLabel.setText(self.model.testResults["natType"])
        self.view.extIPResultLabel.setText(self.model.testResults["extIP"])
        self.view.extPortResultLabel.setText(str(self.model.testResults["extPort"]))
