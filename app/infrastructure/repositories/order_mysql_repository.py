import mysql.connector
import sys
from ...abstraction.repositories.order_repository_interface import IOrderRepository
from ...model.order import Order, OrderValues

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
    
class OrderMysqlRepository(IOrderRepository):
    def read_orders(self):
        mycursor.execute("SELECT * FROM orders")
        orders = mycursor.fetchall()
        order_list=[]
        for order in orders:
            new_order = Order(id=order[0], user_id=order[1], street_name=order[2], postal_code=order[3], city=order[4], 
                              date_of_order=order[5], total_price=order[6], tax=order[7])
            order_list.append(new_order)
        return order_list
    
    def read_order(self, order_id: int):
        try:
            sql = "SELECT * FROM orders WHERE ID = %s"
            val = (order_id,)
            mycursor.execute(sql, val)
            order = mycursor.fetchone()
            if order is None:
                return None
            new_order = Order(id=order[0], user_id=order[1], street_name=order[2], postal_code=order[3], city=order[4],
                              date_of_order=order[5], total_price=order[6], tax=order[7])
            return new_order
        except:
            return None
        finally:
            if mycursor:
                mycursor.close()
            if mydb.is_connected():
                mydb.close()
    
    def create_order(self, new_values: OrderValues):
        sql = ("INSERT INTO orders(user_id, street_name, postal_code, city, date_of_order, total_price, tax)"
                "values(%s, %s, %s, %s, %s, %s, %s)")
        val = (new_values.user_id, new_values.street_name, new_values.postal_code, new_values.city,
               new_values.date_of_order, new_values.total_price, new_values.tax)
        mycursor.execute(sql, val)
        mydb.commit()
        
        mycursor.execute("SELECT LAST_INSERT_ID();")
        last_id = mycursor.fetchone()
        if last_id is not None and isinstance(last_id[0], int):
            last_id_int : int = last_id[0]
        mycursor.execute("SELECT * FROM orders WHERE ID = %s", (last_id_int,))
        order = mycursor.fetchone()
        new_order = Order(id=order[0], user_id=order[1], street_name=order[2], postal_code=order[3], city=order[4],
                          date_of_order=order[5], total_price=order[6], tax=order[7]) if order is not None else None
        return new_order
    
    def delete_order(self, order_id: int):
        try:
            sql = "SELECT EXISTS(SELECT 1 FROM orders WHERE id = %s)"
            val = (order_id,)
            mycursor.execute(sql, val)
            result = mycursor.fetchone() #get the result which is packed
            if result is None: #check if packed result is NONE, because unpacking NONE gives the error
                return None
            id_exist, = result #unpacking the result, 
            id_exist = bool(id_exist)
            if not id_exist:
                return None
            sql = ("DELETE FROM orders WHERE ID = %s")
            mycursor.execute(sql,val)
            mydb.commit()
            return id_exist
        except:
            return None
    
    def update_order(self, order_to_be_updated_id: int ,new_values: OrderValues):
        try:    
            sql = "SELECT EXISTS(SELECT 1 FROM orders WHERE id = %s)"
            val = (order_to_be_updated_id,)
            mycursor.execute(sql, val)
            result = mycursor.fetchone() #get the result which is packed
            if result is None: #check if packed result is NONE, because unpacking NONE gives the error
                return None
            id_exist, = result #unpacking the result, 
            id_exist = bool(id_exist)
            if not id_exist:
                return None
            sql2 = ("UPDATE orders SET user_id = %s, street_name = %s, postal_code = %s, city = %s,"
                    "date_of_order = %s, total_price = %s, tax = %s WHERE ID = %s")
            val2 = (new_values.user_id, new_values.street_name, new_values.postal_code, new_values.city,
                    new_values.date_of_order, new_values.total_price, new_values.tax, order_to_be_updated_id)
            mycursor.execute(sql2,val2)
            mydb.commit()
            
            sql3 = "SELECT user_id, street_name, postal_code, city, date_of_order, total_price, tax FROM orders WHERE ID = %s"
            #val = (user_to_be_updated_id,)
            mycursor.execute(sql3, val)
            order = mycursor.fetchone()
            new_order = Order(id=order[0], user_id=order[1], street_name=order[2], postal_code=order[3], city=order[4],
                              date_of_order=order[5], total_price=order[6], tax=order[7]) if order is not None else None
            return new_order
        except:
            return None