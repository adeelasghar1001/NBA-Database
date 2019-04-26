# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Adeel Asghar\Desktop\thingy.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

import pandas as pd
global df
global value, value2

class Ui_MainWindow(object):        
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(493, 200)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setEnabled(True)
        self.label.setGeometry(QtCore.QRect(10, 10, 311, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 70, 161, 22))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.teamName = QtWidgets.QLineEdit(self.centralwidget)
        self.teamName.setGeometry(QtCore.QRect(170, 70, 113, 22))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.teamName.setFont(font)
        self.teamName.setObjectName("teamName")
        self.submitButton = QtWidgets.QPushButton(self.centralwidget)
        self.submitButton.setGeometry(QtCore.QRect(290, 68, 93, 25))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.submitButton.setFont(font)
        self.submitButton.setObjectName("submitButton")

        self.submitButton.clicked.connect(self.openWindow)
        
        self.incorrectLabel = QtWidgets.QLabel(self.centralwidget)
        self.incorrectLabel.hide()
        self.incorrectLabel.setGeometry(QtCore.QRect(10, 130, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.incorrectLabel.setFont(font)
        self.incorrectLabel.setObjectName("incorrectLabel")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 493, 26))
        self.menubar.setObjectName("menubar")
        self.menuNBA_Database = QtWidgets.QMenu(self.menubar)
        self.menuNBA_Database.setObjectName("menuNBA_Database")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuNBA_Database.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "NBA Database 2017-2018"))
        self.label_2.setText(_translate("MainWindow", "Enter a team name:"))
        self.submitButton.setText(_translate("MainWindow", "Submit"))
        self.incorrectLabel.setText(_translate("MainWindow", "Please enter a valid team!"))
        self.menuNBA_Database.setTitle(_translate("MainWindow", "NBA Database"))

    def openWindow(self):
        self.incorrectLabel.hide()
        global value,value2
        global df
        value = self.teamName.text()
        if 'Denver' in value:
            self.incorrectLabel.hide()

            try:
                df = pd.read_excel("NBA TEAMS//Denver.xlsx")
            except:
                print("File not found")

            value2="Denver"
            self.window = QtWidgets.QMainWindow()
            self.ui = Ui_page2()
            self.ui.setupUi(self.window)
            self.window.show()
            self.incorrectLabel.hide()
        elif 'Portland' in value:
            self.incorrectLabel.hide()

            try:
                df = pd.read_excel("NBA TEAMS//Portland.xlsx")   
            except:
                print("File not found")

            value2="Portland"
            self.window = QtWidgets.QMainWindow()
            self.ui = Ui_page2()
            self.ui.setupUi(self.window)
            self.window.show()
        elif 'Utah' in value:
            self.incorrectLabel.hide()
            df = pd.read_excel("NBA TEAMS//Utah.xlsx")
            value2="Utah"
            self.window = QtWidgets.QMainWindow()
            self.ui = Ui_page2()
            self.ui.setupUi(self.window)
            self.window.show()
        elif 'Oklahoma' in value:
            self.incorrectLabel.hide()
            df = pd.read_excel("NBA TEAMS//Oklahoma.xlsx")   
            value2="Oklahoma"
            self.window = QtWidgets.QMainWindow()
            self.ui = Ui_page2()
            self.ui.setupUi(self.window)
            self.window.show()
        elif 'Minnesota' in value:
            self.incorrectLabel.hide()
            df = pd.read_excel("NBA TEAMS//Minnesota.xlsx") 
            value2="Minnesota"
            self.window = QtWidgets.QMainWindow()
            self.ui = Ui_page2()
            self.ui.setupUi(self.window)
            self.window.show()

        elif 'Atlanta' in value:
            self.incorrectLabel.hide()
            df = pd.read_excel("NBA TEAMS//Atlanta.xlsx") 
            value2="Atlanta"
            self.window = QtWidgets.QMainWindow()
            self.ui = Ui_page2()
            self.ui.setupUi(self.window)
            self.window.show()
        elif 'Boston' in value:
            self.incorrectLabel.hide()
            df = pd.read_excel("NBA TEAMS//Boston.xlsx") 
            value2="Boston"
            self.window = QtWidgets.QMainWindow()
            self.ui = Ui_page2()
            self.ui.setupUi(self.window)
            self.window.show()
        elif 'Brooklyn' in value:
            self.incorrectLabel.hide()
            df = pd.read_excel("NBA TEAMS//Brooklyn.xlsx") 
            value2="Brooklyn"
            self.window = QtWidgets.QMainWindow()
            self.ui = Ui_page2()
            self.ui.setupUi(self.window)
            self.window.show()
        elif 'Charlotte' in value:
            self.incorrectLabel.hide()
            df = pd.read_excel("NBA TEAMS//Charlotte.xlsx") 
            value2="Charlotte"
            self.window = QtWidgets.QMainWindow()
            self.ui = Ui_page2()
            self.ui.setupUi(self.window)
            self.window.show()
        elif 'Chicago' in value:
            self.incorrectLabel.hide()
            df = pd.read_excel("NBA TEAMS//Chicago.xlsx") 
            value2="Chicago"
            self.window = QtWidgets.QMainWindow()
            self.ui = Ui_page2()
            self.ui.setupUi(self.window)
            self.window.show()
        elif 'Cleveland' in value:
            self.incorrectLabel.hide()
            df = pd.read_excel("NBA TEAMS//Cleveland.xlsx") 
            value2="Cleveland"
            self.window = QtWidgets.QMainWindow()
            self.ui = Ui_page2()
            self.ui.setupUi(self.window)
            self.window.show()
        elif 'Dallas' in value:
            self.incorrectLabel.hide()
            df = pd.read_excel("NBA TEAMS//Dallas.xlsx") 
            value2="Dallas"
            self.window = QtWidgets.QMainWindow()
            self.ui = Ui_page2()
            self.ui.setupUi(self.window)
            self.window.show()
        elif 'Detroit' in value:
            self.incorrectLabel.hide()
            df = pd.read_excel("NBA TEAMS//Detroit.xlsx") 
            value2="Detroit"
            self.window = QtWidgets.QMainWindow()
            self.ui = Ui_page2()
            self.ui.setupUi(self.window)
            self.window.show()
        elif 'Golden State' in value:
            self.incorrectLabel.hide()
            df = pd.read_excel("NBA TEAMS//GoldenState.xlsx") 
            value2="Golden State"
            self.window = QtWidgets.QMainWindow()
            self.ui = Ui_page2()
            self.ui.setupUi(self.window)
            self.window.show()
        elif 'Houston' in value:
            self.incorrectLabel.hide()
            df = pd.read_excel("NBA TEAMS//Houston.xlsx") 
            value2="Houston"
            self.window = QtWidgets.QMainWindow()
            self.ui = Ui_page2()
            self.ui.setupUi(self.window)
            self.window.show()
        elif 'Indiana' in value:
            self.incorrectLabel.hide()
            df = pd.read_excel("NBA TEAMS//Indiana.xlsx") 
            value2="Indiana"
            self.window = QtWidgets.QMainWindow()
            self.ui = Ui_page2()
            self.ui.setupUi(self.window)
            self.window.show()
        elif 'Los Angeles Clippers' in value:
            self.incorrectLabel.hide()
            df = pd.read_excel("NBA TEAMS//LosAngelesClippers1.xlsx") 
            value2="Los Angeles Clippers"
            self.window = QtWidgets.QMainWindow()
            self.ui = Ui_page2()
            self.ui.setupUi(self.window)
            self.window.show()
        elif 'Los Angeles Lakers' in value:
            self.incorrectLabel.hide()
            df = pd.read_excel("NBA TEAMS//LosAngelesLakers1.xlsx") 
            value2="Los Angeles Lakers"
            self.window = QtWidgets.QMainWindow()
            self.ui = Ui_page2()
            self.ui.setupUi(self.window)
            self.window.show()
        elif 'Memphis' in value:
            self.incorrectLabel.hide()
            df = pd.read_excel("NBA TEAMS//Memphis.xlsx") 
            value2="Memphis"
            self.window = QtWidgets.QMainWindow()
            self.ui = Ui_page2()
            self.ui.setupUi(self.window)
            self.window.show()
        elif 'Miami' in value:
            self.incorrectLabel.hide()
            df = pd.read_excel("NBA TEAMS//Miami.xlsx") 
            value2="Miami"
            self.window = QtWidgets.QMainWindow()
            self.ui = Ui_page2()
            self.ui.setupUi(self.window)
            self.window.show()
        elif 'Milwaukee' in value:
            self.incorrectLabel.hide()
            df = pd.read_excel("NBA TEAMS//Milwaukee.xlsx") 
            value2="Milwaukee"
            self.window = QtWidgets.QMainWindow()
            self.ui = Ui_page2()
            self.ui.setupUi(self.window)
            self.window.show()
        elif 'New Orleans' in value:
            self.incorrectLabel.hide()
            df = pd.read_excel("NBA TEAMS//NewOrleans.xlsx") 
            value2="New Orleans"
            self.window = QtWidgets.QMainWindow()
            self.ui = Ui_page2()
            self.ui.setupUi(self.window)
            self.window.show()
        elif 'New York' in value:
            self.incorrectLabel.hide()
            df = pd.read_excel("NBA TEAMS//NewYork.xlsx") 
            value2="New York"
            self.window = QtWidgets.QMainWindow()
            self.ui = Ui_page2()
            self.ui.setupUi(self.window)
            self.window.show()
        elif 'Orlando' in value:
            self.incorrectLabel.hide()
            df = pd.read_excel("NBA TEAMS//Orlando.xlsx") 
            value2="Orlando"
            self.window = QtWidgets.QMainWindow()
            self.ui = Ui_page2()
            self.ui.setupUi(self.window)
            self.window.show()
        elif 'Phoenix' in value:
            self.incorrectLabel.hide()
            df = pd.read_excel("NBA TEAMS//Pheonix.xlsx") 
            value2="Phoenix"
            self.window = QtWidgets.QMainWindow()
            self.ui = Ui_page2()
            self.ui.setupUi(self.window)
            self.window.show()
        elif 'Philadelphia' in value:
            self.incorrectLabel.hide()
            df = pd.read_excel("NBA TEAMS//Philadelphia.xlsx") 
            value2="Philadelphia"
            self.window = QtWidgets.QMainWindow()
            self.ui = Ui_page2()
            self.ui.setupUi(self.window)
            self.window.show()
        elif 'Sacramento' in value:
            self.incorrectLabel.hide()
            df = pd.read_excel("NBA TEAMS//Sacramento.xlsx") 
            value2="Sacramento"
            self.window = QtWidgets.QMainWindow()
            self.ui = Ui_page2()
            self.ui.setupUi(self.window)
            self.window.show()
        elif 'San Antonio' in value:
            self.incorrectLabel.hide()
            df = pd.read_excel("NBA TEAMS//SanAntonio.xlsx") 
            value2="San Antonio"
            self.window = QtWidgets.QMainWindow()
            self.ui = Ui_page2()
            self.ui.setupUi(self.window)
            self.window.show()
        elif 'Toronto' in value:
            self.incorrectLabel.hide()
            df = pd.read_excel("NBA TEAMS//Toronto.xlsx") 
            value2="Toronto"
            self.window = QtWidgets.QMainWindow()
            self.ui = Ui_page2()
            self.ui.setupUi(self.window)
            self.window.show()
        elif 'Washington' in value:
            self.incorrectLabel.hide()
            df = pd.read_excel("NBA TEAMS//Washington.xlsx") 
            value2="Washington"
            self.window = QtWidgets.QMainWindow()
            self.ui = Ui_page2()
            self.ui.setupUi(self.window)
            self.window.show()
   
        else:
            self.incorrectLabel.show()


