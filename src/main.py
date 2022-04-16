import sys

from PyQt5 import QtWidgets

from controller.Controller import Controller
from model.Model import Model
from view.STUNATView import STUNATView

app = QtWidgets.QApplication(sys.argv)

# Inizializzazione modello, vista e relativo controller per dependency injection
model = Model()
mainWindow = STUNATView()
controller = Controller(mainWindow, model)

# Lancio finestra principale PyQt
mainWindow.show()
sys.exit(app.exec_())
