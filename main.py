from tkinter import *  #Importar tkinter de https://docs.python.org/es/3/library/tkinter.html #Tkinter libreria GUI de Python
from tkinter import ttk  # importar TKK para darle visualizacion a tkinter
from tkinter import messagebox

import persona as per

ventana=Tk()
ventana.state("zoomed")
ventana.title("aplicacion de escriytorio con bases de datos")

ventana.resizable(0,0)


txt_dni=StringVar()
txt_nombre=StringVar()
txt_apellido=StringVar()
txt_direccion=StringVar()
txt_edad=StringVar()
txt_correo=StringVar()


Label(ventana,text="DNI",width=10,justify="left",anchor="w").grid(row=0,column=0)
Label(ventana,text="Nombre",width=10,justify="left",anchor="w").grid(row=1,column=0)
Label(ventana,text="Apellido",width=10,justify="left",anchor="w").grid(row=2,column=0)
Label(ventana,text="Direccion",width=10,justify="left",anchor="w").grid(row=3,column=0)
Label(ventana,text="Correo",width=10,justify="left",anchor="w").grid(row=4,column=0)
Label(ventana,text="Edad",width=10,justify="left",anchor="w").grid(row=5,column=0)

e_dni=ttk.Entry(textvariable=txt_dni,width=30)
e_nombre=ttk.Entry(textvariable=txt_nombre,width=30)
e_apellido=ttk.Entry(textvariable=txt_apellido,width=30)
e_direccion=ttk.Entry(textvariable=txt_direccion,width=30)
e_edad=ttk.Entry(textvariable=txt_edad,width=30)
e_correo=ttk.Entry(textvariable=txt_correo,width=30)

e_dni.grid(row=0,column=1,pady=2)
e_nombre.grid(row=1,column=1,pady=2)
e_apellido.grid(row=2,column=1,pady=2)
e_direccion.grid(row=3,column=1,pady=2)
e_correo.grid(row=4,column=1,pady=2)
e_edad.grid(row=5,column=1,pady=2)


e_dni.focus()


################### FUNCIONES #########################

# Funcion guardar

def guardar():
    if txt_edad.get().isnumeric():
        persona = {"dni":txt_dni.get(),"nombre":txt_nombre.get(),"apellido":txt_apellido.get(),"direccion":txt_direccion.get(),"correo":txt_correo.get(),"edad":int(txt_edad.get())}
        res = per.save(persona)
        messagebox.showinfo("Persona Registrada",res.get("mensaje"))
    else:
        messagebox.showerror("upps!!","La edad debe ser numerica")


# Funcion Consultar


def consultar():
    if txt_dni.get()=="": #comillas indican que esta vacio el campo
        messagebox.showerror("upps!!","Debe indicar el DNI")
        e_dni.focus()
    else:
        res=per.find(txt_dni.get())
        if(res.get("respuesta")):
            persona=dict(res.get("persona"))
            txt_nombre.set(persona.get("nombre"))
            txt_apellido.set(persona.get("apellido"))
            txt_direccion.set(persona.get("direccion"))
            txt_correo.set(persona.get("correo"))
            txt_edad.set(persona.get("edad"))
        else:
            messagebox.showwarning("upps!!","No se encontro la persona con ese DNI")
            e_dni.focus()



#Funcion Actualizar

def actualizar():
    if txt_edad.get().isnumeric():
        persona = {"dni":txt_dni.get(),"nombre":txt_nombre.get(),"apellido":txt_apellido.get(),"direccion":txt_direccion.get(),"correo":txt_correo.get(),"edad":int(txt_edad.get())}
        res = per.update(persona)

        if res.get('respuesta'):
            messagebox.showinfo("OK",res.get('mensaje'))

        else:
            messagebox.showerror("Upss","No se logro actualizar:"+res.get('mensaje'))

    else:
        txt_edad.set("")
        e_edad.focus()
        messagebox.showerror("Upps!!","La edad debe ser un numero")
 
        



################# BOTONES #################################

ttk.Button(ventana,text="Guardar",command=guardar).place(x=10,y=170)
ttk.Button(ventana,text="Consultar",command=consultar).place(x=120,y=170)
ttk.Button(ventana,text="Actualizar",command=actualizar).place(x=230,y=170)
ttk.Button(ventana,text="Eliminar",command=None).place(x=340,y=170)





ventana.mainloop() #Actualizar la ventana - poner al final del codigo
