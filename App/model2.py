import pymysql

class model2:

    def __init__(self,u_id):
        self.u_id = u_id



    def query_artic(self):
        conn = pymysql.connect(host='localhost', user='root', password='root', database='233')
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

        sql = "select * from artic where u_id=\'" + self.u_id + "\'"

        cursor.execute(sql)
        res = cursor.fetchall()
        conn.commit()
        cursor.close()
        conn.close()
        return res

