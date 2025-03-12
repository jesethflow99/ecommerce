import pymysql
import pymysql.cursors
from colorama import Fore,init
import config
init(autoreset=True)

try:
    conn=pymysql.connect(host="localhost",user="root",port=3306,database="ecommerce",)
    cur=conn.cursor()

    if conn:
        print(Fore.GREEN + "conexion exitosa")

    def ver_clientes():
        conn=pymysql.connect(**config.DB_CONFIG,cursorclass=pymysql.cursors.DictCursor)
        cur=conn.cursor()

        cur.execute("SELECT * FROM cliente")
        lista=cur.fetchall()
        conn.close()
        cur.close()
        return lista

    def ver_cliente(id):
        conn=pymysql.connect(**config.DB_CONFIG,cursorclass=pymysql.cursors.DictCursor)
        cur=conn.cursor()

        cur.execute("SELECT * FROM cliente where ID = %s",id)
        cliente=cur.fetchall()
        conn.close()
        cur.close()
        return cliente
    

except Exception as e:
    print(Fore.RED + "no se pudo conectar ",e)


var=ver_cliente(3)




