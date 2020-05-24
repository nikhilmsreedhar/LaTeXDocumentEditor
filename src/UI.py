import sys
import json
import PySide2
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PIL import Image
from PIL.ImageQt import ImageQt
import io
import main

# Subclass QMainWindow to customise your application's main window
class MainWindow(QMainWindow):

    def mainScreen(self):
        num = self.mainPreviewVBox.count()
        print(num)
        y = 0
        for x in range(num):
            # print(y)
            if isinstance(self.mainPreviewVBox.itemAt(y), PySide2.QtWidgets.QSpacerItem):
                self.mainPreviewVBox.removeItem(self.mainPreviewVBox.itemAt(y))
                # y += 1
            else:
                self.mainPreviewVBox.removeWidget(self.mainPreviewVBox.itemAt(y).widget())

        print(self.mainPreviewVBox.count())
        self.mainPreviewVBox.activate()
        self.mainPreviewVBox.addSpacing(1000)

        self.stackPane.setCurrentIndex(0)

    def dlgAccept(self):
        self.saveFile()
        self.dlg.close()
        self.mainScreen()

    def dlgReject(self):
        self.dlg.close()
        self.mainScreen()

    def returnToMainScreen(self):
        if not self.save:
            self.dlg = QDialog(self)
            self.dlg.setWindowTitle("Unsaved Changes")

            self.mainVerticalLayout = QVBoxLayout(self.dlg)
            self.questionGroupBox = QLabel("Do you want to close without saving?")
            self.mainVerticalLayout.addWidget(self.questionGroupBox)

            self.buttonBox = QDialogButtonBox()
            self.buttonBox.setStandardButtons(QDialogButtonBox.Save | QDialogButtonBox.Close)
            self.buttonBox.button(QDialogButtonBox.Save).clicked.connect(self.dlgAccept)
            self.buttonBox.button(QDialogButtonBox.Close).clicked.connect(self.dlgReject)
            self.mainVerticalLayout.addWidget(self.buttonBox)

            self.dlg.setWindowModality(Qt.ApplicationModal)
            self.dlg.exec_()
        else:
            self.mainScreen()


    def fileUpload(self):
        filename = QFileDialog.getOpenFileName(self, 'Open File', '../imgs/', "Images (*.png *.xpm *.jpg)")
        # 3rd parameter in previous line is default directory to open to
        stringName = self.elementName.text()#append to array
        self.array.append(stringName)
        print(stringName)
        if filename:
            img = main.get_image_from_input(str(filename[0]), stringName, 1)

        self.elementImage = ImageQt(img)
        # get rid of the file upload button
        self.elementBodyStackPane.setCurrentIndex(1)
        # get rid of the file upload button





    def submitChem(self):
        text_in = self.elementInput.text()
        stringName = self.elementName.text()
        img = main.get_image_from_input(text_in, stringName, 2)
        print(img)

    def addPar(self):
        text_in = self.elementInput.text()
        stringName = self.elementName.text()
        main.get_image_from_input(text_in, stringName, 3)
        latexTextFile = open("../out/" + stringName + ".txt", "r")
        print(latexTextFile.read())


    def addSec(self):
        text_in = self.elementInput.text()
        stringName = self.elementName.text()
        main.get_image_from_input(text_in, stringName, 4)
        latexTextFile = open("../out/" + stringName + ".txt", "r")
        print(latexTextFile.read())

    def addSubSec(self):
        text_in = self.elementInput.text()
        stringName = self.elementName.text()
        main.get_image_from_input(text_in, stringName, 5)
        latexTextFile = open("../out/" + stringName + ".txt", "r")
        print(latexTextFile.read())



    def submitMath(self):
        text_in = self.elementInput.text()
        stringName = self.elementName.text()
        img = main.get_image_from_input(text_in, stringName, 0)
        print(img)



    def newFileScreen(self):
        self.stackPane.setCurrentIndex(1)
        for x in range(self.mainPreviewVBox.count()):
            print(self.mainPreviewVBox.itemAt(x))

    def insertElement(self, string):
        self.save = False
        maxElements = 10
        num = self.mainPreviewVBox.count()
        if num > 0:
            self.mainPreviewVBox.itemAt(num - 1).changeSize(0,0)

        self.elementHeaderHBox = QHBoxLayout(self)


        if string == 'type math':
            self.elementName = QLineEdit("Name your element! (e.g. Equation 1)")
            #self.elementName.setGeometry(0,0,100,100)
            # self.elementName.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
            self.elementHeaderHBox.addWidget(self.elementName)
            self.elementHeaderHBox.addSpacing(150)
            self.elementBodyStackPane = QStackedLayout(self)
            self.elementVBoxButton = QVBoxLayout(self)
            self.elementSubmitButton = QPushButton('Add Math')
            self.elementVBoxButton.addWidget(QLineEdit("Type your equation here in natural language (e.g. integral of x^3 dx)."))
            self.elementVBoxButton.addWidget(self.elementSubmitButton)
            self.elementSubmitWidget = QWidget()
            self.elementSubmitWidget.setLayout(self.elementVBoxButton)
            self.elementBodyStackPane.addWidget(self.elementSubmitWidget)




        elif string == 'image math':
            self.elementName = QLineEdit("Name your element! (e.g. Equation 2)")
            # self.elementName.setGeometry(0,0,100,100)
            # self.elementName.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
            self.elementHeaderHBox.addWidget(self.elementName)
            self.elementHeaderHBox.addSpacing(150)
            self.elementBodyStackPane = QStackedLayout(self)
            self.fileUploadButton = QPushButton("Upload File")
            self.fileUploadButton.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
            self.fileUploadButton.setCursor(QCursor(Qt.PointingHandCursor))
            self.fileUploadButton.setFont(QFont("Times", 12))
            self.elementImage = None
            self.fileUploadButton.clicked.connect(self.fileUpload)
            self.elementBodyStackPane.addWidget(self.fileUploadButton)
            self.elementOptionsHBox = QHBoxLayout()
            self.elementPixMap = QPixmap.fromImage(self.elementImage)
            self.elementEditButton = QPushButton('Edit')
            self.elementDeleteButton = QPushButton('Delete')
            self.elementMoveButton = QPushButton('Move')
            self.elementOptionsHBox.addWidget(self.elementPixMap)
            self.elementOptionsHBox.addWidget(self.elementEditButton)
            self.elementOptionsHBox.addWidget(self.elementDeleteButton)
            self.elementOptionsHBox.addWidget(self.elementMoveButton)   
            self.elementViewWidget = QtWidget()
            self.elementViewWidget.setLayout(self.elementOptionsHBox)
            self.elementBodyStackPane.addWidget(self.elementViewWidget)

        elif string == 'molecule':
            self.elementName = QLineEdit("Name your element! (e.g. Glucose Molecule)")
            # self.elementName.setGeometry(0,0,100,100)
            # self.elementName.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
            self.elementHeaderHBox.addWidget(self.elementName)
            self.elementHeaderHBox.addSpacing(150)
            self.elementBodyStackPane = QStackedLayout(self)
            self.elementBodyStackPane.addWidget(QLineEdit("Type the name of the molecule you want here (e.g. glucose)."))

        elif string == 'paragraph':
            self.elementName = QLineEdit("Name your element! (e.g. Paragraph 1)")
            # self.elementName.setGeometry(0,0,100,100)
            # self.elementName.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
            self.elementHeaderHBox.addWidget(self.elementName)
            self.elementHeaderHBox.addSpacing(150)
            self.elementBodyStackPane = QStackedLayout(self)
            self.elementBodyStackPane.addWidget(QLineEdit("Type your paragraph here."))

        elif string == 'section':
            self.elementName = QLineEdit("Name your element! (e.g. Section 1)")
            # self.elementName.setGeometry(0,0,100,100)
            # self.elementName.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
            self.elementHeaderHBox.addWidget(self.elementName)
            self.elementHeaderHBox.addSpacing(150)
            self.elementBodyStackPane = QStackedLayout(self)
            self.elementBodyStackPane.addWidget(QLineEdit("Type your section name here."))

        else:
            self.elementName = QLineEdit("Name your element! (e.g. Subsection 3.4)")
            # self.elementName.setGeometry(0,0,100,100)
            # self.elementName.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
            self.elementHeaderHBox.addWidget(self.elementName)
            self.elementHeaderHBox.addSpacing(150)
            # string is subsection
            self.elementBodyStackPane = QStackedLayout(self)
            self.elementBodyStackPane.addWidget(QLineEdit("Type your subsection name here."))

        self.elementFinalVBox = QVBoxLayout(self)

        self.elementFinalVBox.addLayout(self.elementHeaderHBox)
        self.elementFinalVBox.addLayout(self.elementBodyStackPane)

        self.elementWidget = QWidget()
        self.elementWidget.setLayout(self.elementFinalVBox)


        self.mainPreviewVBox.addSpacing(50)
        self.mainPreviewVBox.addWidget(self.elementWidget)
        self.mainPreviewVBox.addSpacing(990)

    def saveFile(self):
        print("saveee")
        self.save = True
        #how to convert the array to json then save the json locally on out folder

    def export(self):
        print("exporttt")

    def typeMath(self):
        self.insertElement('type math')

    def imageMath(self):
        self.insertElement('image math')

    def molecule(self):
        self.insertElement('molecule')

    def paragraph(self):
        self.insertElement('paragraph')

    def section(self):
        self.insertElement('section')

    def subsection(self):
        self.insertElement('subsection')

    # convert the strings to json then saving the file locally
    def convertToJson(self):
        dictionary = {}
        for x in range(len(self.array)):
             dictionary.update(x, self.array[x])

        with open("project_data.json", "w") as write_file:
            json.dump(dictionary, write_file)




    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.save = True
        """
        HOME PAGE UI CODE
        """
        self.setWindowTitle("APP NAME")
        self.setStyleSheet('background-color: rgb(255, 230, 232)')
        self.homeHBox = QHBoxLayout(self)
        self.homeVBox = QVBoxLayout(self)
        self.homeV2Box = QVBoxLayout(self)
        self.homeH2Box = QHBoxLayout(self)
        self.homeH2Box.setSpacing(0)

        self.array = []


        self.homeAppName = QLabel("EzLaTeX")
        self.homeAppName.setFont(QFont("Times", 36, QFont.Bold))
        self.homeAppName.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.homeAppName.setAlignment(Qt.AlignCenter)
        self.homeAppName.setStyleSheet("""
        QWidget {

        background-color: rgb(173, 216, 230);
        position: absolute;
        top: 0px;
        height: 20 px;
        border-top-left-radius: 5px;
        border-top-right-radius: 20px;
        border-bottom-left-radius: 20px;
        border-bottom-right-radius: 10px;
        }
        """)

        self.homeVBox.addWidget(self.homeAppName)

        self.homeHomeButton = QPushButton("Home")
        self.homeHomeButton.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.homeH2Box.addWidget(self.homeHomeButton)
        self.homeHomeButton.setFont(QFont("Times", 36, QFont.Bold))
        self.homeHomeButton.setStyleSheet("""
        QWidget {
            border: 0.1px solid gray;
            background-color: rgb(173, 216, 230);
            padding-right: 0px;
            width: 33%;
            height: 200%;
            border-bottom-left-radius: 25px;
            border-top-left-radius: 25px;
            }
        """)

        self.homeNewFileButton = QPushButton("New File")
        self.homeNewFileButton.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.homeNewFileButton.setFont(QFont("Times", 36, QFont.Bold))

        self.homeNewFileButton.clicked.connect(self.newFileScreen)
        self.homeNewFileButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.homeNewFileButton.clicked.connect(self.newFileScreen)
        self.homeH2Box.addWidget(self.homeNewFileButton)
        self.homeNewFileButton.setStyleSheet("""
        QWidget {
            border: 0.1px solid gray;
            background-color: rgb(173, 216, 230);
            padding-right: 0px;
            padding-left: 0px;
            width: 33%;
            height: 200%;
            }
        """)

        self.homeOpenFileButton = QPushButton("Open File")
        self.homeOpenFileButton.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.homeOpenFileButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.homeOpenFileButton.setFont(QFont("Times", 36, QFont.Bold))
        self.homeH2Box.addWidget(self.homeOpenFileButton)
        self.homeOpenFileButton.setStyleSheet("""
        QWidget {
            border: 0.1px solid gray;
            background-color: rgb(173, 216, 230);
            padding-left: 0px;
            width: 33%;
            height: 200%;
            border-bottom-right-radius: 25px;
            border-top-right-radius: 25px;
            }
        """)

        self.homeAppText = QLabel("A easy way to create pretty LaTeX documents with great support for chemical molecules, chemical equations, mathematical symbols, tables, and other mathematical equations. Everything will be formatted appropriately in LaTeX, and the best part is you don't even need know LaTeX! This application will handle all the behind-the-scenes LaTeX using your convenient input. Add an element by simply clicking insert and choosing one of the input options. For equations, both mathematical and chemical, you have the choice of typing them out in natural language or uploading a picture of the handwritten [or digitally-drawn] equation. EzLaTeX will interpret the equation and translate it to LaTeX for you, dislaying a nice preview of what it will look like in the final PDF. If you wish to include a molecule diagram, simply select that option and type in the name of the molecule. EzLaTeX will handle the rest. ")
        self.homeAppText.setWordWrap(True)
        self.homeAppText.setStyleSheet("""
        QWidget {
            width: 75%;


        }

        """)
        self.homeAppText.setFont(QFont("Times", 24, QFont.Bold))

        self.homeFormattingVBox = QVBoxLayout(self)
        self.homeFormattingVBox.addWidget(self.homeAppText)
        self.homeFormattingVBox.addSpacing(50)

        self.homeVBox.addLayout(self.homeHBox)
        self.homeV2Box.addWidget(self.homeAppName)
        self.homeHBox.addSpacing(1)
        self.homeV2Box.addLayout(self.homeFormattingVBox)
        self.homeHBox.addLayout(self.homeV2Box)
        self.homeVBox.addLayout(self.homeH2Box)
        self.homeBox = QHBoxLayout(self)


        self.homeWidget = QWidget()
        self.homeWidget.setLayout(self.homeVBox)
        """
        END OF HOME PAGE UI
        """

        """
        START OF MAIN PAGE UI
        """
        self.mainVBox = QVBoxLayout(self)
        self.mainTabHBox = QHBoxLayout(self)

        self.mainHomeAction = QAction('&Home')
        self.mainHomeAction.triggered.connect(self.returnToMainScreen)

        self.mainExportAction = QAction('&Export')
        self.mainExportAction.triggered.connect(self.export)

        self.mainSaveAction = QAction('&Save')
        self.mainSaveAction.triggered.connect(self.saveFile)

        # self.mainFileMenuBar = QMenuBar()
        # self.mainFileMenu = self.mainFileMenuBar.addMenu('&File')
        # self.mainFileMenu.addAction(self.mainHomeAction)


        self.mainFileButton = QPushButton("File")
        self.mainFileButton.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        self.mainFileButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.mainFileButton.setMenu(QMenu(self.mainFileButton))
        self.mainFileButton.menu().addAction(self.mainHomeAction)
        self.mainFileButton.menu().addAction(self.mainSaveAction)
        self.mainFileButton.menu().addAction(self.mainExportAction)

        self.mainTypeMathAction = QAction('&Type in Equation')
        self.mainTypeMathAction.triggered.connect(self.typeMath)

        self.mainImageMathAction = QAction('&Image of Equation')
        self.mainImageMathAction.triggered.connect(self.imageMath)

        self.mainMoleculeAction = QAction('&Type in Molecule Name')
        self.mainMoleculeAction.triggered.connect(self.molecule)

        self.mainParagraphAction = QAction('&Paragraph Text')
        self.mainParagraphAction.triggered.connect(self.paragraph)

        self.mainSectionAction = QAction('&Section Header')
        self.mainSectionAction.triggered.connect(self.section)

        self.mainSubsectionAction = QAction('&Subsection Header')
        self.mainSubsectionAction.triggered.connect(self.subsection)

        self.mainInsertButton = QPushButton("Insert")
        self.mainInsertButton.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        self.mainInsertButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.mainInsertButton.setMenu(QMenu(self.mainInsertButton))
        self.mainInsertButton.menu().addAction(self.mainTypeMathAction)
        self.mainInsertButton.menu().addAction(self.mainImageMathAction)
        self.mainInsertButton.menu().addAction(self.mainMoleculeAction)
        self.mainInsertButton.menu().addAction(self.mainParagraphAction)
        self.mainInsertButton.menu().addAction(self.mainSectionAction)
        self.mainInsertButton.menu().addAction(self.mainSubsectionAction)
        # self.mainInsertButton.clicked.connect(self.insertElement)



        self.mainTabHBox.addWidget(self.mainFileButton)
        self.mainTabHBox.addWidget(self.mainInsertButton)
        self.mainTabHBox.addSpacing(1650)

        self.mainTabWidget = QWidget()
        self.mainTabWidget.setLayout(self.mainTabHBox)

        self.mainPreviewVBox = QVBoxLayout(self)
        self.mainPreviewWidget = QWidget()
        self.mainPreviewWidget.setLayout(self.mainPreviewVBox)
        self.mainPreviewWidget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.mainPreviewWidget.setStyleSheet("""
        QWidget {
            border: 0.5px solid gray;
            background-color: rgb(255, 255, 255);
            width: 100%;
            }
        """)
        self.mainScroll = QScrollArea()
        self.mainScroll.setWidget(self.mainPreviewWidget)
        self.mainScroll.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.mainScroll.setWidgetResizable(True)

        self.mainPageSimHBox = QHBoxLayout(self)
        self.mainPageSimHBox.addSpacing(200)
        self.mainPageSimHBox.addWidget(self.mainScroll)
        self.mainPageSimHBox.addSpacing(200)

        self.mainVBox.addWidget(self.mainTabWidget)
        # self.mainVBox.addSpacing(10)
        self.mainVBox.addLayout(self.mainPageSimHBox)

        # self.mainVBox.addSpacing()

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



app = QApplication(sys.argv)

window = MainWindow()
window.showMaximized()

app.exec_()
