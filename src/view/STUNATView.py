from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QRegExpValidator


class STUNATView(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.setObjectName("STUNATView")
        self.setWindowTitle("STUNAT Desktop")

        self.setFixedSize(QtCore.QSize(480, 300))

        self.centralWidget = QtWidgets.QWidget(self)
        self.centralWidget.setObjectName("centralWidget")

        self.tabWidget = QtWidgets.QTabWidget(self.centralWidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 462, 282))
        self.tabWidget.setObjectName("tabWidget")

        self.homeTab = QtWidgets.QWidget()
        self.homeTab.setObjectName("homeTab")
        self.tabWidget.addTab(self.homeTab, "STUNAT")

        self.homeTabGridLayout = QtWidgets.QGridLayout(self.homeTab)
        self.homeTabGridLayout.setObjectName("homeTabGridLayout")

        self.homeTitleLabel = QtWidgets.QLabel(self.homeTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        self.homeTitleLabel.setSizePolicy(sizePolicy)
        self.homeTitleLabel.setText("STUNAT")
        self.homeTitleLabel.setStyleSheet("font-size:18pt; font-weight:600;")
        self.homeTitleLabel.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)
        self.homeTitleLabel.setObjectName("homeTitleLabel")
        self.homeTabGridLayout.addWidget(self.homeTitleLabel, 0, 0, 1, 2)

        self.homeDescriptionLabel = QtWidgets.QLabel(self.homeTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        self.homeDescriptionLabel.setSizePolicy(sizePolicy)
        self.homeDescriptionLabel.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)
        self.homeDescriptionLabel.setObjectName("homeDescriptionLabel")
        self.homeTabGridLayout.addWidget(self.homeDescriptionLabel, 1, 0, 1, 2)

        self.resultsGroupBox = QtWidgets.QGroupBox(self.homeTab)
        self.resultsGroupBox.setObjectName("resultsGroupBox")
        self.resultsGroupBox.setSizePolicy(
            QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed))
        self.resultsGroupBox.setFixedWidth(207)
        self.homeTabGridLayout.addWidget(self.resultsGroupBox, 2, 0, 1, 1)

        self.resultsGroupBoxGridLayout = QtWidgets.QGridLayout(self.resultsGroupBox)
        self.resultsGroupBoxGridLayout.setObjectName("resultsGroupBoxGridLayout")

        self.natTypeLabel = QtWidgets.QLabel(self.resultsGroupBox)
        self.natTypeLabel.setObjectName("natTypeLabel")
        self.natTypeLabel.setStyleSheet("font-weight:600;")
        self.resultsGroupBoxGridLayout.addWidget(self.natTypeLabel, 0, 0, 1, 1)

        self.extIPLabel = QtWidgets.QLabel(self.resultsGroupBox)
        self.extIPLabel.setObjectName("extIPLabel")
        self.resultsGroupBoxGridLayout.addWidget(self.extIPLabel, 1, 0, 1, 1)

        self.extPortLabel = QtWidgets.QLabel(self.resultsGroupBox)
        self.extPortLabel.setObjectName("extPortLabel")
        self.resultsGroupBoxGridLayout.addWidget(self.extPortLabel, 2, 0, 1, 1)

        self.natTypeResultLabel = QtWidgets.QLabel(self.resultsGroupBox)
        self.natTypeResultLabel.setObjectName("natTypeResultLabel")
        self.resultsGroupBoxGridLayout.addWidget(self.natTypeResultLabel, 0, 1, 1, 1)

        self.extIPResultLabel = QtWidgets.QLabel(self.resultsGroupBox)
        self.extIPResultLabel.setObjectName("extIPResultLabel")
        self.resultsGroupBoxGridLayout.addWidget(self.extIPResultLabel, 1, 1, 1, 1)

        self.extPortResultLabel = QtWidgets.QLabel(self.resultsGroupBox)
        self.extPortResultLabel.setObjectName("extPortResultLabel")
        self.resultsGroupBoxGridLayout.addWidget(self.extPortResultLabel, 2, 1, 1, 1)

        self.natRepresentation = QtWidgets.QLabel(self.homeTab)
        self.natRepresentation.setSizePolicy(
            QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred))
        self.natRepresentation.setFixedWidth(225)

        self.setNatRepresentation("UnknownNAT.png")

        self.natRepresentation.setObjectName("natRepresentation")
        self.homeTabGridLayout.addWidget(self.natRepresentation, 2, 1, 1, 1)

        self.startButton = QtWidgets.QPushButton(self.homeTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        self.startButton.setSizePolicy(sizePolicy)
        self.startButton.setObjectName("startButton")
        self.homeTabGridLayout.addWidget(self.startButton, 3, 0, 1, 2, QtCore.Qt.AlignHCenter)

        self.optionsTab = QtWidgets.QWidget()
        self.optionsTab.setObjectName("optionsTab")
        self.tabWidget.addTab(self.optionsTab, "")
        portRegExp = QRegExp("([1-9][0-9]{0,3}|[1-5][0-9]{4}|6[0-4][0-9]{3}|65[0-4][0-9]{2}|655[0-3][0-9]|6553[0-5])")

        self.optionsTabVLayout = QtWidgets.QVBoxLayout(self.optionsTab)
        self.optionsTabVLayout.setObjectName("optionsTabVLayout")

        self.stunServerGroupBox = QtWidgets.QGroupBox(self.optionsTab)
        self.stunServerGroupBox.setChecked(False)
        self.stunServerGroupBox.setObjectName("stunServerGroupBox")
        self.optionsTabVLayout.addWidget(self.stunServerGroupBox)

        self.stunServerGroupBoxHLayout = QtWidgets.QHBoxLayout(self.stunServerGroupBox)
        self.stunServerGroupBoxHLayout.setObjectName("stunServerGroupBoxHLayout")

        self.serverHostnameLabel = QtWidgets.QLabel(self.stunServerGroupBox)
        self.serverHostnameLabel.setObjectName("serverHostnameLabel")
        self.stunServerGroupBoxHLayout.addWidget(self.serverHostnameLabel)

        self.serverHostnameField = QtWidgets.QLineEdit(self.stunServerGroupBox)
        self.serverHostnameField.setText("stun.sipgate.net")
        self.serverHostnameField.setObjectName("serverHostnameField")
        self.stunServerGroupBoxHLayout.addWidget(self.serverHostnameField)

        self.serverPortLabel = QtWidgets.QLabel(self.stunServerGroupBox)
        self.serverPortLabel.setObjectName("serverPortLabel")
        self.stunServerGroupBoxHLayout.addWidget(self.serverPortLabel)

        self.serverPortField = QtWidgets.QLineEdit(self.stunServerGroupBox)
        self.serverPortField.setFixedWidth(50)
        self.serverPortField.setValidator(QRegExpValidator(portRegExp))
        self.serverPortField.setText("3478")
        self.serverPortField.setMaxLength(5)
        self.serverPortField.setObjectName("serverPortField")
        self.stunServerGroupBoxHLayout.addWidget(self.serverPortField)

        self.netParamsGroupBox = QtWidgets.QGroupBox(self.optionsTab)
        self.netParamsGroupBox.setObjectName("netParamsGroupBox")
        self.optionsTabVLayout.addWidget(self.netParamsGroupBox)

        self.netParamsGroupBoxHLayout = QtWidgets.QHBoxLayout(self.netParamsGroupBox)
        self.netParamsGroupBoxHLayout.setObjectName("netParamsGroupBoxHLayout")

        self.sourceIPLabel = QtWidgets.QLabel(self.netParamsGroupBox)
        self.sourceIPLabel.setObjectName("sourceIPLabel")
        self.netParamsGroupBoxHLayout.addWidget(self.sourceIPLabel)

        self.sourceIPComboBox = QtWidgets.QComboBox(self.netParamsGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        self.sourceIPComboBox.setSizePolicy(sizePolicy)
        self.sourceIPComboBox.setObjectName("sourceIPComboBox")
        self.netParamsGroupBoxHLayout.addWidget(self.sourceIPComboBox)

        self.localPortLabel = QtWidgets.QLabel(self.netParamsGroupBox)
        self.localPortLabel.setObjectName("localPortLabel")
        self.netParamsGroupBoxHLayout.addWidget(self.localPortLabel)

        self.localPortField = QtWidgets.QLineEdit(self.netParamsGroupBox)
        self.localPortField.setFixedWidth(50)
        self.localPortField.setValidator(QRegExpValidator(portRegExp))
        self.localPortField.setText("54320")
        self.localPortField.setMaxLength(5)
        self.localPortField.setObjectName("localPortField")
        self.netParamsGroupBoxHLayout.addWidget(self.localPortField)

        self.showLogCheckBox = QtWidgets.QCheckBox(self.optionsTab)
        self.showLogCheckBox.setObjectName("showLogCheckBox")
        self.optionsTabVLayout.addWidget(self.showLogCheckBox)

        self.setCentralWidget(self.centralWidget)

        self.retranslateUi()
        self.tabWidget.setCurrentIndex(0)

    def setNatRepresentation(self, imageName):
        imagePath = "res/natRepresentations/" + imageName
        pixmap = QtGui.QPixmap(imagePath)
        movie = QtGui.QMovie(imagePath)
        movieSize = pixmap.size()
        movie.setScaledSize(
            movieSize.scaled(self.natRepresentation.width(), movieSize.height(), QtCore.Qt.KeepAspectRatio))
        movie.start()
        self.natRepresentation.setMovie(movie)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.extIPLabel.setText(_translate("STUNATView", "Indirizzo IP\nesterno:"))
        self.natTypeLabel.setText(_translate("STUNATView", "Tipo di NAT:"))
        self.extPortLabel.setText(_translate("STUNATView", "Porta esterna:"))
        self.homeDescriptionLabel.setText(_translate("STUNATView",
                                                     "Scopri il tipo di NAT presente sulla tua rete."
                                                     "Clicca su Inizia test e attendi il risultato."))
        self.startButton.setText(_translate("STUNATView", "Inizia test"))
        self.stunServerGroupBox.setTitle(_translate("STUNATView", "Server STUN"))
        self.serverHostnameLabel.setText(_translate("STUNATView", "Hostname o Indirizzo IP"))
        self.serverPortLabel.setText(_translate("STUNATView", "Porta"))
        self.netParamsGroupBox.setTitle(_translate("STUNATView", "Parametri di rete"))
        self.sourceIPLabel.setText(_translate("STUNATView", "Indirizzo IP sorgente"))
        self.localPortLabel.setText(_translate("STUNATView", "Porta locale"))
        self.showLogCheckBox.setText(_translate("STUNATView", "Visualizza log avanzato"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.optionsTab), _translate("STUNATView", "Opzioni"))
