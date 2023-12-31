from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1463, 784)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 1441, 211))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.groupBox_2 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 0, 401, 201))
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.label = QtWidgets.QLabel(self.groupBox_2)
        self.label.setGeometry(QtCore.QRect(10, 20, 61, 21))
        self.label.setStyleSheet("font: 75 9pt \"Tahoma\";")
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit.setGeometry(QtCore.QRect(82, 20, 301, 20))
        self.lineEdit.setDragEnabled(False)
        self.lineEdit.setClearButtonEnabled(True)
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(self.groupBox_2)
        self.label_2.setGeometry(QtCore.QRect(10, 60, 61, 21))
        self.label_2.setStyleSheet("font: 75 9pt \"Tahoma\";")
        self.label_2.setObjectName("label_2")
        self.ngay = QtWidgets.QSpinBox(self.groupBox_2)
        self.ngay.setGeometry(QtCore.QRect(80, 60, 42, 22))
        self.ngay.setMinimum(1)
        self.ngay.setMaximum(31)
        self.ngay.setObjectName("ngay")
        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        self.label_3.setGeometry(QtCore.QRect(140, 60, 20, 21))
        self.label_3.setStyleSheet("font: 75 9pt \"Tahoma\";")
        self.label_3.setObjectName("label_3")
        self.thang = QtWidgets.QSpinBox(self.groupBox_2)
        self.thang.setGeometry(QtCore.QRect(160, 60, 42, 22))
        self.thang.setMinimum(1)
        self.thang.setMaximum(12)
        self.thang.setObjectName("thang")
        self.label_4 = QtWidgets.QLabel(self.groupBox_2)
        self.label_4.setGeometry(QtCore.QRect(220, 60, 21, 21))
        self.label_4.setStyleSheet("font: 75 9pt \"Tahoma\";")
        self.label_4.setObjectName("label_4")
        self.nam = QtWidgets.QSpinBox(self.groupBox_2)
        self.nam.setGeometry(QtCore.QRect(240, 60, 101, 22))
        self.nam.setMinimum(1999)
        self.nam.setMaximum(2007)
        self.nam.setObjectName("nam")
        self.label_5 = QtWidgets.QLabel(self.groupBox_2)
        self.label_5.setGeometry(QtCore.QRect(10, 100, 61, 21))
        self.label_5.setStyleSheet("font: 75 9pt \"Tahoma\";")
        self.label_5.setObjectName("label_5")
        self.comboBox = QtWidgets.QComboBox(self.groupBox_2)
        self.comboBox.setGeometry(QtCore.QRect(80, 100, 69, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label_6 = QtWidgets.QLabel(self.groupBox_2)
        self.label_6.setGeometry(QtCore.QRect(10, 140, 41, 21))
        self.label_6.setStyleSheet("font: 75 9pt \"Tahoma\";")
        self.label_6.setObjectName("label_6")
        self.comboBox_2 = QtWidgets.QComboBox(self.groupBox_2)
        self.comboBox_2.setGeometry(QtCore.QRect(50, 140, 69, 22))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.label_7 = QtWidgets.QLabel(self.groupBox_2)
        self.label_7.setGeometry(QtCore.QRect(140, 140, 41, 21))
        self.label_7.setStyleSheet("font: 75 9pt \"Tahoma\";")
        self.label_7.setObjectName("label_7")
        self.comboBox_3 = QtWidgets.QComboBox(self.groupBox_2)
        self.comboBox_3.setGeometry(QtCore.QRect(180, 140, 101, 22))
        self.comboBox_3.setObjectName("comboBox_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_4.setGeometry(QtCore.QRect(300, 160, 75, 23))
        self.pushButton_4.setObjectName("pushButton_4")
        self.groupBox_3 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_3.setGeometry(QtCore.QRect(420, 0, 641, 201))
        self.groupBox_3.setTitle("")
        self.groupBox_3.setObjectName("groupBox_3")
        self.label_8 = QtWidgets.QLabel(self.groupBox_3)
        self.label_8.setGeometry(QtCore.QRect(20, 20, 81, 21))
        self.label_8.setStyleSheet("font: 75 9pt \"Tahoma\";")
        self.label_8.setObjectName("label_8")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_2.setGeometry(QtCore.QRect(110, 20, 341, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton.setGeometry(QtCore.QRect(470, 20, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.label_9 = QtWidgets.QLabel(self.groupBox_3)
        self.label_9.setGeometry(QtCore.QRect(110, 50, 341, 21))
        self.label_9.setStyleSheet("font: 75 9pt \"Tahoma\";\n"
"color: rgb(255, 0, 0);")
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.groupBox_3)
        self.label_10.setGeometry(QtCore.QRect(20, 100, 81, 21))
        self.label_10.setStyleSheet("font: 75 9pt \"Tahoma\";")
        self.label_10.setObjectName("label_10")
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_2.setGeometry(QtCore.QRect(100, 100, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.disconnect_CSDL = QtWidgets.QPushButton(self.groupBox)
        self.disconnect_CSDL.setGeometry(QtCore.QRect(1080, 20, 141, 51))
        self.disconnect_CSDL.setObjectName("disconnect_CSDL")
        self.connect_CSDL = QtWidgets.QPushButton(self.groupBox)
        self.connect_CSDL.setGeometry(QtCore.QRect(1260, 20, 141, 51))
        self.connect_CSDL.setObjectName("connect_CSDL")
        self.refesh_CSDL = QtWidgets.QPushButton(self.groupBox)
        self.refesh_CSDL.setGeometry(QtCore.QRect(1180, 90, 141, 51))
        self.refesh_CSDL.setObjectName("refesh_CSDL")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(10, 240, 1441, 521))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(15)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(13, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(14, item)
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.verticalHeader().setVisible(False)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Họ và tên"))
        self.label_2.setText(_translate("MainWindow", "Ngày sinh"))
        self.label_3.setText(_translate("MainWindow", "/"))
        self.label_4.setText(_translate("MainWindow", "/"))
        self.label_5.setText(_translate("MainWindow", "Giới tinh"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Nam"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Nữ"))
        self.label_6.setText(_translate("MainWindow", "Khối"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "A"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "C"))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "D"))
        self.label_7.setText(_translate("MainWindow", "Lớp"))
        self.pushButton_4.setText(_translate("MainWindow", "Thêm"))
        self.label_8.setText(_translate("MainWindow", "File csv , txt"))
        self.pushButton.setText(_translate("MainWindow", "Import"))
        self.label_9.setText(_translate("MainWindow", "(Lưu ý các file txt phải ngăn cách nhau bởi dấu | hoặc dấu ,)"))
        self.label_10.setText(_translate("MainWindow", "File csv , txt"))
        self.pushButton_2.setText(_translate("MainWindow", "Export"))
        self.disconnect_CSDL.setText(_translate("MainWindow", "Ngắt Kết Nối với CSDL"))
        self.connect_CSDL.setText(_translate("MainWindow", "Kết với với CSDL"))
        self.refesh_CSDL.setText(_translate("MainWindow", "Làm mới CSDL "))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "STT"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Họ và Tên"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Giới tính"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Ngày sinh"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Lớp"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Hạnh kiểm "))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Toán"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "Vật Lý"))
        item = self.tableWidget.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "Hóa"))
        item = self.tableWidget.horizontalHeaderItem(9)
        item.setText(_translate("MainWindow", "Tin"))
        item = self.tableWidget.horizontalHeaderItem(10)
        item.setText(_translate("MainWindow", "Sinh"))
        item = self.tableWidget.horizontalHeaderItem(11)
        item.setText(_translate("MainWindow", "Sử "))
        item = self.tableWidget.horizontalHeaderItem(12)
        item.setText(_translate("MainWindow", "Văn"))
        item = self.tableWidget.horizontalHeaderItem(13)
        item.setText(_translate("MainWindow", "Tiếng Anh"))
        item = self.tableWidget.horizontalHeaderItem(14)
        item.setText(_translate("MainWindow", "Trung bình "))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
