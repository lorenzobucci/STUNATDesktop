import threading

from PyQt5.QtCore import QObject, pyqtSignal

from model.Model import Model
from view.LogDialog import LogDialog
from view.STUNATView import STUNATView
from view.components.STUNResultsGroupBox import *


class Controller:

    def __init__(self, stuNatView: STUNATView, model: Model):
        """
        Inizializza il Controller connettendo gli eventi della view ai loro handler e impostando i parametri
        predefiniti dell'applicazione.
        """
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
        """
        Prepara la view all'esecuzione del test, crea un oggetto STUNWorker che eseguirà il test su un thread
        separato e gestisce eventuali eccezioni lanciate durante il test.
        """
        self.view.homeTab.startButton.setDisabled(True)
        self.view.setBusyCursor()
        self.view.homeTab.setNatRepresentation("Loading.gif")
        self.view.homeTab.homeDescriptionLabel.hide()
        self.view.homeTab.resultsGroupBox.setDisabled(True)

        worker = STUNWorker()
        worker.finished.connect(self._processWorkerResults)  # Si processano i risultati appena il test si è concluso
        worker.stunException.connect(lambda: {  # In caso di eccezione durante il test si ripristina lo stato originale della view
            self.view.homeTab.hideResultsGroupBox(),
            self.view.homeTab.setNatRepresentation("UnknownNAT.png"),
            self.view.homeTab.startButton.setEnabled(True),
            self.view.unsetCursor(),
            self.view.showErrorMessage(str(worker.lastException))  # Si mostra sulla view il messaggio contenuto nell'eccezione
        })
        threading.Thread(target=worker.startTest, args=(self.view, self.model)).start()

    def _processWorkerResults(self):
        """
        Visualizza sulla view i risultati del test.
        """
        self.view.homeTab.resultsGroupBox.setEnabled(True)
        self.view.homeTab.setNatRepresentation(self.model.testResults["natRepresentationImage"])
        if self.model.testResults["isAnError"]:  # In caso di test fallito
            # Creazione di una groupbox per la visualizzazione dei risultati corretti
            self.view.homeTab.resultsGroupBox.viewLogLabel.clicked.disconnect()
            self.view.homeTab.replaceResultsGroupBox(STUNErrorResultsGroupBox(self.view.homeTab))
            self.view.homeTab.resultsGroupBox.viewLogLabel.clicked.connect(self._viewLogHandler)
            self.view.homeTab.resultsGroupBox.errorResultLabel.setText(self.model.testResults["errorName"])
            self.view.homeTab.resultsGroupBox.errorDescriptionResultLabel.setText(
                self.model.testResults["errorDescription"])
        else:  # In caso di test riuscito
            # Creazione di una groupbox per la visualizzazione dei risultati corretti
            self.view.homeTab.resultsGroupBox.viewLogLabel.clicked.disconnect()
            self.view.homeTab.replaceResultsGroupBox(STUNCorrectResultsGroupBox(self.view.homeTab))
            self.view.homeTab.resultsGroupBox.viewLogLabel.clicked.connect(self._viewLogHandler)
            self.view.homeTab.resultsGroupBox.natTypeResultLabel.setText(self.model.testResults["natType"])
            self.view.homeTab.resultsGroupBox.extIPResultLabel.setText(self.model.testResults["extIP"])
            self.view.homeTab.resultsGroupBox.extPortResultLabel.setText(str(self.model.testResults["extPort"]))
        self.view.homeTab.showResultsGroupBox()
        self.view.homeTab.startButton.setEnabled(True)
        self.view.unsetCursor()

    def _viewLogHandler(self):
        """
        Apre la finestra che visualizza il log avanzato.
        """
        logDialog = LogDialog(self.model.rawLog)
        logDialog.exec()


# Gestisce l'esecuzione del test
class STUNWorker(QObject):
    finished = pyqtSignal()
    stunException = pyqtSignal()

    lastException = None

    def startTest(self, view, model):
        """
        Lancia il test e ne notifica la fine oppure il lancio di un'eccezione.
        In quest'ultimo caso salva l'eccezione per poter essere letta dal Controller.
        """
        try:
            model.startTest(view.optionsTab.serverHostnameField.text(), view.optionsTab.serverPortField.text(),
                            view.optionsTab.sourceIPComboBox.currentText(), view.optionsTab.localPortField.text())
            self.finished.emit()
        except Exception as e:
            self.lastException = e
            self.stunException.emit()
