while (True) :
    try :
        import mysql.connector  ; break
    except : 
        import os
        os.system('python -m pip install mysql-connector-python')

from datetime import datetime

class Truy_van():
    def __init__(self , _name = "test") -> None:
        self._name_db = _name
    
    def connector(self) :
        try :
            self.database = mysql.connector.connect(
                host="127.0.0.1",
                user="root",
                password="",
                database=self._name_db
            )
            self.cursor = self.database.cursor()
        except Exception as e :
            print(e)
            return False

    def SELECT(self , table : str) :
        self.cursor.execute(f"SELECT * FROM {table}")
        results = self.cursor.fetchall() # fetchone -> trả về giá trị của dòng đầu tiên của database
        return results
    
    def Insert(self , table : str = None , name : str = None , lop : str = None , sex : str = None , birth : str = None , ) :
        if table == "student" :
            checked = [name , lop , sex , birth] 
            if None in checked : return False
            try :
                id = len(self.SELECT(table)) 
                formatted_birth = datetime.strptime(birth, '%Y,%m,%d').strftime('%Y-%m-%d')
                scripts_sql = f"INSERT INTO {table} (Student_ID , Students , Class , Sex , Birth) VALUES (%s , %s, %s, %s, %s)"
                self.cursor.execute(scripts_sql , (id , name , lop, sex, formatted_birth))
                self.database.commit()
                scripts_sql = f"INSERT INTO mark (Student_ID) VALUES ({id});"
                self.cursor.execute(scripts_sql)
                self.database.commit()
                return True
            except Exception as e : 
                print(e)
                return False
        
    
    def Order_by(self , table : str , name : str , first : str = "*" , DESC : bool = True) :
        try:
            self.cursor.execute(f"SELECT * FROM information_schema.columns WHERE table_name = '{table}' AND column_name = '{name}'")
            column_exists = self.cursor.fetchone()

            if column_exists:
                if DESC :
                    sql = f"SELECT {first} FROM {table} ORDER BY {name} DESC" # Giảm dần
                else :
                    sql = f"SELECT {first} FROM {table} ORDER BY {name}"
                self.cursor.execute(sql)
                results = self.cursor.fetchall()
                return results
            else:
                return False
        except Exception as e:
            print(e)
            return False

    def Query(self , table : str , obJ : str = "*", where : str|bool = None) :
        try :
            sql_query = f"SELECT {obJ} FROM {table}"
            if where != None :
                sql_query += f' WHERE {where}'
                self.cursor.execute(sql_query)
                results = self.cursor.fetchall()
                return results
            else : return False
        except Exception as e:
            print(e)
            return False 

    def Delete(self , table : str , address = None ):
        try :
            if address != None :
                sql = f"DELETE FROM {table} WHERE {address}"
                self.cursor.execute(sql)
                self.database.commit()
                return True
            else : 
                return False
        except Exception as e :
            print(e)
            return False

    def Update(self , table : str , old : str , new : str):
        try :
            if self.Query(table , where=f"{old}") != False :
                sql = f"UPDATE {table} SET {new} WHERE {old}"
                self.cursor.execute(sql)
                self.database.commit()
                return True
            else :
                print("Không truy vấn được")
                return False
        except Exception as e :
            print(e)
            return False
        
# print(Truy_van().Insert("student" , "Cung Dinh Tien" , "11A1" , "Nam" , "2007,10,10"))
# print(Truy_van().Delete("student" , 'Students = "Cung Dinh Tien"'))
# print(Truy_van().Query("student" , where="Students = 'Cung Dinh Tien'"))
# print(Truy_van().Update("student" , old="Students = 'Cung Dinh Tien'" , new="Students = 'Tran Sy Hung'"))
# id = Truy_van().Query("student" , "Student_ID" , "Students = 'Nguyen Huu Khanh'")[0][0]

# print("Hoc sinh" , Truy_van().Query("student" , "Students" , "Students = 'Nguyen Huu Khanh'")[0][0] , "Co diem toan la" , Truy_van().Query("mark" , "Lý" , f"Student_ID = {id}" )[0][0])
# print(Truy_van().SELECT("student"))