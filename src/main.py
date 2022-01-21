import sys

from PyQt5 import QtWidgets

from controller.Controller import Controller
from model.Model import Model
from src.view.STUNATView import STUNATView

app = QtWidgets.QApplication(sys.argv)
model = Model()
mainWindow = STUNATView()
controller = Controller(mainWindow, model)
mainWindow.show()
sys.exit(app.exec_())