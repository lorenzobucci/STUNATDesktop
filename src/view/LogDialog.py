from PyQt5.QtCore import QCoreApplication, Qt
from PyQt5.QtWidgets import QDialog, QGridLayout, QTextEdit, QDialogButtonBox


# Dialogo per visualizzare il log avanzato del test STUN
# Codice in larga parte generato automaticamente da QtDesigner
class LogDialog(QDialog):

    def __init__(self, rawLog: str):
        """
        Inizializzazione e creazione dialogo.
        :param rawLog: Stringa contenente il log da visualizzare
        """
        # Settaggio pulsanti finestra
        super().__init__(
            flags=Qt.WindowTitleHint | Qt.WindowSystemMenuHint | Qt.WindowCloseButtonHint | Qt.WindowMaximizeButtonHint)

        self.setObjectName("LogDialog")
        self.resize(400, 300)

        self.gridLayout = QGridLayout(self)
        self.gridLayout.setObjectName("gridLayout")

        self.logContainer = QTextEdit(self)
        self.logContainer.setObjectName("logContainer")
        self.logContainer.setText(rawLog)
        self.logContainer.setReadOnly(True)
        self.logContainer.setLineWrapMode(QTextEdit.NoWrap)  # Testo non a capo automaticamente

        self.gridLayout.addWidget(self.logContainer, 0, 1, 1, 1)

        self.buttonBox = QDialogButtonBox(self)
        self.buttonBox.setObjectName("buttonBox")
        self.buttonBox.setCenterButtons(True)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Close)
        self.buttonBox.button(QDialogButtonBox.Close).clicked.connect(self.accept)

        self.gridLayout.addWidget(self.buttonBox, 1, 1, 1, 1)

        self.retranslateUi()

    def retranslateUi(self):
        _translate = QCoreApplication.translate
        self.setWindowTitle(_translate("LogDialog", "Log avanzato"))
        self.buttonBox.button(QDialogButtonBox.Close).setText(_translate("LogDialog", "Chiudi"))
