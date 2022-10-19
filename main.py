# importing libraries
from PyQt6.QtWidgets import QLabel, QMainWindow, QPushButton, QApplication
from PyQt6.QtGui import *
# from PyQt6.QtCore import *
import sys


class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        # setting title
        self.setWindowTitle("Ghibli Picker")

        # setting geometry
        self.setFixedSize(500, 260)

        # calling method
        self.UiComponents()

        # showing all the widgets
        self.show()

    # method for widgets
    def UiComponents(self):
        options = ["1. Pick a movie for me", "2. Exclude a movie", "3. Save", "4. Load", "5. Exit"]
        buttonpos_x = 10
        buttonpos_y = 10
        buttonsize_x = 200
        buttonsize_y = 40
        # Displaying the picture
        label = QLabel(self)
        label.setPixmap(QPixmap("ghibli.png"))
        label.show()
        label.setGeometry(235, 10, 240, 240)

        for i in range(5):
            # creating a push button
            button1 = QPushButton(options[i], self)
            # setting geometry of button
            button1.setGeometry(buttonpos_x, buttonpos_y, buttonsize_x, buttonsize_y)
            # Decrease the position of button each loop
            buttonpos_y += 50
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
