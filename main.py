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
        options = ["Option1", "Option2", "Option3", "Option4", "Option5"]
        buttonpos_x = 10
        buttonpos_y = 10
        buttonsize_x = 200
        buttonsize_y = 40

        # creating a push button
        button1 = QPushButton(options[0], self)
        # setting geometry of button
        button1.setGeometry(buttonpos_x, buttonpos_y, buttonsize_x, buttonsize_y)
        # adding action to a button
        button1.clicked.connect(self.option1)

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
