import pandas as pd
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import QEventLoop, QTimer

class Ui_Historyadmin(object):
    
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(626, 442)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 626, 442))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("img/abstrait-bleu-clair-concept-innovation-medicale-modele-soins-sante-icone_44392-178.jpg"))
        self.label.setObjectName("label")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(125, 75, 350, 350))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.listWidget.setFont(font)
        self.listWidget.setObjectName("listWidget")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(144, 25, 325, 50))
        self.label_2.setStyleSheet("#label_2{\n"
"font: 75 28pt \"MS Sans Serif\";\n"
"    color: rgb(255, 255, 255);\n"
"}")
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "Recently Searched"))

###############################################################################

class Ui_History(object):
    
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(626, 442)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 626, 442))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("img/abstrait-bleu-clair-concept-innovation-medicale-modele-soins-sante-icone_44392-178.jpg"))
        self.label.setObjectName("label")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(100, 75, 400, 350))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.listWidget.setFont(font)
        self.listWidget.setObjectName("listWidget")
        self.listWidget.addItem("pain vomiting fever")
        self.listWidget.addItem("")
        self.listWidget.addItem("shortness of breath decreased body weight")
        self.listWidget.addItem("")
        self.listWidget.addItem("overweight fatigue")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(144, 25, 325, 50))
        self.label_2.setStyleSheet("#label_2{\n"
"font: 75 28pt \"MS Sans Serif\";\n"
"    color: rgb(255, 255, 255);\n"
"}")
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "Recently Searched"))

###############################################################################

class Ui_Result(object):
    
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(626, 442)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 626, 442))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("img/abstrait-bleu-clair-concept-innovation-medicale-modele-soins-sante-icone_44392-178.jpg"))
        self.label.setObjectName("label")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(100, 75, 425, 350))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.listWidget.setFont(font)
        self.listWidget.setObjectName("listWidget")
        self.listWidget.addItem("adhesion: 0.62254")
        self.listWidget.addItem("")
        self.listWidget.addItem("acquired-immuno-deficiency syndrome: 0.58522")
        self.listWidget.addItem("")
        self.listWidget.addItem("deshydratation: 0.35465")
        self.listWidget.addItem("")
        self.listWidget.addItem("decubitus ulcer: 0.28845")
        self.listWidget.addItem("")
        self.listWidget.addItem("delirium: 0.24365")
    
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(166, 25, 275, 50))
        self.label_2.setStyleSheet("#label_2{\n"
"font: 75 28pt \"MS Sans Serif\";\n"
"    color: rgb(255, 255, 255);\n"
"}")
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "Search\'s Result"))
        
##############################################################################        

class Ui_AdDoc(object):
    
    def initUI(self):
        filePaths = QtWidgets.QFileDialog.getOpenFileNames(None, 
                                                       'Multiple File',
                                                       r"C:/Users/asus/pcd2019/.spyproject/important/disease",
                                                      '*.txt')
        for filePath in filePaths:
            print('filePath',filePath, '\n')
            fileHandle = open(filePath, 'r')
            lines = fileHandle.readlines()
            for line in lines:
                print(line)
    
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(626, 442)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 626, 442))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("img/abstrait-bleu-clair-concept-innovation-medicale-modele-soins-sante-icone_44392-178.jpg"))
        self.label.setObjectName("label")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(50, 50, 525, 325))
        self.frame.setStyleSheet("#frame{\n"
"background:rgba(0,0,0,0.8);\n"
"border-radius:15px;\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(90, 175, 350, 50))
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setStyleSheet("#pushButton{\n"
"background-color: rgb(85, 170, 255);\n"
"border-radius:15px;\n"
"font: 75 15pt \"MS Sans Serif\";\n"
"color:rgb(255, 255, 255);\n"
"}")
        self.pushButton.setAutoDefault(True)
        self.pushButton.setDefault(False)
        self.pushButton.setFlat(False)
        self.pushButton.setObjectName("pushButton")
        
        self.pushButton.clicked.connect(self.initUI)
        
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(133, 25, 300, 50))
        self.label_2.setStyleSheet("#label_2{\n"
"font: 75 28pt \"MS Sans Serif\";\n"
"    color: rgb(255, 255, 255);\n"
"}")
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setGeometry(QtCore.QRect(100, 100, 333, 50))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("#lineEdit{\n"
"font: 75 15pt \"MS Sans Serif\";\n"
"}")
        self.lineEdit.setInputMask("")
        self.lineEdit.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(90, 250, 350, 50))
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_2.setStyleSheet("#pushButton{\n"
"background-color: rgb(85, 170, 255);\n"
"border-radius:15px;\n"
"font: 75 15pt \"MS Sans Serif\";\n"
"color:rgb(255, 255, 255);\n"
"}\n"
"#pushButton_2{\n"
"background-color: rgb(85, 170, 255);\n"
"border-radius:15px;\n"
"font: 75 15pt \"MS Sans Serif\";\n"
"color:rgb(255, 255, 255);\n"
"}")
        self.pushButton_2.setAutoDefault(True)
        self.pushButton_2.setDefault(False)
        self.pushButton_2.setFlat(False)
        self.pushButton_2.setObjectName("pushButton_2")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Choose File"))
        self.label_2.setText(_translate("MainWindow", "Add Documents"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "Document\'s Name"))
        self.pushButton_2.setText(_translate("MainWindow", "Validate"))
        self.pushButton_2.setShortcut(_translate("MainWindow", "Return"))

