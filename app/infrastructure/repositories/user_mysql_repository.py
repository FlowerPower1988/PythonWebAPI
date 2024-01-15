import mysql.connector
import sys
from ...abstraction.repositories.user_repository_interface import IUserRepository
from ...model.user import User, UserValues

try:
    mydb = mysql.connector.connect(
     host = 'localhost',
     user = 'root',
        password = 'Y1012Jqkhkp',
        database = 'mysql_repository'
    )
    mycursor=mydb.cursor()
except Exception as e:
    print(e)
    sys.exit()
    
class UserMysqlRepository(IUserRepository):
    def read_users(self):
        try:
            mycursor.execute("SELECT * FROM users")
            users = mycursor.fetchall()
            user_list=[]
            for user in users:
                new_user = User(id=user[0], name=user[1], email=user[2])
                user_list.append(new_user)
            return user_list
        finally:
            if mycursor:
                mycursor.close()
            if mydb.is_connected():
                mydb.close()
    
    def read_user(self, user_id: int):
        try:
            sql = "SELECT * FROM users WHERE ID = %s"
            val = (user_id,)
            mycursor.execute(sql, val)
            user = mycursor.fetchone()
            if user is None:
                return None
            new_user = User(id=user[0], name=user[1], email=user[2])
            return new_user
        except:
            return None
        finally:
            if mycursor:
                mycursor.close()
            if mydb.is_connected():
                mydb.close()
    
    def create_user(self, new_user_values: UserValues):
        try:    
            sql = "INSERT INTO users(user_name, email) values(%s, %s)"
            val = (new_user_values.name, new_user_values.email)
            mycursor.execute(sql, val)
            mydb.commit()
            
            mycursor.execute("SELECT LAST_INSERT_ID();")
            last_id = mycursor.fetchone()
            if last_id is not None and isinstance(last_id[0], int):
                last_id_int : int = last_id[0]
            mycursor.execute("SELECT * FROM users WHERE ID = %s", (last_id_int,))
            user = mycursor.fetchone()
            new_user = User(id=user[0], name=user[1], email=user[2]) if user is not None else None
            return new_user
        finally:
            if mycursor:
                mycursor.close()
            if mydb.is_connected():
                mydb.close()
    
    def delete_user(self, user_id: int):
        try:
            sql = "SELECT EXISTS(SELECT 1 FROM users WHERE id = %s)"
            val = (user_id,)
            mycursor.execute(sql, val)
            result = mycursor.fetchone() #get the result which is packed
            if result is None: #check if packed result is NONE, because unpacking NONE gives the error
                return None
            id_exist, = result #unpacking the result, 
            id_exist = bool(id_exist)
            if not id_exist:
                return None
            sql = ("DELETE FROM users WHERE ID = %s")
            mycursor.execute(sql,val)
            mydb.commit()
            return id_exist
        except:
            return None
        finally:
            if mycursor:
                mycursor.close()
            if mydb.is_connected():
                mydb.close()
    
    def update_user(self, user_to_be_updated_id: int ,new_values: UserValues):
        try:    
            sql = "SELECT EXISTS(SELECT 1 FROM users WHERE id = %s)"
            val = (user_to_be_updated_id,)
            mycursor.execute(sql, val)
            result = mycursor.fetchone() #get the result which is packed
            if result is None: #check if packed result is NONE, because unpacking NONE gives the error
                return None
            id_exist, = result #unpacking the result, 
            id_exist = bool(id_exist)
            if not id_exist:
                return None
            sql2 = ("UPDATE users SET user_name = %s, email = %s WHERE ID = %s")
            val2 = (new_values.name, new_values.email, user_to_be_updated_id)
            mycursor.execute(sql2,val2)
            mydb.commit()
            
            sql3 = "SELECT id, user_name, email FROM users WHERE ID = %s"
            #val = (user_to_be_updated_id,)
            mycursor.execute(sql3, val)
            user = mycursor.fetchone()
            new_user = User(id=user[0], name=user[1], email=user[2]) if user is not None else None
            return new_user
        except:
            return None
        finally:
            if mycursor:
                mycursor.close()
            if mydb.is_connected():
                mydb.close()