# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'second.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(523, 377)
        MainWindow.setMinimumSize(QtCore.QSize(523, 377))
        MainWindow.setMaximumSize(QtCore.QSize(523, 377))
        MainWindow.setStyleSheet("background:black;\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 6, 501, 20))
        font = QtGui.QFont()
        self.strm=[]
        font.setFamily("Roboto Mono")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setStyleSheet("background:silver;\n"
"padding:4px;")
        self.label.setObjectName("label")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 200, 501, 161))
        self.groupBox_2.setStyleSheet("background:#777;\n"
"border-radius:18px;")
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.down = QtWidgets.QPushButton(self.groupBox_2)
        self.down.setGeometry(QtCore.QRect(370, 20, 117, 117))
        font = QtGui.QFont()
        font.setFamily("Inter")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.down.setFont(font)
        self.down.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.down.setStyleSheet("background:tomato;\n"
"color:green;\n"
"border-radius:55px")
        self.down.setObjectName("down")
        self.groupBox = QtWidgets.QGroupBox(self.groupBox_2)
        self.groupBox.setGeometry(QtCore.QRect(190, 10, 141, 141))
        self.groupBox.setStyleSheet("background:silver;\n"
"")
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.comboBox = QtWidgets.QComboBox(self.groupBox)
        self.comboBox.setGeometry(QtCore.QRect(10, 20, 121, 36))
        self.comboBox.setStyleSheet("background:grey;")
        self.comboBox.setObjectName("comboBox")
        self.size = QtWidgets.QLabel(self.groupBox)
        self.size.setGeometry(QtCore.QRect(10, 90, 121, 31))
        self.size.setStyleSheet("background:grey;")
        self.size.setAlignment(QtCore.Qt.AlignCenter)
        self.size.setObjectName("size")
        self.photo = QtWidgets.QLabel(self.groupBox_2)
        self.photo.setGeometry(QtCore.QRect(10, 10, 135, 135))
        font = QtGui.QFont()
        font.setFamily("Raleway")
        font.setPointSize(37)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.photo.setFont(font)
        self.photo.setStyleSheet("background:silver;\n"
"border-radius:18px")
        self.photo.setObjectName("photo")
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(9, 40, 501, 61))
        self.groupBox_3.setStyleSheet("background:#777;\n"
"border-radius:9px;")
        self.groupBox_3.setTitle("")
        self.groupBox_3.setObjectName("groupBox_3")
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit.setGeometry(QtCore.QRect(10, 10, 381, 36))
        self.lineEdit.setStyleSheet("background:silver;\n"
"border-radius:18px;")
        self.lineEdit.setObjectName("lineEdit")
        self.browse = QtWidgets.QPushButton(self.groupBox_3)
        self.browse.setGeometry(QtCore.QRect(410, 10, 71, 36))
        self.browse.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.browse.setStyleSheet("background:silver;\n"
"border-radius:18px;\n"
"color:black;")
        self.browse.setObjectName("browse")
        self.title = QtWidgets.QTextEdit(self.centralwidget)
        self.title.setGeometry(QtCore.QRect(40, 110, 441, 81))
        font = QtGui.QFont()
        font.setFamily("HSN Sara")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.title.setFont(font)
        self.title.setStyleSheet("background:#777;\n"
"border-radius:18px;\n"
"color:white;\n"
"\n"
"")
        self.title.setObjectName("title")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.comboBox.currentIndex()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "second window"))
        self.down.setText(_translate("MainWindow", "ابدأ التنزيل"))
        self.size.setText(_translate("MainWindow", "الحجم"))
        self.photo.setText(_translate("MainWindow", "الصورة"))
        self.browse.setText(_translate("MainWindow", "حفظ في"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
