import sqlite3 #Es un conector estamos importando. Un conector
def conectar():
    miconexion=sqlite3.connect("sistema_db")
    micursor=miconexion.cursor() #Cursor: Herramienta obligatoria para acceder a los datos (abre y recorre)
    
    try:
        micursor.execute("""
        CREATE TABLE IF NOT EXISTS personas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        dni VARCHAR(15) NOT NULL UNIQUE,
        edad INTEGER NOT NULL,
        nombre VARCHAR (50),
        apellido VARCHAR (50),
        direccion VARCHAR (20),
        correo VARCHAR (50) UNIQUE
        )
        """)
        
        print ("BBDD creada con exito")
        micursor.close()
        return miconexion
    except Exception as ex:
        print("Error de Conexion:",ex)
        micursor.close()
    return miconexion
