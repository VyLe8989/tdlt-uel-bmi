# Form implementation generated from reading ui file 'D:\Github\tdlt-uel-bmi\MainWindow.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(130, 20, 271, 51))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(40, 110, 88, 32))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(40, 180, 84, 32))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.labe_8 = QtWidgets.QLabel(parent=self.centralwidget)
        self.labe_8.setGeometry(QtCore.QRect(40, 240, 101, 51))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(16)
        self.labe_8.setFont(font)
        self.labe_8.setObjectName("labe_8")
        self.label_7 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(40, 310, 117, 32))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(16)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.lineEditWeight = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEditWeight.setGeometry(QtCore.QRect(160, 110, 201, 31))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(16)
        self.lineEditWeight.setFont(font)
        self.lineEditWeight.setClearButtonEnabled(False)
        self.lineEditWeight.setObjectName("lineEditWeight")
        self.lineEditHeight = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEditHeight.setGeometry(QtCore.QRect(160, 180, 201, 31))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(16)
        self.lineEditHeight.setFont(font)
        self.lineEditHeight.setClearButtonEnabled(False)
        self.lineEditHeight.setObjectName("lineEditHeight")
        self.label_4 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(390, 100, 81, 41))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(16)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(390, 180, 61, 41))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(16)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(390, 250, 80, 32))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(16)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.labelComment = QtWidgets.QLabel(parent=self.centralwidget)
        self.labelComment.setGeometry(QtCore.QRect(170, 310, 191, 32))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(16)
        self.labelComment.setFont(font)
        self.labelComment.setObjectName("labelComment")
        self.labelBMI = QtWidgets.QLabel(parent=self.centralwidget)
        self.labelBMI.setGeometry(QtCore.QRect(170, 250, 111, 32))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(16)
        self.labelBMI.setFont(font)
        self.labelBMI.setObjectName("labelBMI")
        self.pushButtonCalculate = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButtonCalculate.setGeometry(QtCore.QRect(30, 390, 191, 51))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(16)
        self.pushButtonCalculate.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("D:\\Github\\tdlt-uel-bmi\\images/9875985_calculator_math_calculate_icon.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButtonCalculate.setIcon(icon)
        self.pushButtonCalculate.setIconSize(QtCore.QSize(50, 50))
        self.pushButtonCalculate.setObjectName("pushButtonCalculate")
        self.pushButtonClose = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButtonClose.setGeometry(QtCore.QRect(300, 390, 191, 51))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(16)
        self.pushButtonClose.setFont(font)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("D:\\Github\\tdlt-uel-bmi\\images/6038_close_error_invalid_wrong_icon.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButtonClose.setIcon(icon1)
        self.pushButtonClose.setIconSize(QtCore.QSize(30, 30))
        self.pushButtonClose.setObjectName("pushButtonClose")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.pushButtonClose.clicked.connect(MainWindow.close) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Lê Tường Vy"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600; color:#ff007f;\">BMI Application</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-style:italic; color:#ff557f;\">Weight:</span></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-style:italic; color:#ff557f;\">Height:</span></p></body></html>"))
        self.labe_8.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-style:italic; color:#ff557f;\">BMI:</span></p></body></html>"))
        self.label_7.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-style:italic; color:#ff557f;\">Comment:</span></p></body></html>"))
        self.lineEditWeight.setText(_translate("MainWindow", "45"))
        self.lineEditHeight.setText(_translate("MainWindow", "155"))
        self.label_4.setText(_translate("MainWindow", "(Kg)"))
        self.label_5.setText(_translate("MainWindow", "(Cm)"))
        self.label_6.setText(_translate("MainWindow", "Kg/m2"))
        self.labelComment.setText(_translate("MainWindow", "Normal"))
        self.labelBMI.setText(_translate("MainWindow", "18.73"))
        self.pushButtonCalculate.setText(_translate("MainWindow", "Calculate"))
        self.pushButtonClose.setText(_translate("MainWindow", "Close"))
