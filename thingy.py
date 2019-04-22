# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Adeel Asghar\Desktop\thingy.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from widget import Ui_page2
import pandas as pd
global df
df = pd.read_excel("Northwest Division.xlsx",sheet_name = "Portland")
global value

class Ui_MainWindow(object):        
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(493, 300)
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
        global value
        global df
        value = self.teamName.text()
        if 'Denver' in value:
            self.incorrectLabel.hide()
            df = pd.read_excel("Northwest Division.xlsx",sheet_name = "Denver")   
            self.window = QtWidgets.QMainWindow()
            self.ui = Ui_page2()
            self.ui.setupUi(self.window)
            self.window.show()
        if 'Portland' in value:
            self.incorrectLabel.hide()
            df = pd.read_excel("Northwest Division.xlsx",sheet_name = "Portland")   
            self.window = QtWidgets.QMainWindow()
            self.ui = Ui_page2()
            self.ui.setupUi(self.window)
            self.window.show()
        if 'Utah' in value:
            self.incorrectLabel.hide()
            df = pd.read_excel("Northwest Division.xlsx",sheet_name = "Utah")   
            self.window = QtWidgets.QMainWindow()
            self.ui = Ui_page2()
            self.ui.setupUi(self.window)
            self.window.show()
        if 'Oklahoma' in value:
            self.incorrectLabel.hide()
            df = pd.read_excel("Northwest Division.xlsx",sheet_name = "Oklahoma")   
            self.window = QtWidgets.QMainWindow()
            self.ui = Ui_page2()
            self.ui.setupUi(self.window)
            self.window.show()
        if 'Minnesota' in value:
            self.incorrectLabel.hide()
            df = pd.read_excel("Northwest Division.xlsx",sheet_name = "Minnesota")   
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
        page2.resize(800, 600)
        self.teamLabel = QtWidgets.QLabel(page2)
        self.teamLabel.setGeometry(QtCore.QRect(20, 20, 181, 21))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.teamLabel.setFont(font)
        self.teamLabel.setObjectName("teamLabel")
        self.addPlayerBtn = QtWidgets.QPushButton(page2)
        self.addPlayerBtn.setGeometry(QtCore.QRect(20, 60, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.addPlayerBtn.setFont(font)
        self.addPlayerBtn.setObjectName("addPlayerBtn")
        self.removePlayerBtn = QtWidgets.QPushButton(page2)
        self.removePlayerBtn.setGeometry(QtCore.QRect(20, 160, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.removePlayerBtn.setFont(font)
        self.removePlayerBtn.setObjectName("removePlayerBtn")
        self.editPlayerByn = QtWidgets.QPushButton(page2)
        self.editPlayerByn.setGeometry(QtCore.QRect(20, 110, 161, 41))
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
        self.removePlayerEdit.setGeometry(QtCore.QRect(190, 160, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.removePlayerEdit.setFont(font)
        self.removePlayerEdit.setObjectName("removePlayerEdit")
        
        self.editPlayerEdit = QtWidgets.QLineEdit(page2)
        self.editPlayerEdit.setGeometry(QtCore.QRect(190, 110, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.editPlayerEdit.setFont(font)
        self.editPlayerEdit.setObjectName("editPlayerEdit")
        
        self.addPlayerEdit = QtWidgets.QLineEdit(page2)
        self.addPlayerEdit.setGeometry(QtCore.QRect(190, 60, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.addPlayerEdit.setFont(font)
        self.addPlayerEdit.setObjectName("addPlayerEdit")
        self.removePlayerBtn.clicked.connect(self.DeletePlayer)
        self.retranslateUi(page2)
        QtCore.QMetaObject.connectSlotsByName(page2)


    def DeletePlayer(self):
        global value
        print(value)
        global df
        choose = self.removePlayerEdit.text()
        if(choose == '0'):
            df = df.drop([0])
            print(df)
            
        elif(choose == '1'):
            df = df.drop([1])

        elif(choose == '2'):
            df = df.drop([2])
            print(df)

        elif(choose == '3'):
            df = df.drop([3])
            print(df)

        elif(choose == '4'):
            df = df.drop([4])
            print(df)

        elif(choose == '5'):
            df = df.drop([5])
            print(df)

        elif(choose == '6'):
            df = df.drop([6])
            print(df)

        elif(choose == '7'):
            df = df.drop([7])
            print(df)

        elif(choose == '8'):
            df = df.drop([8])
            print(df)

        elif(choose == '9'):
            df = df.drop([9])
            print(df)

        else:
            print("Incorrect!")

        self.tableView.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tableView.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tableView.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tableView.setGeometry(QtCore.QRect(260, 57, 500, 450))
        self.tableView.setShowGrid(True)
        self.tableView.setSortingEnabled(True)
        
        df.to_excel("output.xlsx", engine='xlsxwriter', index=False)
        df = pd.read_excel("output.xlsx")
        model = PandasModel(df)
        self.tableView.setModel(model)
        self.tableView.resizeColumnsToContents()
     

    def retranslateUi(self, page2):
        _translate = QtCore.QCoreApplication.translate
        page2.setWindowTitle(_translate("page2", "Form"))
        self.teamLabel.setText(_translate("page2", "Nuggets"))
        self.addPlayerBtn.setText(_translate("page2", "Add Player"))
        self.removePlayerBtn.setText(_translate("page2", "Remove Player"))
        self.editPlayerByn.setText(_translate("page2", "Edit Player"))


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

