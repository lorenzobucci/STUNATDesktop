from PyQt5.QtCore import Qt, QCoreApplication, QRegExp
from PyQt5.QtGui import QFont, QPixmap, QMovie, QRegExpValidator
from PyQt5.QtWidgets import QWidget, QGridLayout, QLabel, QSizePolicy, QGroupBox, QPushButton, QVBoxLayout, QHBoxLayout, \
    QLineEdit, QComboBox, QSpacerItem


class HomeTab(QWidget):
    def __init__(self):
        super().__init__()

        self.homeTabGridLayout = QGridLayout(self)
        self.homeTabGridLayout.setObjectName("homeTabGridLayout")

        self.homeTitleLabel = QLabel(self)
        self.homeTitleLabel.setSizePolicy(QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed))
        self.homeTitleLabel.setText("STUNAT")
        self.homeTitleLabel.setStyleSheet("font-size:22pt; font-weight:600;")
        font = QFont()
        font.setFamily(u"Courier New")
        self.homeTitleLabel.setFont(font)
        self.homeTitleLabel.setAlignment(Qt.AlignHCenter | Qt.AlignTop)
        self.homeTitleLabel.setObjectName("homeTitleLabel")
        self.homeTabGridLayout.addWidget(self.homeTitleLabel, 0, 0, 1, 2)

        self.homeDescriptionLabel = QLabel(self)
        self.homeDescriptionLabel.setSizePolicy(QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed))
        self.homeDescriptionLabel.setStyleSheet("font-size:10pt")
        self.homeDescriptionLabel.setAlignment(Qt.AlignHCenter | Qt.AlignTop)
        self.homeDescriptionLabel.setObjectName("homeDescriptionLabel")
        self.homeTabGridLayout.addWidget(self.homeDescriptionLabel, 1, 0, 1, 2)

        self.resultsGroupBox = QGroupBox(self)
        self.resultsGroupBox.setObjectName("resultsGroupBox")
        self.resultsGroupBox.setSizePolicy(QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed))
        self.resultsGroupBox.setFixedWidth(207)
        self.homeTabGridLayout.addWidget(self.resultsGroupBox, 2, 1, 1, 1)

        self.resultsGroupBoxGridLayout = QGridLayout(self.resultsGroupBox)
        self.resultsGroupBoxGridLayout.setObjectName("resultsGroupBoxGridLayout")

        self.natTypeLabel = QLabel(self.resultsGroupBox)
        self.natTypeLabel.setObjectName("natTypeLabel")
        self.natTypeLabel.setStyleSheet("font-weight:600;")
        self.resultsGroupBoxGridLayout.addWidget(self.natTypeLabel, 0, 0, 1, 1)

        self.extIPLabel = QLabel(self.resultsGroupBox)
        self.extIPLabel.setObjectName("extIPLabel")
        self.resultsGroupBoxGridLayout.addWidget(self.extIPLabel, 1, 0, 1, 1)

        self.extPortLabel = QLabel(self.resultsGroupBox)
        self.extPortLabel.setObjectName("extPortLabel")
        self.resultsGroupBoxGridLayout.addWidget(self.extPortLabel, 2, 0, 1, 1)

        self.natTypeResultLabel = QLabel(self.resultsGroupBox)
        self.natTypeResultLabel.setObjectName("natTypeResultLabel")
        self.resultsGroupBoxGridLayout.addWidget(self.natTypeResultLabel, 0, 1, 1, 1)

        self.extIPResultLabel = QLabel(self.resultsGroupBox)
        self.extIPResultLabel.setObjectName("extIPResultLabel")
        self.resultsGroupBoxGridLayout.addWidget(self.extIPResultLabel, 1, 1, 1, 1)

        self.extPortResultLabel = QLabel(self.resultsGroupBox)
        self.extPortResultLabel.setObjectName("extPortResultLabel")
        self.resultsGroupBoxGridLayout.addWidget(self.extPortResultLabel, 2, 1, 1, 1)

        self.natRepresentation = QLabel(self)
        self.natRepresentation.setSizePolicy(QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred))
        self.natRepresentation.setFixedWidth(225)
        self.natRepresentation.setFixedHeight(100)
        self.natRepresentation.setObjectName("natRepresentation")
        self.homeTabGridLayout.addWidget(self.natRepresentation, 2, 0, 1, 1)

        self.startButton = QPushButton(self)
        self.startButton.setSizePolicy(QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed))
        self.startButton.setObjectName("startButton")
        self.homeTabGridLayout.addWidget(self.startButton, 3, 0, 1, 2, Qt.AlignHCenter)

    def setNatRepresentation(self, imageName):
        imagePath = "res/natRepresentations/" + imageName
        pixmap = QPixmap(imagePath)
        movie = QMovie(imagePath)
        movieSize = pixmap.size()
        movie.setScaledSize(movieSize.scaled(self.natRepresentation.width(), movieSize.height(), Qt.KeepAspectRatio))
        self.natRepresentation.setMovie(movie)
        movie.start()

    def hideResultsGroupBox(self):
        self.resultsGroupBox.hide()
        self.homeTabGridLayout.removeWidget(self.natRepresentation)
        self.homeTabGridLayout.addWidget(self.natRepresentation, 2, 0, 1, 2, Qt.AlignHCenter)

    def showResultsGroupBox(self):
        self.resultsGroupBox.setHidden(False)
        self.homeTabGridLayout.removeWidget(self.natRepresentation)
        self.homeTabGridLayout.addWidget(self.natRepresentation, 2, 0, 1, 1)

    def retranslateUi(self):
        _translate = QCoreApplication.translate
        self.extIPLabel.setText(_translate("STUNATView", "Indirizzo IP\nesterno:"))
        self.natTypeLabel.setText(_translate("STUNATView", "Tipo di NAT:"))
        self.extPortLabel.setText(_translate("STUNATView", "Porta esterna:"))
        self.homeDescriptionLabel.setText(_translate("STUNATView",
                                                     "Scopri il tipo di NAT presente sulla tua rete.\n"
                                                     "Clicca su Inizia test e attendi il risultato."))
        self.startButton.setText(_translate("STUNATView", "Inizia test"))


