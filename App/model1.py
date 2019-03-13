import pymysql


class model1:

    def __init__(self, family, title, content, id):
        self.family = family
        self.title = title
        self.content = content
        self.id = id

    def query_family(self):
        conn = pymysql.connect(host='localhost', user='root', password='root', database='233')
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

        sql = "select * from artic where family=\'" + self.family + "\'"

        cursor.execute(sql)
        res = cursor.fetchall()
        conn.commit()
        cursor.close()
        conn.close()
        return res

    def query_all(self):
        conn = pymysql.connect(host='localhost', user='root', password='root', database='233')
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

        sql = "select * from artic "

        cursor.execute(sql)
        res = cursor.fetchall()
        conn.commit()
        cursor.close()
        conn.close()
        # print(res)
        return res

    def insert(self):
        conn = pymysql.connect(host='localhost', user='root', password='root', database='233')
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

        sql = "insert into artic(id,title,content,family)VALUES(0,\'" + self.title + "\',\'" + self.content + "\',\'" + self.family + "\')"
        cursor.execute(sql)

        conn.commit()
        cursor.close()
        conn.close()

    def query_id(self):
        conn = pymysql.connect(host='localhost', user='root', password='root', database='233')
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

        sql = "select * from artic where id=\'" + self.id + "\'"

        cursor.execute(sql)
        res = cursor.fetchall()
        conn.commit()
        cursor.close()
        conn.close()
        return res

    def query_title(self):
        conn = pymysql.connect(host='localhost', user='root', password='root', database='233')
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

        sql = "SELECT * from artic where title like \'%"+self.title+"%\'"

        cursor.execute(sql)
        res = cursor.fetchall()
        conn.commit()
        cursor.close()
        conn.close()
        return res