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

    def get_names(self):
        conn=sqlite3.connect("mydatabase.db")
        cursor_get_names=conn.execute("""select name,ID from users""")
        names = [row for row in cursor_get_names]
        conn.close()
        return names
    def get_tagids(self):
        conn=sqlite3.connect("mydatabase.db")
        cursor_get_tagids=conn.execute("""select tagid,ID from users""")
        tagids = [row for row in cursor_get_tagids]
        conn.close()
        return tagids
    def get_usernames(self):
        conn=sqlite3.connect("mydatabase.db")
        cursor_get_users=conn.execute("""select username,ID from users""")
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
    newdb.set_name("rajoy",34)
    newdb.set_tagid("raul",34)
    newdb.set_username("PP",34)
    print newdb.get_name()
    print newdb.get_tagid()
    print newdb.get_username()
    newdb.set_name("ramses",34)
    newdb.set_tagid("ramon",34)
    newdb.set_username("PSOE",34)
    print newdb.get_name()
    print newdb.get_tagid()
    print newdb.get_username()

    newdb.set_liters(30,34)
    newdb.set_liters(20,34)
    newdb.set_liters(7,32)
    newdb.set_liters(11,31)

    print newdb.get_liters(34)

