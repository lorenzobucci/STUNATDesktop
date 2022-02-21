from PyQt5.QtCore import Qt, QCoreApplication, QEvent, pyqtSignal
from PyQt5.QtGui import QFont, QCursor, QMouseEvent
from PyQt5.QtWidgets import QGroupBox, QSizePolicy, QGridLayout, QLabel


class STUNResultsGroupBox(QGroupBox):
    def __init__(self, parent):
        super().__init__(parent)

        self.setObjectName("resultsGroupBox")
        self.setSizePolicy(QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Minimum))
        self.setFixedWidth(207)

        self.resultsGroupBoxGridLayout = QGridLayout(self)
        self.resultsGroupBoxGridLayout.setObjectName("resultsGroupBoxGridLayout")

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

        self.natTypeResultLabel = QLabel(self)
        self.natTypeResultLabel.setObjectName("natTypeResultLabel")
        self.resultsGroupBoxGridLayout.addWidget(self.natTypeResultLabel, 0, 1, 1, 1)

        self.extIPResultLabel = QLabel(self)
        self.extIPResultLabel.setObjectName("extIPResultLabel")
        self.resultsGroupBoxGridLayout.addWidget(self.extIPResultLabel, 1, 1, 1, 1)

        self.extPortResultLabel = QLabel(self)
        self.extPortResultLabel.setObjectName("extPortResultLabel")
        self.resultsGroupBoxGridLayout.addWidget(self.extPortResultLabel, 2, 1, 1, 1)

        self.errorLabel = QLabel(self)
        self.errorLabel.setObjectName("errorLabel")
        self.errorLabel.setStyleSheet("font-weight:600;color:#B22222;")
        self.resultsGroupBoxGridLayout.addWidget(self.errorLabel, 3, 0, 1, 1)
        self.errorLabel.hide()

        self.errorDescriptionLabel = QLabel(self)
        self.errorDescriptionLabel.setObjectName("errorDescriptionLabel")
        self.errorDescriptionLabel.setAlignment(Qt.AlignTop)
        self.resultsGroupBoxGridLayout.addWidget(self.errorDescriptionLabel, 4, 0, 1, 1)
        self.errorDescriptionLabel.hide()

        self.errorResultLabel = QLabel(self)
        self.errorResultLabel.setObjectName("errorResultLabel")
        self.errorResultLabel.setWordWrap(True)
        self.resultsGroupBoxGridLayout.addWidget(self.errorResultLabel, 3, 1, 1, 1)
        self.errorResultLabel.hide()

        self.errorDescriptionResultLabel = QLabel(self)
        self.errorDescriptionResultLabel.setObjectName("errorDescriptionResultLabel")
        self.errorDescriptionResultLabel.setWordWrap(True)
        self.resultsGroupBoxGridLayout.addWidget(self.errorDescriptionResultLabel, 4, 1, 1, 1)
        self.errorDescriptionResultLabel.hide()

        self.viewLogLabel = QClickableLabel(self)
        self.viewLogLabel.setObjectName("viewLogLabel")
        self.resultsGroupBoxGridLayout.addWidget(self.viewLogLabel, 5, 0, 1, 2)

    def displayErrorResult(self):
        self.natTypeLabel.hide()
        self.extIPLabel.hide()
        self.extPortLabel.hide()
        self.natTypeResultLabel.hide()
        self.extIPResultLabel.hide()
        self.extPortResultLabel.hide()

        self.errorLabel.show()
        self.errorDescriptionLabel.show()
        self.errorResultLabel.show()
        self.errorDescriptionResultLabel.show()

    def displayCorrectResult(self):
        self.natTypeLabel.show()
        self.extIPLabel.show()
        self.extPortLabel.show()
        self.natTypeResultLabel.show()
        self.extIPResultLabel.show()
        self.extPortResultLabel.show()

        self.errorLabel.hide()
        self.errorDescriptionLabel.hide()
        self.errorResultLabel.hide()
        self.errorDescriptionResultLabel.hide()

    def retranslateUi(self):
        _translate = QCoreApplication.translate
        self.extIPLabel.setText(_translate("STUNATView", "Indirizzo IP\nesterno:"))
        self.natTypeLabel.setText(_translate("STUNATView", "Tipo di NAT:"))
        self.extPortLabel.setText(_translate("STUNATView", "Porta esterna:"))
        self.errorLabel.setText(_translate("STUNATView", "Errore:"))
        self.errorDescriptionLabel.setText(_translate("STUNATView", "Descrizione:"))
        self.viewLogLabel.setText(_translate("STUNATView", "Visualizza log avanzato"))


class QClickableLabel(QLabel):
    clicked = pyqtSignal()

    def __init__(self, p):
        super().__init__(parent=p)

        self.setStyleSheet("color: #0078d7;")
        self.setCursor(QCursor(Qt.PointingHandCursor))

    def leaveEvent(self, a0: QEvent) -> None:
        super(QClickableLabel, self).leaveEvent(a0)
        f = QFont()
        f.setUnderline(False)
        self.setFont(f)

    def enterEvent(self, a0: QEvent) -> None:
        super(QClickableLabel, self).enterEvent(a0)
        f = QFont()
        f.setUnderline(True)
        self.setFont(f)

    def mousePressEvent(self, ev: QMouseEvent) -> None:
        super(QClickableLabel, self).mousePressEvent(ev)
        self.clicked.emit()
