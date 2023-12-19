import mysql.connector
import sys
from ...abstraction.repositories.user_repository_interface import IUserRepository
from ...model.user import User, UserValues

try:
    mydb = mysql.connector.connect(
     host = 'localhost',
     user = 'root',
        password = 'Y1012Jqkhkp',
        database = 'user_mysql_repository'
    )
    mycursor=mydb.cursor()
except Exception as e:
    print(e)
    sys.exit()
    
class UserMysqlRepository(IUserRepository):
    def read_users(self):
        mycursor.execute("SELECT * FROM users")
        users = mycursor.fetchall()
        for user in users:
            return user
    
    def read_user(self, user_id: int):
        #matching_users = [user for user in users if user.id == user_id]
        #return matching_users[0] if matching_users else None
        sql = "SELECT * FROM users WHERE ID = %s"
        val = (user_id,)
        mycursor.execute(sql, val)
        user = mycursor.fetchone()
        return user
    
    def create_user(self, new_user_values: UserValues):
        sql = "INSERT INTO users(user_name, email) values(%s, %s)"
        val = (new_user_values.name, new_user_values.email)
        mycursor.execute(sql, val)
        mydb.commit()
        
        mycursor.execute("SELECT LAST_INSERT_ID();")
        last_id = mycursor.fetchone()[0]
        mycursor.execute("SELECT * FROM users WHERE ID = %s", (last_id,))
        user = mycursor.fetchone()
        new_user = User(id=int(user['id']), name=user['user_name'], email=user['email'])
        return new_user
    
    def delete_user(self, user_id: int):
        result = True
        sql = ("DELETE FROM users WHERE ID = %s")
        val = (user_id,)
        mycursor.execute(sql,val)
        return result
    
    def update_user(self, user_to_be_updated_id: int ,new_values: UserValues):
        sql = ("UPDATE users SET user_name = %s, email = %s WHERE ID = %s")
        val = (new_values.name, new_values.email, user_to_be_updated_id)
        mycursor.execute(sql,val)
        user = mycursor.fetchall()
        return user