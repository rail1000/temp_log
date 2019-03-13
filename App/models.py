import pymysql


class model():


    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email


    def create_DB(self):
        conn = pymysql.connect(host='localhost', user='root', password='root', database='233')
        cursor = conn.cursor()

        sql = """
         create table USER1(
        `u_id` int AUTO_INCREMENT PRIMARY KEY,
        `username` char(50) not null,
        `password` char(50) not NULL,
        `email` char(50) not null 
        )
            """
        cursor.execute(sql)
        conn.commit()
        cursor.close()
        conn.close()


    def regist(self):
        conn = pymysql.connect(host='localhost', user='root', password='root', database='233')
        cursor = conn.cursor()
        #print(self.username)
        sql = "insert into user1(u_id,username,password,email)VALUES(0,\'" + str(self.username) + "\',\'" + str(self.password) + "\',\'" + str(self.email)+ "\')"
        #print(sql)
        cursor.execute(sql)
        conn.commit()
        cursor.close()
        conn.close()

    def log(self):
        conn = pymysql.connect(host='localhost', user='root', password='root', database='233')
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        sql = "select password from user1 where username=\'"+str(self.username)+"\' and email=\'"+self.email+"\'"

        cursor.execute(sql)
        res = cursor.fetchall()
        dict=res[0]
        conn.commit()
        cursor.close()
        conn.close()
        return dict['password']
