import mysql.connector


class DB():
    def __init__(self):
        self.mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="elibelib",
        port="3306",
        database="sakila"
                                            )



    def ask(self,qury):
        connaction = self.mydb.cursor()
        connaction.execute(qury)
        return connaction.fetchall()

    def update(self,qury):
        connaction = self.mydb.cursor()
        connaction.execute(qury)
        return self.mydb.commit()
