from PyQt5.QtCore import Qt, QCoreApplication, QEvent, pyqtSignal
from PyQt5.QtGui import QFont, QCursor, QMouseEvent
from PyQt5.QtWidgets import QGroupBox, QSizePolicy, QGridLayout, QLabel


# Componente dedicato alla visualizzazione testuale dei risultati del test STUN
# È una groupbox di base da cui erediteranno due classi specializzate per la visualizzazione di risultati corretti o erronei
# Codice in larga parte generato automaticamente da QtDesigner su cui è stata eseguita una fattorizzazione
class STUNResultsGroupBox(QGroupBox):
    def __init__(self, parent):
        super().__init__(parent)

        self.setObjectName("resultsGroupBox")
        self.setSizePolicy(QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Minimum))
        self.setFixedWidth(207)

        self.resultsGroupBoxGridLayout = QGridLayout(self)
        self.resultsGroupBoxGridLayout.setObjectName("resultsGroupBoxGridLayout")

        # Link per visualizzare il log avanzato del test
        self.viewLogLabel = QClickableLabel(self)
        self.viewLogLabel.setObjectName("viewLogLabel")
        self.resultsGroupBoxGridLayout.addWidget(self.viewLogLabel, 10, 0, 1, 2)  # Riga 10 = ultima riga

    def retranslateUi(self):
        _translate = QCoreApplication.translate
        self.viewLogLabel.setText(_translate("STUNATView", "Visualizza log avanzato"))


# Groupbox per la visualizzazione di risultati corretti
# Codice in larga parte generato automaticamente da QtDesigner su cui è stata eseguita una fattorizzazione
class STUNCorrectResultsGroupBox(STUNResultsGroupBox):
    def __init__(self, parent):
        super().__init__(parent)

        # ETICHETTE DESCRITTIVE

        self.natTypeLabel = QLabel(self)
        self.natTypeLabel.setObjectName("natTypeLabel")
        self.natTypeLabel.setStyleSheet("font-weight:600;")
        self.resultsGroupBoxGridLayout.addWidget(self.natTypeLabel, 0, 0, 1, 1)

        self.extIPLabel = QLabel(self)
        self.extIPLabel.setObjectName("extIPLabel")
        self.resultsGroupBoxGridLayout.addWidget(self.extIPLabel, 1, 0, 1, 1)

        self.extPortLabel = QLabel(self)
        self.extPortLabel.setObjectName("extPortLabel")
        self.resultsGroupBoxGridLayout.addWidget(self.extPortLabel, 2, 0, 1, 1)

        # ETICHETTE DEI RISULTATI

        self.natTypeResultLabel = QLabel(self)
        self.natTypeResultLabel.setObjectName("natTypeResultLabel")
        self.resultsGroupBoxGridLayout.addWidget(self.natTypeResultLabel, 0, 1, 1, 1)

        self.extIPResultLabel = QLabel(self)
        self.extIPResultLabel.setObjectName("extIPResultLabel")
        self.resultsGroupBoxGridLayout.addWidget(self.extIPResultLabel, 1, 1, 1, 1)

        self.extPortResultLabel = QLabel(self)
        self.extPortResultLabel.setObjectName("extPortResultLabel")
        self.resultsGroupBoxGridLayout.addWidget(self.extPortResultLabel, 2, 1, 1, 1)

    def retranslateUi(self):
        super(STUNCorrectResultsGroupBox, self).retranslateUi()
        _translate = QCoreApplication.translate
        self.extIPLabel.setText(_translate("STUNATView", "Indirizzo IP\nesterno:"))
        self.natTypeLabel.setText(_translate("STUNATView", "Tipo di NAT:"))
        self.extPortLabel.setText(_translate("STUNATView", "Porta esterna:"))


# Groupbox per la visualizzazione di risultati erronei
# Codice in larga parte generato automaticamente da QtDesigner su cui è stata eseguita una fattorizzazione
class STUNErrorResultsGroupBox(STUNResultsGroupBox):
    def __init__(self, parent):
        super().__init__(parent)

        # ETICHETTE DESCRITTIVE

        self.errorLabel = QLabel(self)
        self.errorLabel.setObjectName("errorLabel")
        self.errorLabel.setStyleSheet("font-weight:600;color:#B22222;")
        self.resultsGroupBoxGridLayout.addWidget(self.errorLabel, 0, 0, 1, 1)

        self.errorDescriptionLabel = QLabel(self)
        self.errorDescriptionLabel.setObjectName("errorDescriptionLabel")
        self.errorDescriptionLabel.setAlignment(Qt.AlignTop)
        self.resultsGroupBoxGridLayout.addWidget(self.errorDescriptionLabel, 1, 0, 1, 1)

        # ETICHETTE DEI RISULTATI

        self.errorResultLabel = QLabel(self)
        self.errorResultLabel.setObjectName("errorResultLabel")
        self.errorResultLabel.setWordWrap(True)
        self.resultsGroupBoxGridLayout.addWidget(self.errorResultLabel, 0, 1, 1, 1)

        self.errorDescriptionResultLabel = QLabel(self)
        self.errorDescriptionResultLabel.setObjectName("errorDescriptionResultLabel")
        self.errorDescriptionResultLabel.setWordWrap(True)
        self.resultsGroupBoxGridLayout.addWidget(self.errorDescriptionResultLabel, 1, 1, 1, 1)

    def retranslateUi(self):
        super(STUNErrorResultsGroupBox, self).retranslateUi()
        _translate = QCoreApplication.translate
        self.errorLabel.setText(_translate("STUNATView", "Errore:"))
        self.errorDescriptionLabel.setText(_translate("STUNATView", "Descrizione:"))


# Specializzazione di una QLabel che emula un link cliccabile
class QClickableLabel(QLabel):
    clicked = pyqtSignal()

    def __init__(self, p):
        super().__init__(parent=p)

        self.setStyleSheet("color: #0078d7;")  # Colore caratterizzante i link
        self.setCursor(QCursor(Qt.PointingHandCursor))  # Cursore caratterizzante i link

    # Eliminazione sottolineatura se il cursore esce dall'etichetta
    def leaveEvent(self, a0: QEvent) -> None:
        super(QClickableLabel, self).leaveEvent(a0)
        f = QFont()
        f.setUnderline(False)
        self.setFont(f)

    # Aggiunta sottolineatura se il cursore entra nell'etichetta
    def enterEvent(self, a0: QEvent) -> None:
        super(QClickableLabel, self).enterEvent(a0)
        f = QFont()
        f.setUnderline(True)
        self.setFont(f)

    def mousePressEvent(self, ev: QMouseEvent) -> None:
        super(QClickableLabel, self).mousePressEvent(ev)
        self.clicked.emit()
