import os
import csv

class Exel():
    def __init__(self , name = "11A1") -> None:
        self.PATH = f"{os.getcwd()}\\data_excel"
        self.colums = ["STT" , "Ho va ten" , "Gioi tinh" , "Ngay sinh" , "Lop" , "Hanh kiem" , "Toan" , "Ly" , "Hoa" , "Sinh" , "Su" , "Van" , "Tieng Anh" , "Trung binh"]
        self.name = name
        with open(f"{self.PATH}\\{self.name}.csv" , "a+" , encoding="utf-8-sig" , newline= "") as csvfile :
            self.csvwriter = csv.writer(csvfile)
            self.csvwriter.writerow(self.colums)

    def write_line(self , tableWidget : object) :
        print("cc")
        with open(f"{self.PATH}\\{self.name}.csv" , "a+" , encoding="utf-8-sig" , newline= "") as csvfile :
            self.csvwriter = csv.writer(csvfile)
            for row in range(tableWidget.rowCount()):
                row_data = [tableWidget.item(row, col).text() for col in range(tableWidget.columnCount())]
            self.csvwriter.writerow(row_data)

    def update_csv(self, row, col, new_value):
        with open(f"{self.PATH}\\{self.name}.csv", 'r', newline='' , encoding="utf-8-sig") as csvfile:
            csvreader = csv.reader(csvfile)
            data = list(csvreader)
            data[row][col] = new_value

        with open(f"{self.PATH}\\{self.name}.csv", 'w', newline='' , encoding="utf-8-sig") as csvfile:
            self.csvwriter = csv.writer(csvfile)
            self.csvwriter.writerows(data)

    def save_to_csv(self , file_name , tableWidghet):
        if file_name:
            try :
                with open(file_name, 'w', newline='' , encoding= "utf-8-sig") as csvfile:
                    csvwriter = csv.writer(csvfile)
                    header = [tableWidghet.horizontalHeaderItem(i).text() for i in range(tableWidghet.columnCount())]
                    csvwriter.writerow(header)

                    for row in range(tableWidghet.rowCount()):
                        row_data = [tableWidghet.item(row, col).text() for col in range(tableWidghet.columnCount())]
                        csvwriter.writerow(row_data)
                return True
            
            except Exception as e :
                return e
        
        return