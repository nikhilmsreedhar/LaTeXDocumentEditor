import sys
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2.QtCore import *




# Subclass QMainWindow to customise your application's main window
class MainWindow(QMainWindow):

    def mainScreen(self):
        print('bruh')
        self.stackPane.setCurrentIndex(0)

    def newFileScreen(self):
        print('hello')
        self.stackPane.setCurrentIndex(1)






    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        """
        HOME PAGE UI CODE
        """
        self.setWindowTitle("APP NAME")
        self.homeHBox = QHBoxLayout(self)
        self.homeVBox = QVBoxLayout(self)

        self.homeAppName = QLabel("App Name")
        self.homeAppName.setFont(QFont("Times", 36, QFont.Bold))
        self.homeAppName.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.homeVBox.addWidget(self.homeAppName)

        self.homeHomeButton = QPushButton("Home")
        self.homeHomeButton.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.homeVBox.addWidget(self.homeHomeButton)

        self.homeNewFileButton = QPushButton("New File")
        self.homeNewFileButton.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.homeNewFileButton.clicked.connect(self.newFileScreen)
        self.homeVBox.addWidget(self.homeNewFileButton)

        self.homeOpenFileButton = QPushButton("Open File")
        self.homeOpenFileButton.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.homeVBox.addWidget(self.homeOpenFileButton)

        self.homeAppText = QLabel("One dollar and eighty-seven cents. That was all. And sixty cents of it was in pennies. Pennies saved one and two at a time by bulldozing the grocer and the vegetable man and the butcher until one’s cheeks burned with the silent imputation of parsimony that such close dealing implied. One dollar and eighty-seven cents. And the next day would be Christmas...jjjjjj jjjjjjjjjj jjjjjjjjjjj jjjjjjj jjjjjjjjjj jjjjj jjjjjj jjjj jjjjj jjjjjjj jjjjj jjjjj jjj jjjL OLO LOL")
        self.homeAppText.setWordWrap(True)
        self.homeAppText.setFont(QFont("Times", 24, QFont.Bold))

        self.homeFormatingVBox = QVBoxLayout(self)
        self.homeFormatingVBox.addWidget(self.homeAppText)
        self.homeFormatingVBox.addSpacing(500)

        self.homeHBox.addLayout(self.homeVBox)
        self.homeHBox.addSpacing(300)
        self.homeHBox.addLayout(self.homeFormatingVBox)


        self.homeWidget = QWidget()
        self.homeWidget.setLayout(self.homeHBox)
        """
        END OF HOME PAGE UI
        """

        """
        START OF MAIN PAGE UI
        """
        self.mainVBox = QVBoxLayout(self)
        self.mainTabHBox = QHBoxLayout(self)

        self.mainFileButton = QPushButton("File")
        self.mainFileButton.clicked.connect(self.mainScreen)

        self.mainInsertButton = QPushButton("Insert")

        self.mainTabHBox.addWidget(self.mainFileButton)
        self.mainTabHBox.addWidget(self.mainInsertButton)
        self.mainTabHBox.addSpacing(1000)

        self.mainVBox.addLayout(self.mainTabHBox)

        self.mainWidget = QWidget()
        self.mainWidget.setLayout(self.mainVBox)



        """
        END OF MAIN PAGE UI
        """
        self.stackPane = QStackedLayout(self)
        self.stackPane.addWidget(self.homeWidget)
        self.stackPane.addWidget(self.mainWidget)

        self.widget = QWidget()
        self.widget.setLayout(self.stackPane)




        # self.setLayout(self.hBox)
        # self.homePage = HomePageWidget(self)

        # Set the central widget of the Window. Widget will expand
        # to take up all the space in the window by default.
        self.setCentralWidget(self.widget)
        self.setGeometry(0,0,2000,2000)

# class HomePageWidget(QWidget):
#     def onPushNewFile(parent):
#         print('hello')
#         parent.hide()
#
#
#
#
#     def __init__(self, parent):
#         super(HomePageWidget, self).__init__(parent)
#         self.hBox = QHBoxLayout(self)
#         self.vBox = QVBoxLayout(self)
#
#         self.label = QLabel("App Name")
#         self.label.setFont(QFont("Times", 36, QFont.Bold))
#         self.label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
#         self.vBox.addWidget(self.label)
#
#         self.button1 = QPushButton("Home")
#         self.button1.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
#         self.vBox.addWidget(self.button1)
#
#         self.button2 = QPushButton("New File")
#         self.button2.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
#         self.button2.clicked.connect(self.onPushNewFile)
#         self.vBox.addWidget(self.button2)
#
#         self.button3 = QPushButton("Open File")
#         self.button3.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
#         self.vBox.addWidget(self.button3)
#
#         self.hBox.addLayout(self.vBox)
#         self.hBox.addStretch()
#         self.hBox.addStretch()
#         self.hBox.addStretch()
#         self.hBox.addStretch()
#         self.hBox.addStretch()
#         self.hBox.addStretch()
#         self.hBox.addStretch()
#         self.hBox.addStretch()
#
#
#         self.setLayout(self.hBox)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec_()