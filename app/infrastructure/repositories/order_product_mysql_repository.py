import mysql.connector
import sys
from ...abstraction.repositories.order_product_repository_interface import IOrder_productRepository
from ...model.order_product import Order_product, Order_productValues

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
    
class Order_productMysqlRepository(IOrder_productRepository):
    def read_orders_products(self):
        try:
            mycursor.execute("SELECT * FROM orders_products")
            orders_products = mycursor.fetchall()
            orders_products_list=[]
            for order_product in orders_products:
                new_order_product = Order_product(order_id=order_product[0], product_id=order_product[1], amount=order_product[2])
                orders_products_list.append(new_order_product)
            return orders_products_list
        finally:
            if mycursor:
                mycursor.close()
            if mydb.is_connected():
                mydb.close()
    
    def read_order_product(self, order_id: int):
        try:
            sql = "SELECT * FROM orders_products WHERE ID = %s"
            val = (order_id,)
            mycursor.execute(sql, val)
            orders_products = mycursor.fetchall()
            orders_products_list=[]
            for order_product in orders_products:
                new_order_product = Order_product(order_id=order_product[0], product_id=order_product[1], amount=order_product[2])
                orders_products_list.append(new_order_product)
            return orders_products_list
        except:
            return None
        finally:
            if mycursor:
                mycursor.close()
            if mydb.is_connected():
                mydb.close()
    
    def create_order_product(self, new_values: Order_productValues):
        try:
            sql = ("INSERT INTO orders_products(order_id, product_id, amount) values(%s, %s, %s)")
            val = (new_values.order_id, new_values.product_id, new_values.amount)
            mycursor.execute(sql, val)
            mydb.commit()
            new_order_product = Order_product(order_id = new_values.order_id, product_id = new_values.product_id, amount = new_values.amount)
            return new_order_product
        finally:
            if mycursor:
                mycursor.close()
            if mydb.is_connected():
                mydb.close()
    
    def delete_order_product(self, order_id: int, product_id: int):
        try:
            sql = "SELECT EXISTS(SELECT 1 FROM orders_products WHERE order_id = %s AND product_id = %s)"
            val = (order_id, product_id)
            mycursor.execute(sql, val)
            result = mycursor.fetchone() #get the result which is packed
            if result is None: #check if packed result is NONE, because unpacking NONE gives the error
                return None
            id_exist, = result #unpacking the result, 
            id_exist = bool(id_exist)
            if not id_exist:
                return None
            sql = ("DELETE FROM orders_products WHERE order_id = %s AND product_id = %s")
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
    
    def update_order_product(self, order_to_be_updated_id: int, product_to_be_updated_id: int, amount: int):
        try:    
            sql = "SELECT EXISTS(SELECT 1 FROM orders_products WHERE order_id = %s AND product_id = %s)"
            val = (order_to_be_updated_id,product_to_be_updated_id)
            mycursor.execute(sql, val)
            result = mycursor.fetchone() #get the result which is packed
            if result is None: #check if packed result is NONE, because unpacking NONE gives the error
                return None
            id_exist, = result #unpacking the result, 
            id_exist = bool(id_exist)
            if not id_exist:
                return None
            sql2 = ("UPDATE orders_products SET amount = %s WHERE order_id = %s AND product_id = %s")
            val2 = (amount,)
            mycursor.execute(sql2,val2)
            mydb.commit()
            
            sql3 = "SELECT order_id, product_id, amount FROM orders_products WHERE order_id = %s AND product_id = %s"
            #val = (user_to_be_updated_id,)
            mycursor.execute(sql3, val)
            order_product = mycursor.fetchone()
            new_order_product = Order_product(order_id=order_product[0], product_id=order_product[1], amount=order_product[2]) if order_product is not None else None
            return new_order_product
        except:
            return None
        finally:
            if mycursor:
                mycursor.close()
            if mydb.is_connected():
                mydb.close()