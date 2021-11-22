import sys

from PyQt5 import QtWidgets

from src.view.STUNATView import STUNATView

app = QtWidgets.QApplication(sys.argv)
mainWindow = STUNATView()
mainWindow.show()
sys.exit(app.exec_())