class Ui_page2(object):

    def resetTable(self):
        model = PandasModel(df)
        self.tableView.setModel(model)
        self.tableView.resizeColumnsToContents()

    def setupUi(self, page2):     
        page2.setObjectName("page2")
        page2.resize(965, 661)
        self.teamLabel = QtWidgets.QLabel(page2)
        self.teamLabel.setGeometry(QtCore.QRect(20, 20, 181, 21))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.teamLabel.setFont(font)
        self.teamLabel.setObjectName("teamLabel")

        global rk 
        rk=10

        self.addPlayerBtn = QtWidgets.QPushButton(page2)
        self.addPlayerBtn.setGeometry(QtCore.QRect(20, 280, 221, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.addPlayerBtn.setFont(font)
        self.addPlayerBtn.setObjectName("addPlayerBtn")
        self.removePlayerBtn = QtWidgets.QPushButton(page2)
        self.removePlayerBtn.setGeometry(QtCore.QRect(20, 400, 221, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.removePlayerBtn.setFont(font)
        self.removePlayerBtn.setObjectName("removePlayerBtn")
        self.editPlayerByn = QtWidgets.QPushButton(page2)
        self.editPlayerByn.setGeometry(QtCore.QRect(20, 580, 221, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.editPlayerByn.setFont(font)
        self.editPlayerByn.setObjectName("editPlayerByn")

        self.tableView = QtWidgets.QTableView(page2)
        self.tableView.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tableView.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tableView.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tableView.setGeometry(QtCore.QRect(260, 57, 500, 450))
        self.tableView.setShowGrid(True)
        self.tableView.setSortingEnabled(True)
        
        self.tableView.setObjectName("tableView")
            
        model = PandasModel(df)
        self.tableView.setModel(model)
        self.tableView.resizeColumnsToContents()


        self.removePlayerEdit = QtWidgets.QLineEdit(page2)
        self.removePlayerEdit.setGeometry(QtCore.QRect(144, 368, 96, 25))
        font = QtGui.QFont()
        font.setPointSize(12)        
        self.removePlayerEdit.setFont(font)
        self.removePlayerEdit.setObjectName("removePlayerEdit")
        
        self.nameEdit = QtWidgets.QLineEdit(page2)
        self.nameEdit.setGeometry(QtCore.QRect(130, 70, 111, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.nameEdit.setFont(font)
        self.nameEdit.setObjectName("nameEdit")
        self.label = QtWidgets.QLabel(page2)
        self.label.setGeometry(QtCore.QRect(12, 75, 111, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.reboundsEdit = QtWidgets.QLineEdit(page2)
        self.reboundsEdit.setGeometry(QtCore.QRect(130, 100, 111, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.reboundsEdit.setFont(font)
        self.reboundsEdit.setObjectName("reboundsEdit")
        self.assistsEdit = QtWidgets.QLineEdit(page2)
        self.assistsEdit.setGeometry(QtCore.QRect(130, 130, 111, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.assistsEdit.setFont(font)
        self.assistsEdit.setObjectName("assistsEdit")
        self.label_2 = QtWidgets.QLabel(page2)
        self.label_2.setGeometry(QtCore.QRect(20, 105, 101, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(page2)
        self.label_3.setGeometry(QtCore.QRect(20, 135, 101, 20))
        font = QtGui.QFont()
        font.setPointSize(11)

        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(page2)
        self.label_4.setGeometry(QtCore.QRect(20, 165, 101, 20))
        font = QtGui.QFont()
        font.setPointSize(11)

        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.stealsEdit = QtWidgets.QLineEdit(page2)
        self.stealsEdit.setGeometry(QtCore.QRect(130, 160, 111, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.stealsEdit.setFont(font)
        self.stealsEdit.setObjectName("stealsEdit")
        self.label_5 = QtWidgets.QLabel(page2)
        self.label_5.setGeometry(QtCore.QRect(20, 195, 101, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.blocksEdit = QtWidgets.QLineEdit(page2)
        self.blocksEdit.setGeometry(QtCore.QRect(130, 190, 111, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.blocksEdit.setFont(font)
        self.blocksEdit.setObjectName("blocksEdit")
        self.TurnoversEdit = QtWidgets.QLineEdit(page2)
        self.TurnoversEdit.setGeometry(QtCore.QRect(130, 220, 111, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.TurnoversEdit.setFont(font)
        self.TurnoversEdit.setObjectName("TurnoversEdit")
 
        self.label_6 = QtWidgets.QLabel(page2)
        self.label_6.setGeometry(QtCore.QRect(20, 225, 101, 20))
        font = QtGui.QFont()
        font.setPointSize(11)

        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(page2)
        self.label_7.setGeometry(QtCore.QRect(20, 255, 101, 20))
        font = QtGui.QFont()
        font.setPointSize(11)

        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_7.setObjectName("label_7")
        self.pointsEdit = QtWidgets.QLineEdit(page2)
        self.pointsEdit.setGeometry(QtCore.QRect(130, 250, 111, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pointsEdit.setFont(font)
        self.pointsEdit.setObjectName("pointsEdit")

        self.line = QtWidgets.QFrame(page2)
        self.line.setGeometry(QtCore.QRect(10, 321, 236, 16))
        self.line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line.setLineWidth(3)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setObjectName("line")


        self.line_2 = QtWidgets.QFrame(page2)
        self.line_2.setGeometry(QtCore.QRect(237, 60, 21, 271))
        self.line_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_2.setLineWidth(3)
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(page2)
        self.line_3.setGeometry(QtCore.QRect(1, 60, 21, 271))
        self.line_3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_3.setLineWidth(3)
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setObjectName("line_3")
        self.line_4 = QtWidgets.QFrame(page2)
        self.line_4.setGeometry(QtCore.QRect(10, 50, 239, 16))
        self.line_4.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_4.setLineWidth(3)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setObjectName("line_4")
        self.line_5 = QtWidgets.QFrame(page2)
        self.line_5.setGeometry(QtCore.QRect(10, 442, 238, 16))
        self.line_5.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_5.setLineWidth(3)
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setObjectName("line_5")
        self.label_8 = QtWidgets.QLabel(page2)
        self.label_8.setGeometry(QtCore.QRect(20, 370, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.line_6 = QtWidgets.QFrame(page2)
        self.line_6.setGeometry(QtCore.QRect(1, 360, 21, 91))
        self.line_6.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_6.setLineWidth(3)
        self.line_6.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_6.setObjectName("line_6")
        self.line_7 = QtWidgets.QFrame(page2)
        self.line_7.setGeometry(QtCore.QRect(237, 358, 21, 94))
        self.line_7.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_7.setLineWidth(3)
        self.line_7.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_7.setObjectName("line_7")
        self.line_8 = QtWidgets.QFrame(page2)
        self.line_8.setGeometry(QtCore.QRect(10, 350, 238, 16))
        self.line_8.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_8.setLineWidth(3)
        self.line_8.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_8.setObjectName("line_8")

        self.label_9 = QtWidgets.QLabel(page2)
        self.label_9.setGeometry(QtCore.QRect(20, 555, 101, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_9.setFont(font)
        self.label_9.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_9.setObjectName("label_9")
        self.playernameEdit = QtWidgets.QLineEdit(page2)
        self.playernameEdit.setGeometry(QtCore.QRect(130, 490, 111, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.typeofEdit = QtWidgets.QLineEdit(page2)
        self.typeofEdit.setGeometry(QtCore.QRect(130, 520, 111, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.typeofEdit.setFont(font)
        self.typeofEdit.setObjectName("typeofEdit")
        self.playernameEdit.setFont(font)
        self.playernameEdit.setObjectName("playernameEdit")
        self.assistsEdit_2 = QtWidgets.QLineEdit(page2)
        self.assistsEdit_2.setGeometry(QtCore.QRect(130, 550, 111, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.assistsEdit_2.setFont(font)
        self.assistsEdit_2.setObjectName("assistsEdit_2")
        self.label_10 = QtWidgets.QLabel(page2)
        self.label_10.setGeometry(QtCore.QRect(20, 525, 101, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_10.setFont(font)
        self.label_10.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(page2)
        self.label_11.setGeometry(QtCore.QRect(12, 495, 111, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_11.setFont(font)
        self.label_11.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_11.setObjectName("label_11")
        
        self.line_9 = QtWidgets.QFrame(page2)
        self.line_9.setGeometry(QtCore.QRect(1, 480, 21, 151))
        self.line_9.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_9.setLineWidth(3)
        self.line_9.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_9.setObjectName("line_9")
        self.line_10 = QtWidgets.QFrame(page2)
        self.line_10.setGeometry(QtCore.QRect(10, 470, 238, 16))
        self.line_10.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_10.setLineWidth(3)
        self.line_10.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_10.setObjectName("line_10")
        self.line_11 = QtWidgets.QFrame(page2)
        self.line_11.setGeometry(QtCore.QRect(10, 621, 238, 16))
        self.line_11.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_11.setLineWidth(3)
        self.line_11.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_11.setObjectName("line_11")
        self.line_12 = QtWidgets.QFrame(page2)
        self.line_12.setGeometry(QtCore.QRect(237, 477, 21, 153))
        self.line_12.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_12.setLineWidth(3)
        self.line_12.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_12.setObjectName("line_12")

        self.line.setStyleSheet("color:grey")
        self.line_2.setStyleSheet("color:grey")
        self.line_3.setStyleSheet("color:grey")
        self.line_4.setStyleSheet("color:grey")
        self.line_5.setStyleSheet("color:grey")
        self.line_6.setStyleSheet("color:grey")
        self.line_7.setStyleSheet("color:grey")
        self.line_8.setStyleSheet("color:grey")
        self.line_9.setStyleSheet("color:grey")
        self.line_10.setStyleSheet("color:grey")
        self.line_11.setStyleSheet("color:grey")
        self.line_12.setStyleSheet("color:grey")

        self.removePlayerBtn.clicked.connect(self.DeletePlayer)
        self.addPlayerBtn.clicked.connect(self.AddPlayer)
        self.editPlayerByn.clicked.connect(self.EditPlayer)
        self.retranslateUi(page2)
        QtCore.QMetaObject.connectSlotsByName(page2)


    def DeletePlayer(self):
        global value2
        print(value2)
        global df
        print(df.shape[0])
        choose = int(self.removePlayerEdit.text())
        if choose<(df.shape[0]):
            df=df.drop([choose])
            self.tableView.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
            self.tableView.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
            self.tableView.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
            self.tableView.setGeometry(QtCore.QRect(260, 57, 500, 500))
            self.tableView.setShowGrid(True)
            self.tableView.setSortingEnabled(True)
        
            df.to_excel("NBA TEAMS//" + value2 + ".xlsx", engine='xlsxwriter', index=False)
            df = pd.read_excel("NBA TEAMS//" +value2+".xlsx")
            model = PandasModel(df)
            self.tableView.setModel(model)
            self.tableView.resizeColumnsToContents()
        else:
            print("Out of range")


    def AddPlayer(self):
        global df
        rk=df.shape[0]
        i1 = self.nameEdit.text()
        i2 = int(self.reboundsEdit.text())
        i3 = int(self.assistsEdit.text())
        i4 = int(self.stealsEdit.text())
        i5 = int(self.blocksEdit.text())
        i6 = int(self.TurnoversEdit.text())
        i7 = int(self.pointsEdit.text())
        df.loc[rk] = [i1, i2, i3, i4, i5, i6, i7]
        
        df.to_excel("NBA TEAMS//" + value2 + ".xlsx", engine='xlsxwriter', index=False)
        df = pd.read_excel("NBA TEAMS//" +value2+".xlsx")
        model = PandasModel(df)
        self.tableView.setModel(model)
        self.tableView.resizeColumnsToContents()
        print(df)
    
    def EditPlayer(self):
        global df
        pName = self.playernameEdit.text()
        typeState = self.typeofEdit.text()
        valueStat = self.assistsEdit_2.text()
        
        df.loc[df['Name']==pName, [typeState]] = valueStat
        
        df.to_excel("NBA TEAMS//" + value2 + ".xlsx", engine='xlsxwriter', index=False)
        df = pd.read_excel("NBA TEAMS//" + value2+".xlsx")
        model = PandasModel(df)
        self.tableView.setModel(model)
        self.tableView.resizeColumnsToContents()
        print(df)

    def retranslateUi(self, page2):
        _translate = QtCore.QCoreApplication.translate
        page2.setWindowTitle(_translate("page2", "Form"))
        self.teamLabel.setText(_translate("page2", value2))
        self.addPlayerBtn.setText(_translate("page2", "Add Player"))
        self.removePlayerBtn.setText(_translate("page2", "Remove Player"))
        self.editPlayerByn.setText(_translate("page2", "Edit Player"))
        self.label.setText(_translate("page2", "Player Name:"))
        self.label_2.setText(_translate("page2", "Rebounds:"))
        self.label_3.setText(_translate("page2", "Assist:"))
        self.label_4.setText(_translate("page2", "Steals:"))
        self.label_5.setText(_translate("page2", "Blocks:"))
        self.label_6.setText(_translate("page2", "Turnovers:"))
        self.label_7.setText(_translate("page2", "Points/Game"))
        self.label_8.setText(_translate("page2", "Player Number:"))
        self.label_9.setText(_translate("page2", "New Stat:"))
        self.label_10.setText(_translate("page2", "Stat:"))
        self.label_11.setText(_translate("page2", "Player Name:"))


class PandasModel(QtCore.QAbstractTableModel): 
    def __init__(self, df = pd.DataFrame(), parent=None): 
        QtCore.QAbstractTableModel.__init__(self, parent=parent)
        self._df = df

    def headerData(self, section, orientation, role=QtCore.Qt.DisplayRole):
        if role != QtCore.Qt.DisplayRole:
            return QtCore.QVariant()

        if orientation == QtCore.Qt.Horizontal:
            try:
                return self._df.columns.tolist()[section]
            except (IndexError, ):
                return QtCore.QVariant()
        elif orientation == QtCore.Qt.Vertical:
            try:
                # return self.df.index.tolist()
                return self._df.index.tolist()[section]
            except (IndexError, ):
                return QtCore.QVariant()

    def data(self, index, role=QtCore.Qt.DisplayRole):
        if role != QtCore.Qt.DisplayRole:
            return QtCore.QVariant()

        if not index.isValid():
            return QtCore.QVariant()

        return QtCore.QVariant(str(self._df.ix[index.row(), index.column()]))

    def setData(self, index, value, role):
        row = self._df.index[index.row()]
        col = self._df.columns[index.column()]
        if hasattr(value, 'toPyObject'):
            # PyQt4 gets a QVariant
            value = value.toPyObject()
        else:
            # PySide gets an unicode
            dtype = self._df[col].dtype
            if dtype != object:
                value = None if value == '' else dtype.type(value)
        self._df.set_value(row, col, value)
        return True

    def rowCount(self, parent=QtCore.QModelIndex()): 
        return len(self._df.index)

    def columnCount(self, parent=QtCore.QModelIndex()): 
        return len(self._df.columns)

    def sort(self, column, order):
        colname = self._df.columns.tolist()[column]
        self.layoutAboutToBeChanged.emit()
        self._df.sort_values(colname, ascending= order == QtCore.Qt.AscendingOrder, inplace=True)
        self._df.reset_index(inplace=True, drop=True)
        self.layoutChanged.emit()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