###############################################################################

class Ui_ListDoc(object):
    
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(626, 442)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(175, 0, 251, 442))
        self.tableWidget.setRowCount(137)
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setObjectName("tableWidget")
        
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 0, item)
        for x in range(1, 137):
            item = QtWidgets.QTableWidgetItem()
            self.tableWidget.setItem(x, 0, item)
            item = QtWidgets.QTableWidgetItem()
            self.tableWidget.setItem(x, 1, item)
            
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 626, 442))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("img/abstrait-bleu-clair-concept-innovation-medicale-modele-soins-sante-icone_44392-178.jpg"))
        self.label.setObjectName("label")
        self.label.raise_()
        self.tableWidget.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.item(0, 0)
        item.setText(_translate("MainWindow", "Disease"))
        item = self.tableWidget.item(0, 1)
        item.setText(_translate("MainWindow", "Symptoms"))
            
        file_errors_location = r'important/doc.xlsx'
        df = pd.read_excel(file_errors_location)
        l=[]
        li=[]
        for x in range(137):
            l.append(df["Disease"][x])
            li.append(df["Symptoms"][x])
            item = self.tableWidget.item(x, 0)
            item.setText(_translate("MainWindow", l[x]))
            item = self.tableWidget.item(x, 1)
            item.setText(_translate("MainWindow", li[x]))
            
        self.tableWidget.setSortingEnabled(__sortingEnabled)

###############################################################################

