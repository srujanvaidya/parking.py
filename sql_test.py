import mysql.connector


class Server:
    def __init__ (self):
        self.mydb=mysql.connector.connect(host='localhost',
                                          user='root',
                                          passwd = 'srujanvaidya',
                                          database = 'parking')
        self.mycursor=self.mydb.cursor()
        self.mycursor.execute("use parking")



    def park1 (self,carno,j):
        self.mycursor.execute("update lot set carno = %s where slot = %s",(carno,j))
        self.mydb.commit()

    def exit1 (self,k):
        self.mycursor.execute("update lot set carno = %s where slot = %s",("free",k))
        self.mydb.commit()

obj=Server()







