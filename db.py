import pymysql
import pymysql.cursors
from colorama import Fore,init
import config
init(autoreset=True)


class Database:
    def __init__(self):
        self.conn=None
        self.cur=None

    def __enter__(self):
        try:
            self.conn=pymysql.connect(**config.DB_CONFIG)
            self.cur = self.conn.cursor(pymysql.cursors.DictCursor)
            return self.cur
        except Exception as e:
            print(Fore.RED+f"no se pudo conectar a la base de datos {e}")
    
    def __exit__(self,exc_type, exc_value, traceback):

        if exc_type is None and self.conn:
            self.conn.commit()
        if self.cur:
            self.cur.close()
        if self.conn:
            self.conn.close()
        return False



class Cliente:
    def __init__(self,nombre,numero,correo,direccion):
        self.nombre=nombre
        self.numero=numero
        self.correo=correo
        self.direccion=direccion

    def CREATE(self):
        try:
            with Database() as cur: 
                sql = """
                    INSERT INTO cliente(correo, numero_contacto, nombre, cp, cuidad, calle, numero) 
                    VALUES (%s, %s, %s, %s, %s, %s, %s)
                """  
                valores = (
                    self.correo,
                    self.numero,
                    self.nombre,
                    self.direccion["cp"],
                    self.direccion["cuidad"],
                    self.direccion["calle"],
                    self.direccion["numero"]
                ) 

                cur.execute(sql, valores) 

        except Exception as e:
            print(Fore.RED + f"Error al agregar: {e}") 

    @classmethod
    def READ_ALL(cls):
        with Database() as cur:
            cur.execute("SELECT * FROM cliente")
            lista=cur.fetchall()
            return lista

    @classmethod
    def READ_ONE(cls,id):
        with Database() as cur:
            cur.execute("SELECT * FROM cliente where id = %s",id)
            cliente=cur.fetchall()
            return cliente
        
    @classmethod    
    def UPDATE(cls, datos):
        try:
            with Database() as cur:
                id_cliente = datos.pop("id", None)
                if id_cliente is None:
                    print("Error: No se proporcionó un ID.")
                    return
                
                columnas = ", ".join(f"{key} = %s" for key in datos.keys())

                sql = f"UPDATE cliente SET {columnas} WHERE id = %s"

                valores = list(datos.values()) + [id_cliente]
                cur.execute(sql, valores)

                print("Registro actualizado correctamente.")

        except Exception as e:
            print(f"Error al actualizar: {e}")

    
    @classmethod
    def DELETE(cls,id):
        with Database() as cur:
            cur.execute("DELETE FROM cliente where id = %s",id)
            print("cliente eliminado...")



class Producto:
    def __init__(self,precio,color,nombre,categoria):
        self.precio=precio
        self.color=color
        self.nombre=nombre
        self.categoria=categoria


    def CREATE(self):
        with Database() as cur:
            sql="INSERT INTO producto(precio,color,nombre,categoria) values(%s,%s,%s,%s)"
            lista=(self.precio,self.color,self.nombre,self.categoria)
            cur.execute(sql,lista)
            print("producto agregado")


    @classmethod
    def READ_ALL(cls):
        with Database() as cur:
            cur.execute("SELECT * FROM producto")
            lista=cur.fetchall()
            return lista


    @classmethod
    def READ_ONE(cls,id):
        with Database() as cur:
            cur.execute("SELECT * FROM producto WHERE id = %s",id)
            lista=cur.fetchall()
            return lista
        

    @classmethod
    def UPDATE(cls,datos):
        try:
            with Database() as cur:
                id_producto = datos.pop("id", None)
                if id_producto is None:
                    print("Error: No se proporcionó un ID.")
                    return
                
                columnas = ", ".join(f"{key} = %s" for key in datos.keys())

                sql = f"UPDATE producto SET {columnas} WHERE id = %s"

                valores = list(datos.values()) + [id_producto]
                cur.execute(sql, valores)

                print("Registro actualizado correctamente.")

        except Exception as e:
            print(f"Error al actualizar: {e}")

    @classmethod
    def DELETE(cls,id):
        with Database() as cur:
            cur.execute("DELETE FROM producto where id = %s",id)
            print("producto eliminado...")

    class Ventas:
        def __init__(self,cliente,ticket,producto,cantidad):
            self.cliente=cliente
            self.ticket=ticket
            self.producto=producto
            self.cantidad=cantidad

        def CREATE(self):
            with Database() as cur:
                sql="INSERT INTO ventas(cliente,ticket,producto,cantidad) values(%s,%s,%s,%s)"
                lista=(self.cliente,self.ticket,self.producto,self.cantidad)
                cur.execute(sql,lista)
                print("venta agregada")
            
        @classmethod
        def READ_ALL(cls):
            with Database() as cur:
                cur.execute("SELECT * FROM ventas")
                lista=cur.fetchall()
                return lista
        
        @classmethod
        def READ_ONE(cls,id):
            with Database() as cur:
                cur.execute("SELECT * FROM ventas WHERE id = %s",id)
                lista=cur.fetchall()
                return lista
        
        @classmethod
        def UPDATE(cls,datos):
            try:
                with Database() as cur:
                    id_venta = datos.pop("id", None)
                    if id_venta is None:
                        print("Error: No se proporcionó un ID.")
                        return
                    
                    columnas = ", ".join(f"{key} = %s" for key in datos.keys())

                    sql = f"UPDATE ventas SET {columnas} WHERE id = %s"

                    valores = list(datos.values()) + [id_venta]
                    cur.execute(sql, valores)

                    print("Registro actualizado correctamente.")

            except Exception as e:
                print(f"Error al actualizar: {e}")
            
        @classmethod
        def DELETE(cls,id):
            with Database() as cur:
                cur.execute("DELETE FROM ventas where id = %s",id)
                print("venta eliminada...")

        