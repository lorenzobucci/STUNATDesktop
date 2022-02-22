import threading

from PyQt5.QtCore import QObject, pyqtSignal

from model.Model import Model
from view.LogDialog import LogDialog
from view.STUNATView import STUNATView


class Controller:

    def __init__(self, stuNatView: STUNATView, model: Model):
        self.view = stuNatView
        self.model = model

        self.view.homeTab.startButton.clicked.connect(self._startButtonHandler)
        self.view.homeTab.resultsGroupBox.viewLogLabel.clicked.connect(self._viewLogHandler)

        self.view.homeTab.setNatRepresentation("UnknownNAT.png")
        self.view.homeTab.hideResultsGroupBox()

        self.view.optionsTab.serverHostnameField.setText("stun.sipgate.net")
        self.view.optionsTab.serverPortField.setText("3478")
        self.view.optionsTab.sourceIPComboBox.insertItems(0, self.model.localIPList)
        self.view.optionsTab.sourceIPComboBox.setCurrentIndex(0)
        self.view.optionsTab.localPortField.setText(str(self.model.localPort))

    def _startButtonHandler(self):
        self.view.homeTab.startButton.setDisabled(True)
        self.view.setBusyCursor()
        self.view.homeTab.setNatRepresentation("Loading.gif")
        self.view.homeTab.homeDescriptionLabel.hide()
        self.view.homeTab.resultsGroupBox.setDisabled(True)

        worker = STUNWorker()
        worker.finished.connect(self._processWorkerResults)
        worker.stunException.connect(lambda: {
            self.view.homeTab.hideResultsGroupBox(),
            self.view.homeTab.setNatRepresentation("UnknownNAT.png"),
            self.view.homeTab.startButton.setEnabled(True),
            self.view.unsetCursor(),
            self.view.showErrorMessage(str(worker.lastException))
        })
        threading.Thread(target=worker.startTest, args=(self.view, self.model)).start()

    def _processWorkerResults(self):
        self.view.homeTab.resultsGroupBox.setEnabled(True)
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

    def _viewLogHandler(self):
        logDialog = LogDialog(self.model.rawLog)
        logDialog.exec()


class STUNWorker(QObject):
    finished = pyqtSignal()
    stunException = pyqtSignal()

    lastException = None

    def startTest(self, view, model):
        try:
            model.startTest(view.optionsTab.serverHostnameField.text(), view.optionsTab.serverPortField.text(),
                            view.optionsTab.sourceIPComboBox.currentText(), view.optionsTab.localPortField.text())
            self.finished.emit()
        except Exception as e:
            self.lastException = e
            self.stunException.emit()