class Ui_Admin(object):
    
    def result(self):
        MainWindow = QtWidgets.QMainWindow()
        ui = Ui_Result()
        ui.setupUi(MainWindow)
        MainWindow.show()
        MainWindow.exec_()
    
    def hisTry(self):
        MainWindow = QtWidgets.QMainWindow()
        ui = Ui_Historyadmin()
        ui.setupUi(MainWindow)
        MainWindow.show()
        MainWindow.exec_()

    def add_Doc(self):
        MainWindow = QtWidgets.QMainWindow()
        ui = Ui_AdDoc()
        ui.setupUi(MainWindow)
        MainWindow.show()
        MainWindow.exec_()
        
    def listDoc(self):
        MainWindow = QtWidgets.QMainWindow()
        ui = Ui_ListDoc()
        ui.setupUi(MainWindow)
        MainWindow.show()
        MainWindow.exec_()
        
    def goUser(self):
        MainWindow = QtWidgets.QMainWindow()
        ui = Ui_Gui()
        ui.setupUi(MainWindow)
        MainWindow.show()
        MainWindow.exec_()
        
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(603, 425)
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(50, 325, 500, 37))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        self.lineEdit.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(16)
        font.setItalic(False)
        self.lineEdit.setFont(font)
        self.lineEdit.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.lineEdit.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.lineEdit.setStatusTip("")
        self.lineEdit.setWhatsThis("")
        self.lineEdit.setAutoFillBackground(False)
        self.lineEdit.setInputMask("")
        self.lineEdit.setText("")
        self.lineEdit.setFrame(False)
        self.lineEdit.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(550, 325, 37, 37))
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/téléchargement (2).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QtCore.QSize(37, 37))
        self.pushButton.setAutoDefault(False)
        self.pushButton.setDefault(False)
        self.pushButton.setFlat(False)
        self.pushButton.setObjectName("pushButton")
        
        self.pushButton.clicked.connect(self.result)
        
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 603, 425))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("img/Annotation.jpg"))
        self.label.setObjectName("label")
        self.commandLinkButton = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.commandLinkButton.setGeometry(QtCore.QRect(310, 240, 111, 41))
        self.commandLinkButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("img/bfa_sign-out_flat-circle-white-on-ios-blue-gradient_512x512.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.commandLinkButton.setIcon(icon1)
        self.commandLinkButton.setIconSize(QtCore.QSize(25, 25))
        self.commandLinkButton.setDefault(False)
        self.commandLinkButton.setDescription("")
        self.commandLinkButton.setObjectName("commandLinkButton")
        
        self.commandLinkButton.clicked.connect(self.goUser)
        
        self.commandLinkButton_2 = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.commandLinkButton_2.setGeometry(QtCore.QRect(280, 200, 141, 41))
        self.commandLinkButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("img/About-Us-Web-Icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.commandLinkButton_2.setIcon(icon2)
        self.commandLinkButton_2.setIconSize(QtCore.QSize(25, 25))
        self.commandLinkButton_2.setObjectName("commandLinkButton_2")
        
        self.commandLinkButton_2.clicked.connect(self.hisTry)
        
        self.commandLinkButton_3 = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.commandLinkButton_3.setGeometry(QtCore.QRect(250, 160, 171, 41))
        self.commandLinkButton_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("img/images (3).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.commandLinkButton_3.setIcon(icon3)
        self.commandLinkButton_3.setIconSize(QtCore.QSize(25, 25))
        self.commandLinkButton_3.setObjectName("commandLinkButton_3")
        
        self.commandLinkButton_3.clicked.connect(self. add_Doc)
        
        self.commandLinkButton_4 = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.commandLinkButton_4.setGeometry(QtCore.QRect(220, 120, 201, 41))
        self.commandLinkButton_4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("img/images (4).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.commandLinkButton_4.setIcon(icon4)
        self.commandLinkButton_4.setIconSize(QtCore.QSize(25, 25))
        self.commandLinkButton_4.setObjectName("commandLinkButton_4")
        
        self.commandLinkButton_4.clicked.connect(self.listDoc)
        
        self.label.raise_()
        self.lineEdit.raise_()
        self.pushButton.raise_()
        self.commandLinkButton.raise_()
        self.commandLinkButton_2.raise_()
        self.commandLinkButton_3.raise_()
        self.commandLinkButton_4.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "Symptoms"))
        self.pushButton.setShortcut(_translate("MainWindow", "Return"))
        self.commandLinkButton.setText(_translate("MainWindow", "Sign Out"))
        self.commandLinkButton_2.setText(_translate("MainWindow", "History"))
        self.commandLinkButton_3.setText(_translate("MainWindow", "Add Documents"))
        self.commandLinkButton_4.setText(_translate("MainWindow", "Documents\' List"))

###############################################################################

class Ui_Password(object):
    
    def generate(self):
        passw = self.lineEdit.text()
        if str(passw) == "bouthainabir":
            self.pushButton.clicked.connect(self.goAdmin)
        else:
            msgBox = QMessageBox()
            msgBox.setText("Password incorrect")
            msgBox.setWindowTitle("Error")
            msgBox.exec_()

    def goAdmin(self):
        MainWindow = QtWidgets.QMainWindow()
        ui = Ui_Admin()
        ui.setupUi(MainWindow)
        MainWindow.show()
        MainWindow.exec_()
    
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(626, 442)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 626, 442))
        self.label.setStyleSheet("QFrame{\n"
"background:#fff;\n"
"}")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("img/abstrait-bleu-clair-concept-innovation-medicale-modele-soins-sante-icone_44392-178.jpg"))
        self.label.setObjectName("label")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(50, 50, 525, 325))
        self.frame.setStyleSheet("#frame{\n"
"background:rgba(0,0,0,0.8);\n"
"border-radius:15px;\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(95, 250, 350, 50))
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setStyleSheet("#pushButton{\n"
"background-color: rgb(85, 170, 255);\n"
"border-radius:15px;\n"
"font: 75 15pt \"MS Sans Serif\";\n"
"color:rgb(255, 255, 255);\n"
"}")
        self.pushButton.setAutoDefault(True)
        self.pushButton.setDefault(False)
        self.pushButton.setFlat(False)
        self.pushButton.setObjectName("pushButton")
        
        self.pushButton.clicked.connect(self.generate)
        
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(100, 25, 350, 50))
        self.label_2.setStyleSheet("#label_2{\n"
"font: 75 28pt \"MS Sans Serif\";\n"
"    color: rgb(255, 255, 255);\n"
"}")
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setGeometry(QtCore.QRect(100, 125, 333, 50))
        self.lineEdit.setStyleSheet("#lineEdit{\n"
"font: 75 15pt \"MS Sans Serif\";\n"
"}")
        self.lineEdit.setInputMask("")
        self.lineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit.setObjectName("lineEdit")        
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Log In"))
        self.pushButton.setShortcut(_translate("MainWindow", "Return"))
        self.label_2.setText(_translate("MainWindow", "Administrator Space"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "Password"))
        
