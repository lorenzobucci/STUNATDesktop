import random
import threading

from PyQt5.QtCore import QObject, pyqtSignal

from model.Model import Model
from view.STUNATView import STUNATView


class Controller:

    def __init__(self, stuNatView: STUNATView, model: Model):
        self.view = stuNatView
        self.model = model

        self.view.homeTab.startButton.clicked.connect(self._startButtonHandler)

        self.view.homeTab.setNatRepresentation("UnknownNAT.png")
        self.view.homeTab.hideResultsGroupBox()

        self.view.optionsTab.serverHostnameField.setText("stun.sipgate.net")
        self.view.optionsTab.serverPortField.setText("3478")
        self.view.optionsTab.sourceIPComboBox.insertItems(0, self.model.localIPList)
        self.view.optionsTab.sourceIPComboBox.setCurrentIndex(0)
        self.view.optionsTab.localPortField.setText(str(random.randint(10000, 65000)))

        self.view.optionsTab.languageComboBox.setCurrentText(self.model.currentOSLanguage)

    def _startButtonHandler(self):
        self.view.homeTab.startButton.setDisabled(True)
        self.view.setBusyCursor()
        self.view.homeTab.setNatRepresentation("Loading.gif")
        self.view.homeTab.homeDescriptionLabel.hide()

        worker = STUNWorker()
        threading.Thread(target=worker.startTest, args=(self.view, self.model)).start()
        worker.finished.connect(self._processWorkerResults)
        worker.stunException.connect(lambda: {
            self.view.homeTab.setNatRepresentation("UnknownNAT.png"),
            self.view.homeTab.startButton.setEnabled(True),
            self.view.unsetCursor(),
            self.view.showErrorMessage(worker.exceptionMessage)
        })

    def _processWorkerResults(self):
        self.view.homeTab.setNatRepresentation(self.model.testResults["natRepresentationImage"])
        if self.model.testResults["isAnError"]:
            self.view.homeTab.resultsGroupBox.displayErrorResult()
            self.view.homeTab.resultsGroupBox.errorResultLabel.setText(self.model.testResults["errorName"])
            self.view.homeTab.resultsGroupBox.errorDescriptionResultLabel.setText(
                self.model.testResults["errorDescription"])
        else:
            self.view.homeTab.resultsGroupBox.displayCorrectResult()
            self.view.homeTab.resultsGroupBox.natTypeResultLabel.setText(self.model.testResults["natType"])
            self.view.homeTab.resultsGroupBox.extIPResultLabel.setText(self.model.testResults["extIP"])
            self.view.homeTab.resultsGroupBox.extPortResultLabel.setText(str(self.model.testResults["extPort"]))
        self.view.homeTab.showResultsGroupBox()
        self.view.homeTab.startButton.setEnabled(True)
        self.view.unsetCursor()


class STUNWorker(QObject):
    finished = pyqtSignal()
    stunException = pyqtSignal()

    exceptionMessage = ""

    def startTest(self, view, model):
        try:
            model.startTest(view.optionsTab.serverHostnameField.text(), view.optionsTab.serverPortField.text(),
                            view.optionsTab.sourceIPComboBox.currentText(), view.optionsTab.localPortField.text())
            self.finished.emit()
        except Exception as e:
            self.exceptionMessage = str(e)
            self.stunException.emit()
