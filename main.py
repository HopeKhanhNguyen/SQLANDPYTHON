while (True) :
    try :
        from PyQt5 import * 
        break
    except :
        import os
        os.system("pip install PyQt5")

from PyQt5 import QtGui , QtWidgets , QtCore
import os
from database.databseSQL import Truy_van
from data_excel.execl import Exel
from ui.ui import Ui_MainWindow

class Main(QtWidgets.QMainWindow) :
    PATH = f"{os.getcwd()}\database"
    def __init__(self) :
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self._client_db = Truy_van()
        self._work = Exel()
        try :
            if self._client_db.connector() == False:
                self.Mesagebox("CÓ LỖI" , "KHÔNG THỂ KẾT NỐI VỚI DATABASE !!!")
            else :
                self.show_table()
        except Exception as e  : 
            print(e)
            self.Mesagebox("CÓ LỖI" , "KHÔNG THỂ KẾT NỐI VỚI DATABASE !!!")
        self.setFixedSize(1463, 784)
        self.ui.tableWidget.setColumnWidth(0 , 30)
        self.ui.tableWidget.setColumnWidth(1 , 200)
        self.ui.tableWidget.setColumnWidth(2 , 50)
        self.ui.tableWidget.setColumnWidth(3 , 100)
        self.ui.tableWidget.setColumnWidth(4 , 50)
        self.ui.tableWidget.setColumnWidth(5 , 100)

        self.ui.pushButton_4.clicked.connect(self.New_Student)
        self.ui.disconnect_CSDL.clicked.connect(self.disconect_to_CSDL)
        self.ui.connect_CSDL.clicked.connect(self.connect_to_CSDL)
        self.ui.refesh_CSDL.clicked.connect(self.Refesh_CSDL)
        self.ui.pushButton_2.clicked.connect(self.save_to_csv)
        # LOAD DATA LOW_PRIORITY LOCAL INFILE 'C:\\Users\\admin\\DOWNLO~1\\QL7DC9~1\\DATA_E~1\\11A1.csv' REPLACE INTO TABLE `test`.`mark` CHARACTER SET utf8 FIELDS TERMINATED BY ';' OPTIONALLY ENCLOSED BY '"' ESCAPED BY '"' LINES TERMINATED BY '\r\n' IGNORE 1 LINES (`Student_ID`, `Toán`, `Lý`, `Hóa`, `Sinh`, `Sử`, `Văn`, `Anh`, `Tin`);
    def show_table(self) :
        list_hs = self._client_db.SELECT("student")
        list_diem = self._client_db.SELECT("mark")
        
        for hs , diem in zip(list_hs , list_diem) :
            self.ui.tableWidget.insertRow(self.ui.tableWidget.rowCount())
            stt = hs[0] ; name = hs[1] ; lop = hs[2] ; gioitinh = hs[3] ; ngaysinh = hs[4] ; hanhkiem = hs[5]
            tbc = (diem[1] + diem[2] + diem[3] + diem[4] + diem[5] + diem[6] + diem[7] + diem[8])/8
            self.ui.tableWidget.setItem(stt , 0 , QtWidgets.QTableWidgetItem(str(stt+1)))
            self.ui.tableWidget.setItem(stt , 1 , QtWidgets.QTableWidgetItem(str(name)))
            self.ui.tableWidget.setItem(stt , 2 , QtWidgets.QTableWidgetItem(str(gioitinh)))
            self.ui.tableWidget.setItem(stt , 3 , QtWidgets.QTableWidgetItem(str(ngaysinh)))
            self.ui.tableWidget.setItem(stt , 4 , QtWidgets.QTableWidgetItem(str(lop)))
            self.ui.tableWidget.setItem(stt , 6 , QtWidgets.QTableWidgetItem(str(diem[1])))
            self.ui.tableWidget.setItem(stt , 7 , QtWidgets.QTableWidgetItem(str(diem[2])))
            self.ui.tableWidget.setItem(stt , 8 , QtWidgets.QTableWidgetItem(str(diem[3])))
            self.ui.tableWidget.setItem(stt , 9 , QtWidgets.QTableWidgetItem(str(diem[8])))
            self.ui.tableWidget.setItem(stt , 10 , QtWidgets.QTableWidgetItem(str(diem[4])))
            self.ui.tableWidget.setItem(stt , 11 , QtWidgets.QTableWidgetItem(str(diem[5])))
            self.ui.tableWidget.setItem(stt , 12 , QtWidgets.QTableWidgetItem(str(diem[6])))
            self.ui.tableWidget.setItem(stt , 13  , QtWidgets.QTableWidgetItem(str(diem[7])))
            self.ui.tableWidget.setItem(stt , 14 , QtWidgets.QTableWidgetItem(str(tbc)))
            if hanhkiem == "Tot" : 
                self.ui.tableWidget.setItem(stt , 5 , QtWidgets.QTableWidgetItem("Tốt"))
            elif hanhkiem == "Kha" : 
                self.ui.tableWidget.setItem(stt , 5 , QtWidgets.QTableWidgetItem("Khá"))
            elif hanhkiem == "TB" : 
                self.ui.tableWidget.setItem(stt , 5 , QtWidgets.QTableWidgetItem("TB"))
            elif hanhkiem is None or len(hanhkiem) == 0 :
                if tbc > 8 : self.ui.tableWidget.setItem(stt , 5 , QtWidgets.QTableWidgetItem("Tốt")) ; self._client_db.Update("student" , f'Student_ID = "{stt}"' , 'Hanhkiem = "Tot"')
                elif tbc < 8 and tbc >= 7 : self.ui.tableWidget.setItem(stt , 5 , QtWidgets.QTableWidgetItem("Khá")) ; self._client_db.Update("student" , f'Student_ID = "{stt}"' , 'Hanhkiem = "Kha"')
                elif tbc < 7 and tbc >= 6 : self.ui.tableWidget.setItem(stt , 5 , QtWidgets.QTableWidgetItem("TB")) ; self._client_db.Update("student" , f'Student_ID = "{stt}"' , 'Hanhkiem = "TB"')
                else : self.ui.tableWidget.setItem(stt , 5 , QtWidgets.QTableWidgetItem("Yếu")) ; self._client_db.Update("student" , f'Student_ID = "{stt}"' , 'Hanhkiem = "Yeu"')
            else : 
                self.ui.tableWidget.setItem(stt , 5 , QtWidgets.QTableWidgetItem("Yếu"))
            self._work.write_line(self.ui.tableWidget)
            self.delay(0.1)
        
        self.ui.tableWidget.itemChanged.connect(self.item_change)

    def Mesagebox(self, title = "Thông báo", text = ""):
        global msg
        msg = QtWidgets.QMessageBox()
        msg.setWindowIcon(QtGui.QIcon('error.png'))
        msg.setWindowTitle(title)
        # QtWidgets.QMessageBox.about(msg, title,"chi")
        msg.setText(text)
        msg.show()
    
    def delay(self, countdelay):
        loop = QtCore.QEventLoop()
        QtCore.QTimer.singleShot(int(countdelay*1000), loop.quit)
        loop.exec()

    def item_change(self , item) :
        row = item.row()
        col = item.column()
        new_value = item.text() 
        stt = self.ui.tableWidget.item(row , 0).text()
        json_data = {
            "6" : "Toán" , 
            "7" : "Lý" ,
            "8" : "Hóa" , 
            "9" : "Tin" , 
            "10" : "Sinh" , 
            "11" : "Sử" , 
            "12" : "Văn" , 
            "13" : "Anh"
        }
        json_student = {
            "1" : "Students" , 
            "2" : "Sex" , 
            "3" : "Birth" ,
            "4" : "Class" ,  
        }
        self._work.update_csv(row , col , new_value)
        if col > 5 :
            qr = str(json_data[f"{col}"])
            self._client_db.Update("mark" , f"Student_ID = {int(stt) - 1}" , f"{qr} = {new_value}")

        elif col < 5 :
            qr = str(json_student[f"{col}"]) 
            if new_value == "Nữ" : new_value = "Nu"
            self._client_db.Update("student" , f"Student_ID = {int(stt) - 1}" , f'{qr} = "{new_value}"')
            
        else :
            if new_value == "Tốt" :
                self._client_db.Update("student" , f"Student_ID = {int(stt) - 1}" , f'Hanhkiem = "Tot"')    
            elif new_value == "Khá" :
                self._client_db.Update("student" , f"Student_ID = {int(stt) - 1}" , f'Hanhkiem = "Kha"')
            elif new_value == "TB" :
                self._client_db.Update("student" , f"Student_ID = {int(stt) - 1}" , f'Hanhkiem = "TB"')
            else :
                self._client_db.Update("student" , f"Student_ID = {int(stt) - 1}" , f'Hanhkiem = "Yeu"')
    
    def New_Student(self) :
        ten = self.ui.lineEdit.text()
        ngay = self.ui.ngay.value()
        thang = self.ui.thang.value()
        nam = self.ui.nam.value()
        lop = "11A1"
        gioitinh = self.ui.comboBox.currentText()
        self.ui.tableWidget.itemChanged.disconnect(self.item_change)
        if self._client_db.Insert("student" , ten , lop , gioitinh , f"{nam},{thang},{ngay}") :
            self.ui.tableWidget.insertRow(self.ui.tableWidget.rowCount())
            row = self.ui.tableWidget.rowCount()
            self.ui.tableWidget.setItem(row-1 , 0 , QtWidgets.QTableWidgetItem(f'{row}'))
            self.ui.tableWidget.setItem(row-1 , 1 , QtWidgets.QTableWidgetItem(ten))
            self.ui.tableWidget.setItem(row-1 , 2 , QtWidgets.QTableWidgetItem(gioitinh))
            if thang < 10 : thang = f"0{thang}"
            if ngay < 10 : ngay = f"0{ngay}"
            self.ui.tableWidget.setItem(row-1 , 3 , QtWidgets.QTableWidgetItem(f"{nam}-{thang}-{ngay}"))
            self.ui.tableWidget.setItem(row-1 , 4 , QtWidgets.QTableWidgetItem(f"{lop}"))
            for col in range( 6 , self.ui.tableWidget.columnCount()) :
                self.ui.tableWidget.setItem(row-1 , col , QtWidgets.QTableWidgetItem(str(0)))
            self.Mesagebox(text= "Thêm thành công")
            self.ui.tableWidget.itemChanged.connect(self.item_change)
        else :
            self.Mesagebox(text= "Vui lòng kiểm tra lại thông tin")

    def disconect_to_CSDL(self) :
        if self._client_db.database.is_connected():
            self.ui.tableWidget.itemChanged.disconnect(self.item_change)
            self._client_db.database.close()
            for row in range(self.ui.tableWidget.rowCount()) :
                self.ui.tableWidget.removeRow(0)
                self.delay(0.1)
    
    def connect_to_CSDL(self) :
        if self._client_db.database.is_connected() == False :
            try :
                self._client_db.connector()
                self.show_table()
            except Exception as e :
                self.Mesagebox( title= "CÓ LỖI" , text= f"{str(e)}")
    
    def Refesh_CSDL(self) :
        if self._client_db.database.is_connected():
            self.disconect_to_CSDL()
            self.connect_to_CSDL()

    def save_to_csv(self):
        file_name, _ = QtWidgets.QFileDialog.getSaveFileName(self, 'Lưu CSV', '', 'CSV Files (*.csv);;All Files (*)')
        save_file = self._work.save_to_csv(file_name , self.ui.tableWidget)
        if save_file == True :
            self.Mesagebox("THÔNG BÁO" , "LƯU FILE CSV THÀNH CÔNG !!")
        elif save_file is None :
            self.Mesagebox("CÓ LỖI" , "CÓ LỖI TRONG QUÁ TRÌNH LƯU FILE !!")
        else :
            self.Mesagebox("CÓ LỖI" , f"{str(save_file)}")
if __name__ == "__main__" :
    import sys
    app = QtWidgets.QApplication(sys.argv)
    main = Main()
    main.show()
    sys.exit(app.exec_())