###############################################################################

class Ui_Gui(object):
    
    def clickMethod(self):
        print(self.lineEdit.text())
    
    def result(self):
        MainWindow = QtWidgets.QMainWindow()
        ui = Ui_Result()
        ui.setupUi(MainWindow)
        loop = QEventLoop()
        QTimer.singleShot(5000, loop.quit)
        loop.exec_()
        MainWindow.show()
        MainWindow.exec_()
    
    def histOry(self):
        MainWindow = QtWidgets.QMainWindow()
        ui = Ui_History()
        ui.setupUi(MainWindow)
        MainWindow.show()
        MainWindow.exec_()
    
    def generate_report(self):
        data_line = self.lineEdit.displayText()
        print(data_line)
    
    def signIn(self):
        MainWindow = QtWidgets.QMainWindow()
        ui = Ui_Password()
        ui.setupUi(MainWindow)
        MainWindow.show()
        MainWindow.exec_()
    
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(603, 426)
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(50, 325, 500, 37))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        self.lineEdit.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(16)
        font.setItalic(False)
        self.lineEdit.setFont(font)
        self.lineEdit.setText("")
        self.lineEdit.setFrame(False)
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setEnabled(True)
        self.pushButton.setGeometry(QtCore.QRect(550, 325, 37, 37))
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setText("")
        
        self.pushButton.clicked.connect(self.generate_report)
        
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/téléchargement (2).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QtCore.QSize(37, 37))
        self.pushButton.setObjectName("pushButton")
        
        self.pushButton.clicked.connect(self.result)
        
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 603, 426))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("img/both.jpg"))
        self.label.setObjectName("label")
        self.commandLinkButton = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.commandLinkButton.setGeometry(QtCore.QRect(300, 180, 121, 41))
        self.commandLinkButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("img/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.commandLinkButton.setIcon(icon1)
        self.commandLinkButton.setIconSize(QtCore.QSize(27, 27))
        self.commandLinkButton.setObjectName("commandLinkButton")
        
        self.commandLinkButton.clicked.connect(self.signIn)
        
        self.commandLinkButton_2 = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.commandLinkButton_2.setGeometry(QtCore.QRect(300, 220, 121, 41))
        self.commandLinkButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("img/About-Us-Web-Icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.commandLinkButton_2.setIcon(icon2)
        self.commandLinkButton_2.setIconSize(QtCore.QSize(25, 25))
        self.commandLinkButton_2.setObjectName("commandLinkButton_2")
        
        self.commandLinkButton_2.clicked.connect(self.histOry)
        self.commandLinkButton_2.clicked.connect(self.clickMethod)
        
        self.label.raise_()
        self.lineEdit.raise_()
        self.pushButton.raise_()
        self.commandLinkButton.raise_()
        self.commandLinkButton_2.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "Symptoms"))
        self.pushButton.setShortcut(_translate("MainWindow", "Return"))
        self.commandLinkButton.setText(_translate("MainWindow", "Sign In"))
        self.commandLinkButton_2.setText(_translate("MainWindow", "History"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Gui()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())