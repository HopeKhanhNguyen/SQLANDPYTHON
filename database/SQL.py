import os , sqlite3 , time , random

class Database:

    __DATABASE_INIT__ = os.path.join(os.getcwd(), 'config', 'database.db')
    def __init__(self) -> None:
        if os.path.exists(self.__DATABASE_INIT__.split('\\')[-2]) == False:
            os.makedirs(self.__DATABASE_INIT__.split('\\')[-2])
            
        #Kết nối tới DB
        self.db = sqlite3.connect(self.__DATABASE_INIT__)
        self.cursor = self.db.cursor()

    def creatTable(self, name: str, data: str):
        for _ in range(10):
            self.reconnect()
            self.cursor.execute(f'''CREATE TABLE IF NOT EXISTS "{name}" {data}''')
            return True
    
    def insert(self, tableName: str, key: tuple, value: tuple):
        for _ in range(50):
            self.reconnect()
            try:
                self.cursor.execute(f'''INSERT INTO `{tableName}` 
                    {key} 
                    VALUES 
                    {value}''')
                self.db.commit()
                return True
            except Exception as e:pass
    
    def query(self, table_name: str, objQuery: str, where: str|bool = None):
        for _ in range(10):
            self.reconnect()
            try:
                string = f"SELECT {objQuery} FROM {table_name}"
                if where != None:
                    string += f' WHERE {where}'
                data = self.cursor.execute(string).fetchall()
                return data
            except Exception as e: print(e)

    def delete(self, table_name: str, where = None):
        for _ in range(10):
            self.reconnect()
            sql = f"DELETE FROM {table_name}"
            if where is not None:sql += f' WHERE {where}'
            try:
                self.cursor.execute(sql)
                self.db.commit()
                return True
            except: pass

    def close(self):
        self.cursor.close()
        self.db.close()

    def reconnect(self):
        try:
            self.cursor.close()
            self.db.close()
        except:pass
        self.db = sqlite3.connect(self.__DATABASE_INIT__)
        self.cursor = self.db.cursor()

    def update(self, table_name: str, data: str, where: str):
        for _ in range(50):
            try:
                self.reconnect()
                self.cursor.execute(f"UPDATE {table_name} SET {data} WHERE {where}")
                self.db.commit()
                return True
            except Exception as e: print(e)
            time.sleep(random.uniform(0.2, 1))

    def querys(self, query_list = []):
        self.reconnect() 
        for query in query_list:
            self.cursor.execute(query)
        self.db.commit()

    @property
    def excute(self):
        return self.init.execute
    @property

    def init(self):
        self.reconnect()
        return self.cursor
#     def 
# sql = Database()
# # sql.creatTable('accounts22', '("id" INTEGER PRIMARY KEY AUTOINCREMENT, "gmail" TEXT, "password" TEXT)')
# # sql.insert('accounts22', ('gmail', 'password'), ('a;lksou983@gmail.com', '2006Taine'))
# sql.update('accounts22', 'gmail = "oidoioi@gmail.com", password = "218738hs"', 'gmail = "a;lksou983@gmail.com"')
# print(sql.query('accounts22', 'id, gmail'))
# sql.close()
