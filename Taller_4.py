import sqlite3
con = sqlite3.connect("DataBase.db")
cur = con.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT,name TEXT, email TEXT)""")
con.commit()
def create_users(name,email):
    cur.execute("INSERT INTO users(name,email) VALUES (?,?)",(name,email))
    con.commit()
def leer_users():
    cur.execute("SELECT * FROM users")
    return cur.fetchall()
def actualizar_users(id,name,email):
    cur.execute("UPDATE users SET name =?, email=? WHERE id =?",(name,email,id))
    con.commit()
def borrar_users(id):
    cur.execute("DELETE FROM users WHERE id =?",(id,))
    con.commit()
    
while True:
    x=int(input("""Que te gustaria hacer en la base de datos.
    0.Cerrar el programa
    1.Crear un usuario
    2.Mostrar Base de datos
    3.Actualizar informacion de un usuario
    4.Borrar Usuario
    Que te gustaria hacer? 
                """))
    if x==0:
        print("Muchas gracias por usar nuestra aplicacion")
        break
    elif x==1:
        datos=list(input("Para añadir un usuario tienes que escribir el nombre y email separado por una , ").split(","))
        create_users(datos[0].strip(), datos[1].strip())
        continue
    elif x==2:
        print(leer_users())
        continue
    elif x==3:
        datos=list(input("Dame el id nombre y email todos separados por , ").split(","))
        actualizar_users(int(datos[0]), datos[1].strip(), datos[2].strip())
        continue
    elif x==4:
        datos=int(input("Que usuario quiere borrar? "))
        borrar_users(datos)
        continue
    else:
        print("Opcion invalida")
        continue
    
con.close()