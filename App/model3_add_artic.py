import pymysql

class model3:
    def __init__(self,title,content,family,u_id):
        self.title = title
        self.content = content
        self.family = family
        self.u_id = u_id


    def insert_artic(self):
        conn = pymysql.connect(host='localhost', user='root', password='root', database='233')
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

        sql ="insert into artic(id,title,content,family,u_id)VALUES(0,\'"+self.title+"\',\'"+self.content+"\',\'"+self.family+"\',\'"+self.u_id+"\')"

        cursor.execute(sql)
        conn.commit()
        cursor.close()
        conn.close()



