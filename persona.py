import conexion as con

def save(persona):
    try:
        db = con.conectar()
        miCursor=db.cursor()
        
        columnas=tuple(persona.keys())
        valores=tuple(persona.values())
        sql="INSERT INTO personas {campos} VALUES(?,?,?,?,?,?)".format(campos = columnas)
        miCursor.execute(sql,(valores))
        creada = miCursor.rowcount>0
        db.commit()
        miCursor.close()
        db.close()
        if creada:
            return{"respuesta":True,"mensaje":"Persona registrada"}
        else:
            return{"respuesta":False,"mensaje":"No se logro registrar a la perona"}
        
    except Exception as ex:
        miCursor.close()
        db.close()
        return{"respuesta":False,"mensaje":str(ex)}
    
def findAll():
    try:
        db = con.conectar()
        miCursor=db.cursor()
        miCursor=db.execute("SELECT*FROM personas ORDER BY nombre")
        personas=miCursor.fetchall()
        if personas:
            miCursor.close()
            db.close()
            return{"respuesta":True,"personas":personas,"mensaje":"lista de personas con exito"}

        miCursor.close()
        db.close()
        return{"respuesta":False,"mensaje":"No hay personas"}
    except Exception as ex:
        miCursor.close()
        db.close()
        return{"respuesta":False,"mensaje":str(ex)}
    
    
    
    """ bloque de codigo para buscar a una perosna"""
def find(dni):
    try:
        db=con.conectar()
        miCursor=db.cursor()
        miCursor.execute("SELECT* From personas WHERE dni="+dni)
        resultado=miCursor.fetchall()
        
        if resultado:
            info=resultado[0]
            persona={"id":info[0],"dni":info[1],"edad":info[2],"nombre":info[3],"apellido":info[4],"direccion":info[5],"correo":info[6]}
            miCursor.close()
            db.close()
            return {"respuesta":True,"persona":persona,"mensaje":"Consultado con exito"}
        else:
            miCursor.close()
            db.close()
            return{"respuesta":False,"mensaje":"No existe la persona"}
    except Exception as ex:
        miCursor.close()
        db.close()
        return{"respuesta":False,"mensaje":str(ex)}
    


def update (persona):
    try:
        db = con.conectar()
        miCursor=db.cursor()
        dniPersona = persona.get("dni")
        persona.pop("dni")
        valores=tuple(persona.values())
        sql="""" UPDATE personas SET edad=?,nombre=?,apellido=?,direccion=?,correo=?
        WHERE dni={dni}""",format(dni=dniPersona)
        miCursor.execute(sql(valores))
        modificado = miCursor.rowcount>0
        db.commit
        miCursor.close()
        db.close()
        if modificado:
            return{"respuesta":True,"mensaje":"Persona actualizada"}
        else:
            return{"respuesta":False,"mensaje":"No existe la persona con ese DNI"}
    except Exception as ex:
        miCursor.close()
        db.close()
        return{"respuesta":False,"mensaje":str(ex)}
