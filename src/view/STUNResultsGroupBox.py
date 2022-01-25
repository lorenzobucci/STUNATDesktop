from PyQt5.QtCore import QCoreApplication
from PyQt5.QtWidgets import QGroupBox, QSizePolicy, QGridLayout, QLabel


class STUNResultsGroupBox(QGroupBox):
    def __init__(self, parent):
        super().__init__(parent)

        self.setObjectName("resultsGroupBox")
        self.setSizePolicy(QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed))
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

    def retranslateUi(self):
        _translate = QCoreApplication.translate
        self.extIPLabel.setText(_translate("STUNATView", "Indirizzo IP\nesterno:"))
        self.natTypeLabel.setText(_translate("STUNATView", "Tipo di NAT:"))
        self.extPortLabel.setText(_translate("STUNATView", "Porta esterna:"))