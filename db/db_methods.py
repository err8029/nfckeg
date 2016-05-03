import sqlite3

class Database():
    def __init__(self):
        conn=sqlite3.connect("mydatabase.db")
        try:
            cursor=conn.execute("create table users(ID integer, name text, tagid text, username text)")
            cursor=conn.execute("create table beer(ID integer, liters real)")
        except:
            cursor=conn.cursor()
        conn.commit()
        conn.close()

#--------------------taula users---------------------------------------------------------------------------------

    def get_names(self,name):
        conn=sqlite3.connect("mydatabase.db")
        cursor_get_names=conn.execute("""select name,ID from users where name = ?""", (name,))
        names = [row for row in cursor_get_names]
        conn.close()
        return names
    def get_tagids(self,tagid):
        conn=sqlite3.connect("mydatabase.db")
        cursor_get_tagids=conn.execute("""select tagid,ID from users where tagid = ?""", (tagid,))
        tagids = [row for row in cursor_get_tagids]
        conn.close()
        return tagids
    def get_usernames(self, usernames):
        conn=sqlite3.connect("mydatabase.db")
        cursor_get_users=conn.execute("""select username,ID from users = ?""", (usernames,))
        users = [row for row in cursor_get_users]
        conn.close()
        return users

    def set_name(self,name,ID):
        conn=sqlite3.connect("mydatabase.db")
        cursor_set_name=conn.execute("""update users set name = ? where ID = ?""", (name,ID))
        conn.commit()
        conn.close()
    def set_tagid(self,tagid,ID):
        conn=sqlite3.connect("mydatabase.db")
        cursor_set_tagid=conn.execute("""update users set tagid = ? where ID = ?""", (tagid,ID))
        conn.commit()
        conn.close()
    def set_username(self,username,ID):
        conn=sqlite3.connect("mydatabase.db")
        cursor_set_username=conn.execute("""update users set username = ? where ID = ?""", (username,ID))
        conn.commit()
        conn.close()

    def save(self,name,tagid,username):
        conn=sqlite3.connect("mydatabase.db")
        #------------Obtencio automatica de numero de Id---------
        ID=0
        cursor_id=conn.execute("select * from users")
        for row in cursor_id:
            ID=ID+1
        #--------------------------------------------------------
        cursor_save=conn.execute("insert into users (ID,name,tagid,username) values(?, ?, ?, ?)", (ID,name,tagid,username))
        conn.commit()
        conn.close()

#--------------------taula beer---------------------------------------------------------------------------------

    def set_liters(self,liters,ID):
        conn=sqlite3.connect("mydatabase.db")
        cursor_user=conn.execute("insert into beer (ID,liters) values(?, ?)", (ID,liters))
        conn.commit()
        conn.close()
    def get_liters(self,ID):
        conn=sqlite3.connect("mydatabase.db")
        cursor_get_liters=conn.execute("""select liters from beer where ID = ?""", (ID,))
        liters = [row for row in cursor_get_liters]
        conn.close()
        return liters


if __name__=="__main__":

    newdb=Database()
    #newdb.save("mariano rajoy","00x1","rajoy65")
    print newdb.get_tagids("00x1")
