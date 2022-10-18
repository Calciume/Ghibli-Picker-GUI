# importing libraries
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *
import sys


class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        # setting title
        self.setWindowTitle("Python ")

        # setting geometry
        self.setGeometry(0, 0, 600, 400)

        # calling method
        self.UiComponents()

        # showing all the widgets
        self.show()

    # method for widgets
    def UiComponents(self):
        # creating a push button
        button = QPushButton("Pick a movie for me!", self)

        # setting geometry of button
        button.setGeometry(500, 150, 200, 40)

        # adding action to a button
        button.clicked.connect(self.option1)

    # action method
    def option1(self):
        # printing pressed
        print("pressed")


# create pyqt5 app
App = QApplication(sys.argv)

# create the instance of our Window
window = Window()

# start the app
sys.exit(App.exec())
