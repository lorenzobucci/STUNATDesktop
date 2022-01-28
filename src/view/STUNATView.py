from PyQt5.QtCore import Qt, QSize, QRect, QTranslator, QCoreApplication, QLocale, QLibraryInfo
from PyQt5.QtGui import QCursor
from PyQt5.QtWidgets import QMessageBox, QMainWindow, QWidget, QTabWidget, QApplication

from view.TabWidgets import HomeTab, OptionsTab


class STUNATView(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setObjectName("STUNATView")
        self.setWindowTitle("STUNAT Desktop")

        self.setFixedSize(QSize(480, 300))

        self.centralWidget = QWidget(self)
        self.centralWidget.setObjectName("centralWidget")

        self.tabWidget = QTabWidget(self.centralWidget)
        self.tabWidget.setGeometry(QRect(10, 10, 462, 282))
        self.tabWidget.setObjectName("tabWidget")

        self.homeTab = HomeTab()
        self.homeTab.setObjectName("homeTab")
        self.tabWidget.addTab(self.homeTab, "STUNAT")

        self.optionsTab = OptionsTab()
        self.optionsTab.setObjectName("optionsTab")
        self.tabWidget.addTab(self.optionsTab, "")

        self.setCentralWidget(self.centralWidget)
        self.tabWidget.setCurrentIndex(0)

        self.translator = QTranslator(self)
        self.optionsTab.languageComboBox.currentIndexChanged.connect(self._languageChangedHandler)
        if QLocale.system().name() == "it_IT":
            currentOSLanguage = "Italiano"
        else:
            currentOSLanguage = "English"
        self.optionsTab.languageComboBox.setCurrentText(currentOSLanguage)
        self._retranslateUi()

        self.qtTranslator = QTranslator(self)
        self.qtTranslator.load("qtbase_" + QLocale.system().name(),
                               QLibraryInfo.location(QLibraryInfo.TranslationsPath))
        QApplication.instance().installTranslator(self.qtTranslator)

    def setBusyCursor(self):
        self.setCursor(QCursor(Qt.WaitCursor))

    def showErrorMessage(self, message):
        errorBox = QMessageBox()
        errorBox.setIcon(QMessageBox.Critical)
        errorBox.setText(message)
        errorBox.setWindowTitle("Error")
        errorBox.exec_()

    def _languageChangedHandler(self, index):
        data = self.optionsTab.languageComboBox.itemData(index)
        if data:
            self.translator.load(data, "view")
            QApplication.instance().installTranslator(self.translator)
        else:
            QApplication.instance().removeTranslator(self.translator)
        self._retranslateUi()

    def _retranslateUi(self):
        _translate = QCoreApplication.translate
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.optionsTab), _translate("STUNATView", "Opzioni"))
        self.homeTab.retranslateUi()
        self.optionsTab.retranslateUi()
