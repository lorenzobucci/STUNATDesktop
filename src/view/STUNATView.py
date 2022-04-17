from PyQt5.QtCore import Qt, QSize, QRect, QTranslator, QCoreApplication, QLocale, QLibraryInfo
from PyQt5.QtGui import QCursor, QIcon
from PyQt5.QtWidgets import QMessageBox, QMainWindow, QWidget, QTabWidget, QApplication

from utils import _path
from view.components.TabWidgets import HomeTab, OptionsTab


# Finestra principale dell'applicazione
# Codice in larga parte generato automaticamente da QtDesigner su cui è stata eseguita una fattorizzazione
class STUNATView(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setObjectName("STUNATView")
        self.setWindowTitle("STUNAT Desktop")

        self.setFixedSize(QSize(480, 300))

        self.setWindowIcon(QIcon(_path("res/icon.ico")))

        self.centralWidget = QWidget(self)
        self.centralWidget.setObjectName("centralWidget")

        self.tabWidget = QTabWidget(self.centralWidget)
        self.tabWidget.setGeometry(QRect(10, 10, 462, 282))
        self.tabWidget.setObjectName("tabWidget")

        # Tab principale (Home)
        self.homeTab = HomeTab()
        self.homeTab.setObjectName("homeTab")
        self.tabWidget.addTab(self.homeTab, "STUNAT")

        # Tab opzioni avanzate
        self.optionsTab = OptionsTab()
        self.optionsTab.setObjectName("optionsTab")
        self.tabWidget.addTab(self.optionsTab, "")

        self.setCentralWidget(self.centralWidget)
        self.tabWidget.setCurrentIndex(0)

        # Inizializzazione lingua applicazione (Italiano o Inglese)
        # La lingua dell'applicazione è scelta automaticamente in base alla lingua di sistema
        self.translator = QTranslator(self)
        self.optionsTab.languageComboBox.currentIndexChanged.connect(self._languageChangedHandler)
        if QLocale.system().name() == "it_IT":
            currentOSLanguage = "Italiano"
        else:
            currentOSLanguage = "English"
        self.optionsTab.languageComboBox.setCurrentText(currentOSLanguage)
        self._retranslateUi()

        # Settaggio lingua di visualizzazione delle librerie native pyqt (es. menu contestuali) sulla base della lingua
        # di sistema
        self.qtTranslator = QTranslator(self)
        self.qtTranslator.load("qtbase_" + QLocale.system().name(),
                               QLibraryInfo.location(QLibraryInfo.TranslationsPath))
        QApplication.instance().installTranslator(self.qtTranslator)

    def setBusyCursor(self):
        """
        Imposta il cursore del mouse relativo alla finestra su "Occupato".
        """
        self.setCursor(QCursor(Qt.WaitCursor))

    def showErrorMessage(self, message: str):
        """
        Apre un message box per segnalare un errore grave.
        :param message: Stringa di errore da visualizzare
        """
        errorBox = QMessageBox()
        errorBox.setIcon(QMessageBox.Critical)
        errorBox.setText(message)
        errorBox.setWindowTitle("Error")
        errorBox.exec_()

    def _languageChangedHandler(self, index):
        """
        Gestisce la traduzione nel caso venga cambiata la lingua dell'applicazione.
        """
        data = self.optionsTab.languageComboBox.itemData(index)
        if data:
            self.translator.load(data, _path("res"))
            QApplication.instance().installTranslator(self.translator)
        else:
            QApplication.instance().removeTranslator(self.translator)
        self._retranslateUi()

    def _retranslateUi(self):
        _translate = QCoreApplication.translate
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.optionsTab), _translate("STUNATView", "Opzioni"))
        self.homeTab.retranslateUi()  # Propagazione della traduzione nella tab Home
        self.optionsTab.retranslateUi()  # Propagazione della traduzione nella tab Opzioni
