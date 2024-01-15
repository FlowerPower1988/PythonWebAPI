import mysql.connector
import sys
from ...abstraction.repositories.product_repository_interface import IProductRepository
from ...model.product import Product, ProductValues

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
    
class ProductMysqlRepository(IProductRepository):
    def read_products(self):
        try:
            mycursor.execute("SELECT * FROM products")
            products = mycursor.fetchall()
            product_list=[]
            for product in products:
                new_product = Product(id=product[0], name=product[1], price=product[2])
                product_list.append(new_product)
            return product_list
        finally:
            if mycursor:
                mycursor.close()
            if mydb.is_connected():
                mydb.close()
    
    def read_product(self, product_id: int):
        try:
            sql = "SELECT * FROM products WHERE ID = %s"
            val = (product_id,)
            mycursor.execute(sql, val)
            product = mycursor.fetchone()
            if product is None:
                return None
            new_product = Product(id=product[0], name=product[1], price=product[2])
            return new_product
        except:
            return None
        finally:
            if mycursor:
                mycursor.close()
            if mydb.is_connected():
                mydb.close()
    
    def create_product(self, new_product_values: ProductValues):
        try:
            sql = "INSERT INTO products(product_name, price) values(%s, %s)"
            val = (new_product_values.name, new_product_values.price)
            mycursor.execute(sql, val)
            mydb.commit()
            
            mycursor.execute("SELECT LAST_INSERT_ID();")
            last_id = mycursor.fetchone()
            if last_id is not None and isinstance(last_id[0], int):
                last_id_int : int = last_id[0]
            mycursor.execute("SELECT * FROM products WHERE ID = %s", (last_id_int,))
            product = mycursor.fetchone()
            new_product = Product(id=product[0], name=product[1], price=product[2]) if product is not None else None
            return new_product
        
        finally:
            if mycursor:
                mycursor.close()
            if mydb.is_connected():
                mydb.close()
    
    def delete_product(self, product_id: int):
        try:
            sql = "SELECT EXISTS(SELECT 1 FROM products WHERE id = %s)"
            val = (product_id,)
            mycursor.execute(sql, val)
            result = mycursor.fetchone() #get the result which is packed
            if result is None: #check if packed result is NONE, because unpacking NONE gives the error
                return None
            id_exist, = result #unpacking the result, 
            id_exist = bool(id_exist)
            if not id_exist:
                return None
            
            sql2= ("SELECT EXISTS(SELECT 1 FROM orders_products WHERE product_id = %s)")
            mycursor.execute(sql2, val)
            result2 = mycursor.fetchone()
            if result2 is None: #check if packed result is NONE, because unpacking NONE gives the error
                return None
            id_exist2, = result2 #unpacking the result, 
            id_exist2 = bool(id_exist2)
            if id_exist and not id_exist2:
                sql = ("DELETE FROM products WHERE ID = %s")
                mycursor.execute(sql,val)
                mydb.commit()
                return id_exist
            elif id_exist and id_exist2:
                id_exist=409
                return id_exist
        except:
            return None
        finally:
            if mycursor:
                mycursor.close()
            if mydb.is_connected():
                mydb.close()
    
    def update_product(self, product_to_be_updated_id: int ,new_values: ProductValues):
        try:    
            sql = "SELECT EXISTS(SELECT 1 FROM products WHERE id = %s)"
            val = (product_to_be_updated_id,)
            mycursor.execute(sql, val)
            result = mycursor.fetchone() #get the result which is packed
            if result is None: #check if packed result is NONE, because unpacking NONE gives the error
                return None
            id_exist, = result #unpacking the result, 
            id_exist = bool(id_exist)
            if not id_exist:
                return None
            sql2 = ("UPDATE products SET product_name = %s, price = %s WHERE ID = %s")
            val2 = (new_values.name, new_values.price, product_to_be_updated_id)
            mycursor.execute(sql2,val2)
            mydb.commit()
            
            sql3 = "SELECT id, product_name, price FROM products WHERE ID = %s"
            #val = (user_to_be_updated_id,)
            mycursor.execute(sql3, val)
            product = mycursor.fetchone()
            new_product = Product(id=product[0], name=product[1], price=product[2]) if product is not None else None
            return new_product
        except:
            return None
        finally:
            if mycursor:
                mycursor.close()
            if mydb.is_connected():
                mydb.close()