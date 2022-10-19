# importing libraries
from PyQt6.QtWidgets import QLabel, QMainWindow, QPushButton, QApplication, QMenuBar, QGridLayout, QMenu
from PyQt6.QtGui import *
# from PyQt6.QtCore import *
import sys


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        # setting title
        self.setWindowTitle("Ghibli Picker")
        # setting geometry
        self.setFixedSize(500, 276)
        # calling actions for menubar
        self.menubaractions()
        # calling menubar
        self.createmenubar()
        # calling method
        self.UiComponents()
        # showing all the widgets
        self.show()

    def menubaractions(self):
        # Create action with first constructor
        self.newAction = QAction(self)
        # Create action with second constructor
        self.aboutAction = QAction("&About", self)

    def createmenubar(self):
        menuBar = self.menuBar()
        # File Menu
        filemenu = QMenu("&File", self)
        menuBar.addMenu(filemenu)

        # Help Menu
        helpmenu = QMenu("&Help", self)
        menuBar.addMenu(helpmenu)
        helpmenu.addAction(self.aboutAction)
        # Creating menus with a title


    # method for widgets
    def UiComponents(self):
        options = ["1. Pick a movie for me", "2. Exclude a movie", "3. Save", "4. Load", "5. Exit"]
        buttonpos_x = 10
        buttonpos_y = 26
        buttonsize_x = 200
        buttonsize_y = 40

        # Displaying the picture
        label = QLabel(self)
        label.setPixmap(QPixmap("ghibli.png"))
        label.show()
        label.setGeometry(235, 26, 240, 240)

        # Loop to add the button row
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
