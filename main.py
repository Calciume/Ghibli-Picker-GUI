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
        self.main_menu()
        # showing all the widgets
        self.show()

    def menubaractions(self):
        # Create action with first constructor
        self.newAction = QAction(self)
        # File menu actions
        self.openAction = QAction("&Open", self)
        self.saveAction = QAction("&Save", self)
        self.loadAction = QAction("&Load", self)
        self.exitAction = QAction("&Exit", self)

        # About menu actions
        self.aboutAction = QAction("&About", self)

    def createmenubar(self):
        menubar = self.menuBar()
        # File Menu
        filemenu = QMenu("&File", self)
        menubar.addMenu(filemenu)
        filemenu.addAction(self.openAction)
        filemenu.addAction(self.saveAction)
        filemenu.addAction(self.loadAction)
        filemenu.addAction(self.exitAction)
        # Help Menu
        helpmenu = QMenu("&Help", self)
        menubar.addMenu(helpmenu)
        helpmenu.addAction(self.aboutAction)
        # Creating menus with a title

    # method for widgets
    def main_menu(self):
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

        # Defining each button
        button0 = QPushButton(options[0], self)
        button1 = QPushButton(options[1], self)
        button2 = QPushButton(options[2], self)
        button3 = QPushButton(options[3], self)
        button4 = QPushButton(options[4], self)

        # Set the geometry of each button
        button0.setGeometry(buttonpos_x, buttonpos_y, buttonsize_x, buttonsize_y)
        buttonpos_y += 50
        button1.setGeometry(buttonpos_x, buttonpos_y, buttonsize_x, buttonsize_y)
        buttonpos_y += 50
        button2.setGeometry(buttonpos_x, buttonpos_y, buttonsize_x, buttonsize_y)
        buttonpos_y += 50
        button3.setGeometry(buttonpos_x, buttonpos_y, buttonsize_x, buttonsize_y)
        buttonpos_y += 50
        button4.setGeometry(buttonpos_x, buttonpos_y, buttonsize_x, buttonsize_y)

        # Set each click action
        button0.clicked.connect(self.option0)
        button1.clicked.connect(self.option1)
        button2.clicked.connect(self.option2)
        button3.clicked.connect(self.option3)
        button4.clicked.connect(self.option4)

    # action method
    def option0(self):
        # printing pressed
        print("pressed")

    def option1(self):
        pass

    def option2(self):
        pass

    def option3(self):
        pass

    def option4(self):
        pass

# create pyqt5 app
App = QApplication(sys.argv)

# create the instance of our Window
window = Window()

# start the app
sys.exit(App.exec())
