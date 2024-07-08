# -*- coding: utf-8 -*-
"""
Created on Tue May 21 18:58:03 2024

@author: Aidan
"""

from tkinter import*

root = Tk()
root.title("P177")
root.geometry("600x600")

nombre = Label(root, text="Nombre")
nombre.place(relx=0.5, rely=0.1, anchor=CENTER)

obtener_nombre = Entry(root)
obtener_nombre.place(relx=0.5, rely=0.2)

contraseña = Label(root, text="Contraseña")
contraseña.place(relx=0.5, rely=0.3, anchor=CENTER)

obtener_contra = Entry(root)
obtener_contra.place(relx=0.5, rely=0.4)

captcha = Label(root, text="Captcha")
captcha.place(relx=0.5, rely=0.5, anchor=CENTER)

captcha_e = Entry(root)
captcha_e.place(relx=0.5, rely=0.6, anchor=CENTER)

class userDB:
    def __init__(self):
       self.__userName = "Tiggy"
       self.__contraseña = "TiggyLeviosa2024"
       self.__captcha = "Fer y Tiggy 2017-2024"
       
    def show_user(self):
        nombre["text"] = "Nombre: " + self.__userName
        contraseña["text"] = "Contraseña: " + self.__contraseña
        captcha["text"] = "Captcha: " + self.__captcha
        
objeto = userDB()

def addUser():
    global objeto
    objeto.userName
    objeto.userName = obtener_nombre.get()
    objeto.contraseña
    objeto.contrasña = obtener_contra.get()
    objeto.captcha
    objeto.captcha = obtener_captcha.get()
       
boton = Button(root, text="actualizar", command=addUser)
boton.place(relx=0.5, rely=0.7, anchor=CENTER)

boton2 = Button(root, text="Mostrar perfil", command=show_user)
boton2.place(relx=0.5, rely=0.8, anchor=CENTER)

root.mainloop()