class OptionsTab(QWidget):
    def __init__(self):
        super().__init__()

        portRegExp = QRegExp("([1-9][0-9]{0,3}|[1-5][0-9]{4}|6[0-4][0-9]{3}|65[0-4][0-9]{2}|655[0-3][0-9]|6553[0-5])")

        self.optionsTabVLayout = QVBoxLayout(self)
        self.optionsTabVLayout.setObjectName("optionsTabVLayout")

        self.stunServerGroupBox = QGroupBox(self)
        self.stunServerGroupBox.setChecked(False)
        self.stunServerGroupBox.setObjectName("stunServerGroupBox")
        self.optionsTabVLayout.addWidget(self.stunServerGroupBox)

        self.stunServerGroupBoxHLayout = QHBoxLayout(self.stunServerGroupBox)
        self.stunServerGroupBoxHLayout.setObjectName("stunServerGroupBoxHLayout")

        self.serverHostnameLabel = QLabel(self.stunServerGroupBox)
        self.serverHostnameLabel.setObjectName("serverHostnameLabel")
        self.stunServerGroupBoxHLayout.addWidget(self.serverHostnameLabel)

        self.serverHostnameField = QLineEdit(self.stunServerGroupBox)
        self.serverHostnameField.setObjectName("serverHostnameField")
        self.stunServerGroupBoxHLayout.addWidget(self.serverHostnameField)

        self.serverPortLabel = QLabel(self.stunServerGroupBox)
        self.serverPortLabel.setObjectName("serverPortLabel")
        self.stunServerGroupBoxHLayout.addWidget(self.serverPortLabel)

        self.serverPortField = QLineEdit(self.stunServerGroupBox)
        self.serverPortField.setFixedWidth(50)
        self.serverPortField.setValidator(QRegExpValidator(portRegExp))
        self.serverPortField.setMaxLength(5)
        self.serverPortField.setObjectName("serverPortField")
        self.stunServerGroupBoxHLayout.addWidget(self.serverPortField)

        self.netParamsGroupBox = QGroupBox(self)
        self.netParamsGroupBox.setObjectName("netParamsGroupBox")
        self.optionsTabVLayout.addWidget(self.netParamsGroupBox)

        self.netParamsGroupBoxHLayout = QHBoxLayout(self.netParamsGroupBox)
        self.netParamsGroupBoxHLayout.setObjectName("netParamsGroupBoxHLayout")

        self.sourceIPLabel = QLabel(self.netParamsGroupBox)
        self.sourceIPLabel.setObjectName("sourceIPLabel")
        self.netParamsGroupBoxHLayout.addWidget(self.sourceIPLabel)

        self.sourceIPComboBox = QComboBox(self.netParamsGroupBox)
        self.sourceIPComboBox.setSizePolicy(QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed))
        self.sourceIPComboBox.setObjectName("sourceIPComboBox")
        self.netParamsGroupBoxHLayout.addWidget(self.sourceIPComboBox)

        self.localPortLabel = QLabel(self.netParamsGroupBox)
        self.localPortLabel.setObjectName("localPortLabel")
        self.netParamsGroupBoxHLayout.addWidget(self.localPortLabel)

        self.localPortField = QLineEdit(self.netParamsGroupBox)
        self.localPortField.setFixedWidth(50)
        self.localPortField.setValidator(QRegExpValidator(portRegExp))
        self.localPortField.setMaxLength(5)
        self.localPortField.setObjectName("localPortField")
        self.netParamsGroupBoxHLayout.addWidget(self.localPortField)

        self.languageHLayout = QHBoxLayout()
        self.languageHLayout.setObjectName(u"languageHLayout")
        self.optionsTabVLayout.addLayout(self.languageHLayout)

        self.languageLabel = QLabel(self)
        self.languageLabel.setObjectName("languageLabel")
        self.optionsTabVLayout.addWidget(self.languageLabel)
        self.languageHLayout.addWidget(self.languageLabel)

        self.languageComboBox = QComboBox(self)
        self.languageComboBox.setSizePolicy(QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed))
        self.languageComboBox.setObjectName("languageComboBox")

        langOptions = ([('Italiano', ''), ('English', 'it-eng')])
        for i, (text, lang) in enumerate(langOptions):
            self.languageComboBox.addItem(text)
            self.languageComboBox.setItemData(i, lang)

        self.languageHLayout.addWidget(self.languageComboBox)

        self.horizontalSpacer = QSpacerItem(100, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.languageHLayout.addItem(self.horizontalSpacer)

    def retranslateUi(self):
        _translate = QCoreApplication.translate
        self.stunServerGroupBox.setTitle(_translate("STUNATView", "Server STUN"))
        self.serverHostnameLabel.setText(_translate("STUNATView", "Hostname o Indirizzo IP"))
        self.serverPortLabel.setText(_translate("STUNATView", "Porta"))
        self.netParamsGroupBox.setTitle(_translate("STUNATView", "Parametri di rete"))
        self.sourceIPLabel.setText(_translate("STUNATView", "Indirizzo IP sorgente"))
        self.localPortLabel.setText(_translate("STUNATView", "Porta locale"))
        self.languageLabel.setText(_translate("STUNATView", "Lingua"))
