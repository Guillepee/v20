# -*- coding: utf-8 -*-
"""
Created on Fri Jan  6 10:45:21 2023

@author: guillermo.palmieri
"""


from tkinter import *
from tkinter import ttk
import random
import pickle, json
import os, copy
from tkinter import filedialog as FileDialog


datos= {"nombre":    ["",1,0], "jugador":    ["",2,0],  "cronica": ["",3,0],
        "naturaleza":["",1,8], "conducta":   ["",2,8],  "concepto":["",3,8],
        "clan":      ["",1,14],"generacion": ["",2,14], "sire":    ["",3,14]}

caracteristicas= {"Fuerza":    [1,1,1], "Destreza":    [1,2,1],"Resistencia":[1,3,1],
                  "Carisma":   [1,1,8], "Manipulación":[1,2,8],"Apariencia":[1,3,8],
                  "Percepción":[1,1,14],"Inteligencia":[1,2,14],"Astucia":[1,3,14]}

#Creo un diccionario con las filas y columnas donde debe arrancar cada habilidad, en la lista [valor, fila, columna]
habilidades= {"Alerta":[0,2,1],"Atletismo":[0,3,1],"Callejeo":[0,4,1],"Conciencia":[0,5,1],"Empatia":[0,6,1],"Expresion":[0,7,1],
              "Intimidacion":[0,8,1],"Liderazgo":[0,9,1],"Pelea":[0,10,1],"Subterfugio":[0,11,1],"Arma de Fuego":[0,2,8],
              "Artesania":[0,3,8],"Conducir":[0,4,8],"Etiqueta":[0,5,8],"Interpretacion":[0,6,8],"Latrocinio":[0,7,8],
              "Pelea con Armas":[0,8,8],"Sigilo":[0,9,8],"Supervivencia":[0,10,8],"Trato C. Animales":[0,11,8],"Academicismo":[0,2,14],
              "Ciencia":[0,3,14],"Finanzas":[0,4,14],"Informatica":[0,5,14],"Investigacion":[0,6,14],"Leyes":[0,7,14],
              "Medicina":[0,8,14],"Ocultismo":[0,9,14],"Politica":[0,10,14],"Tecnologia":[0,11,14]}

nombres_disciplinas = ["Animalismo","Auspex","Celeridad","Quimerismo","Dementacion","Dominación","Fortaleza","Ofuscación",
                       "Obtenebration","Necromancia","Potencia","Presencia","Protean","Temporis","Serpentis",
                       "Taumaturgia","Vicisitud","Extincion"]

nombres_trasfondos = ["Aliados","Contactos","Criados","Fama","Generación","Rebaño","Influencia","Mentor","Posicion","Recursos",
                      "Dominio"]

disciplinas = {"disciplina1":  [0,2,1,""],"disciplina2":  [0,3,1,""],"disciplina3":[0,4,1,""]
              ,"disciplina4":  [0,5,1,""],"disciplina5":  [0,6,1,""],}

trasfondos = {"trasfondo1":   [0,2,8,""],"trasfondo2":  [0,3,8,""],"trasfondo3":[0,4,8,""],
              "trasfondo4":   [0,5,8,""],"trasfondo5":  [0,6,8,""]}

#LISTAS COPIAS PARA QUE LABUREN CUANDO ABRO UNA FICHA NUEVA
datos_base           = copy.deepcopy(datos)
caracteristicas_base = copy.deepcopy(caracteristicas)
habilidades_base     = copy.deepcopy(habilidades)
disciplinas_base     = copy.deepcopy(disciplinas)
trasfondos_base      = copy.deepcopy(trasfondos)

#EN ESTAS LISTAS ESTAN LOS OBJETOS, DE DONDE TENGO QUE CONSULTAR LOS VALORES. 
obj_datos           = {}
obj_caracteristicas = {}
obj_habilidades     = {}
obj_disciplinas     = {}
obj_transfonodos    = {}

ruta = ""

lista_madre = [datos,caracteristicas,habilidades,disciplinas,trasfondos]

root = Tk()
frame_datos = Frame(root)
frame_datos.grid(row=10,column=0)

frame_caracteristicas = Frame(root)
frame_caracteristicas.grid(row=20,column=0)

frame_otras_tiradas = Frame(root)
frame_otras_tiradas.grid(row=20,column=1)

frame_habilidades = Frame(root)
frame_habilidades.grid(row=30,column=0)

frame_tiradas = Frame(root)
frame_tiradas.grid(row=10,column=1) #FILA 10 PERO COLUMNA 1, AL COSTADO

frame_ventajas = Frame(root)
frame_ventajas.grid(row=40,column=0)

def distribucion_datos(lista,lista_base,ubicacion,tipo) :
    global datos
    
    #TITULO
    datos_label = Label(root)
    datos_label.grid(row=9,column=0,sticky="w",padx=2.5, pady=2.5)
    datos_label.config(font=("Arial",12),text="                                                                          La Mascarada")
    
    #DISTRIBUCION
    for key,valores in lista_base.items():
        obj_datos[key] = Crear_objeto(ubicacion,key,valores[1],valores[2],valores[0],tipo)
        
def almacenar_info(event):
    global datos
    
    pass

#FUNCION Y CLASE: CADA LABEL Y CHECKBUTTON CREADA DENTRO DE UN OBJETO CON EL NOMBRE "FUERZA", "DESTREZA", ETC
def distribucion_atributo(lista,lista_base,ubicacion,tipo):
    #TITULO
    caracteristicas_label = Label(root)
    caracteristicas_label.grid(row=19,column=0,sticky="w",padx=2.5, pady=2.5)
    caracteristicas_label.config(font=("Arial",12),text="                                                                               Atributos")
    #DISTRIBUCION Y CREACION DE OBJETOS
    for key,valores in lista_base.items():
        obj_caracteristicas[key] = Crear_objeto(ubicacion,key,valores[1],valores[2],valores[0],tipo)

#FUNCION Y CLASE: CADA LABEL Y CHECKBUTTON CREADA DENTRO DE UN OBJETO CON EL NOMBRE "ATLETISMO", "LIDERAZGO", ETC
def distribucion_habilidades(lista,lista_base,ubicacion,tipo):
    #TITULO
    habilidades_label = Label(root)
    habilidades_label.grid(row=29,column=0,sticky="w",padx=2.5, pady=2.5)
    habilidades_label.config(font=("Arial",12),text="                                                                             Habilidades")
    #DISTRIBUCION Y CREACION DE OBJETOS
    for key,valores in lista_base.items():
        obj_habilidades[key] = Crear_objeto(ubicacion,key,valores[1],valores[2],valores[0],tipo)
  
def distribucion_disciplinas(lista,lista_base,ubicacion,tipo,nombres_disciplinas):
    #TITULO
    disciplinas_label = Label(root)
    disciplinas_label.grid(row=39,column=0,sticky="w",padx=2.5, pady=2.5)
    disciplinas_label.config(font=("Arial",12),text="                                                                                 Ventajas")
    #DISTRIBUCION Y CREACION DE OBJETOS
    for key,valores in lista_base.items():
        obj_disciplinas[key] = Crear_objeto(ubicacion,key,valores[1],valores[2],valores[0],tipo,valores[3],nombres_disciplinas)
        
def distribucion_trasfondos(lista,lista_base,ubicacion,tipo,nombres_trasfondos):
    #TITULO
    
    #DISTRIBUCION Y CREACION DE OBJETOS
    for key,valores in lista_base.items():
        obj_trasfondos[key] = Crear_objeto(ubicacion,key,valores[1],valores[2],valores[0],tipo,valores[3],nombres_trasfondos)
        
class Crear_objeto:
    
    def __init__(self, ubicacion, nombre, fila, col,puntaje,tipo,nom_disci=None,variante=None):
        self.ubicacion = ubicacion
        self.nombre = nombre
        self.fila = fila
        self.col = col
        self.puntaje = puntaje
        self.tipo = tipo
        self.nom_disci = nom_disci
        self.variante = variante
  
        self.valor = IntVar()
        self.valor.set(self.puntaje)  
        self.text = StringVar()
        self.disci = StringVar()
        #self.text = StringVar(value=self.puntaje)
        #self.text.set(self.puntaje)

        if self.tipo == 0:
            label= Label(self.ubicacion, text=self.nombre)
            label.grid(row=self.fila, column=self.col, sticky="w", padx=5, pady=2.5)
            label.bind("<Button-1>", on_click_label)
            
            a=Checkbutton(self.ubicacion, onvalue=1, offvalue=0,variable=self.valor)
            a.grid(row=self.fila, column=self.col+1)
            a.bind("<Button-1>", on_click_checkbutton)
            
            b=Checkbutton(self.ubicacion, onvalue=2, offvalue=0,variable=self.valor)
            b.grid(row=self.fila, column=self.col+2)
            b.bind("<Button-1>", on_click_checkbutton)
            
            c=Checkbutton(self.ubicacion, onvalue=3, offvalue=0,variable=self.valor)
            c.grid(row=self.fila, column=self.col+3)
            c.bind("<Button-1>", on_click_checkbutton)
            
            d=Checkbutton(self.ubicacion, onvalue=4, offvalue=0,variable=self.valor)
            d.grid(row=self.fila, column=self.col+4)
            d.bind("<Button-1>", on_click_checkbutton)
            
            e=Checkbutton(self.ubicacion, onvalue=5, offvalue=0,variable=self.valor)
            e.grid(row=self.fila, column=self.col+5)
            e.bind("<Button-1>", on_click_checkbutton)
            
        elif self.tipo == 1:
            desplegable = ttk.Combobox(self.ubicacion,textvariable=self.disci,values=self.variante)
            desplegable.grid(row=self.fila,column=self.col)
            desplegable.set(self.nom_disci)
            
            a=Checkbutton(self.ubicacion, onvalue=1, offvalue=0,variable=self.valor)
            a.grid(row=self.fila, column=self.col+1)
            a.bind("<Button-1>", on_click_checkbutton)
            
            b=Checkbutton(self.ubicacion, onvalue=2, offvalue=0,variable=self.valor)
            b.grid(row=self.fila, column=self.col+2)
            b.bind("<Button-1>", on_click_checkbutton)
            
            c=Checkbutton(self.ubicacion, onvalue=3, offvalue=0,variable=self.valor)
            c.grid(row=self.fila, column=self.col+3)
            c.bind("<Button-1>", on_click_checkbutton)
            
            d=Checkbutton(self.ubicacion, onvalue=4, offvalue=0,variable=self.valor)
            d.grid(row=self.fila, column=self.col+4)   
            d.bind("<Button-1>", on_click_checkbutton)
            
            e=Checkbutton(self.ubicacion, onvalue=5, offvalue=0,variable=self.valor)
            e.grid(row=self.fila, column=self.col+5)
            e.bind("<Button-1>", on_click_checkbutton)
            
        elif self.tipo == 2:
             #LABES Y ENTRYS DE NOMBRE,JUGADOR,CRONICA, 
             Label(self.ubicacion,text=self.nombre.capitalize()).grid(row=self.fila,column=self.col)
             
             #self.text = StringVar(name=self.nombre,value=self.puntaje)
             entry = Entry(self.ubicacion,textvariable=self.text)
             entry.grid(row=self.fila,column=self.col+1)
             entry.insert(0,self.puntaje)
             print(self.puntaje)
             entry.bind("<Return>", almacenar_info)
             
        return

def distribucion_tiradas(ubicacion):
    global monitor_caracteristica,monitor_habilidades,dado1,dado2,monitor_exitos,monitor_tirada,dificultad
    #TITULO
    tirada_label = Label(root)
    tirada_label.grid(row=9,column=1,sticky="w",padx=2.5, pady=2.5)
    tirada_label.config(font=("Arial",12),text="        Tirada de Dados")
    #DADO DE CARACTERISTICA, ACCIONA CON EL ENTER COMENTANDO LA CANTIDAD DE DADOS DE LA CARACTESTICA ELEGIDA
    dado1 = Label(ubicacion)
    dado1.grid(row=6,column=1)
    dado1_label = Label(ubicacion)
    dado1_label.grid(row=6,column=0)
    dado1_label.config(text="Atributo: ")
    #LABEL "VACIO" AL LADO DE LA CARACTERISTICA SELECCIONADA QUE TOMA VALOR CUANDO SE APRETA ENTER
    monitor_caracteristica = Label(ubicacion)
    monitor_caracteristica.grid(row=6,column=2)
    #DADO DE HABILIDAD, ACCIONA CON EL ENTER COMENTANDO LA CANTIDAD DE DADOS DE LA CARACTESTICA ELEGIDA
    dado2 = Label(ubicacion)
    dado2.grid(row=7,column=1)
    dado2_label = Label(ubicacion)
    dado2_label.grid(row=7,column=0)
    dado2_label.config(text="Habilidad: ")
    #LABEL "VACIO" AL LADO DE LA HABILIDAD SELECCIONADA QUE TOMA VALOR CUANDO SE APRETA ENTER
    monitor_habilidades = Label(ubicacion)
    monitor_habilidades.grid(row=7,column=2)
    #CREO EL LABEL DIFICULTAD, PARA QUE EL USUARIO INGRESE LA DIFICULTAD DE LA TIRADA
    dificultad = Entry(ubicacion)
    dificultad.grid(row=8,column=1)
    dificultad.insert(0, 6)
    dificultad.config(justify="center")
    dificultad_label = Label(ubicacion)
    dificultad_label.grid(row=8,column=0)
    dificultad_label.config(text="Dificultad: ")
    #CREO EL LABEL RESULTADO,DONDE FIGURA EL NUMEROS QUE SALIERON EN LA TIRADA DE DADOS.
    resultado = Label(ubicacion)
    resultado.grid(row=9,column=1)
    resultado_label = Label(ubicacion)
    resultado_label.grid(row=9,column=0)
    resultado_label.config(text="Resultado: ")
    monitor_exitos = Label(ubicacion)
    monitor_exitos.grid(row=9,column=2)
    monitor_tirada= Label(frame_tiradas)
    monitor_tirada.grid(row=9,column=1)
    #BOTON "TIRAR DADOS"
    tirar = Button(root,text="TIRAR DADOS!",command=tirada)
    tirar.grid(row=19,column=1)

def otras_tiradas(ubicacion):
    global valor_iniciativa, resultado_iniciativa
    
    valor_iniciativa = StringVar()

    Button(ubicacion,text="Iniciativa",command=iniciativa).grid(row=1,column=0)
    resultado_iniciativa=Label(ubicacion,textvariable=valor_iniciativa)
    resultado_iniciativa.grid(row=2,column=0)

#CALCULA LA INICIATIVA, CON 1d10 + DES + AST --- FALTA SUMARLE LA CELERIDAD
def iniciativa():   

    global d
    a = int(random.randint(1, 10))
    b = obj_caracteristicas["Destreza"].valor.get()
    c = obj_caracteristicas["Astucia"].valor.get()
    d = 0
    
    for nombre,dato in obj_disciplinas.items():
        if dato.disci.get() == "Celeridad":
            d= int(dato.valor.get())

    #print(obj_disciplinas["disciplina1"].disci.get())
    #print(obj_disciplinas["disciplina1"].valor.get())
    
    ini = a+b+c+d
    if d == 0:
        valor_iniciativa.set(f"Des({b}) + Ast({c}) + 1d10({a}) = {ini}")
    else:
        valor_iniciativa.set(f"Des({b}) + Ast({c}) + Cel({d}) + 1d10({a}) = {ini}")
        
    resultado_iniciativa.config(text=ini)
    
#CLIC LABEL , LLEVA EL NOMBRE Y LA PUNTUACION AL SECTOR "TIRADA"
def on_click_label(event):
    global monitor_caracteristica
    global nombre_caracteristica
    label = event.widget  # Obtiene el objeto Label que ha generado el evento
    nombre_caracteristica = label.cget("text")  # Obtiene el texto del Label
    print(nombre_caracteristica)
    
    #Busca en la lista caracteristica [Fuerza].puntaje
    if nombre_caracteristica in caracteristicas:
        monitor_caracteristica.config(text=obj_caracteristicas[nombre_caracteristica].valor.get())
        dado1.config(text=nombre_caracteristica)        
    else:
    #Busca en la lista habilidades [Pelea].puntaje
        monitor_habilidades.config(text=obj_habilidades[nombre_caracteristica].valor.get())
        dado2.config(text=nombre_caracteristica)
    
#CLIC boton , CADA VEZ QUE SE MODIFICA UN VALOR, TIENE QUE ALMACENARLO
def on_click_checkbutton(event):
    """
    global caracteristicas
    print (event.widget.cget("onvalue"))
    
    for clave, objeto in obj_caracteristicas.items():
        #print(caracteristicas[clave])
        caracteristicas[clave][0]= objeto.valor.get()
        #print(objeto.valor.get())
    """

def tirada():
    cantidad_dados = (monitor_caracteristica.cget("text"))+monitor_habilidades.cget("text")
    resultado = random.sample(range(1,11),cantidad_dados)
    monitor_tirada.config(text=resultado)
    
    dificultad_tirada = dificultad.get()
    exitos = 0
    unos= 0
    #LOGICA DE TIRADA DE DADOS CON EXITOS, FALLOS Y FRACASOS
    for n in resultado:
        if n >= int(dificultad_tirada):
            exitos += 1
        elif n == 1:
            unos += 1

    if (exitos-unos) == 0:
        exitos = "Fallo"
    elif exitos == 0 and unos >= 1:
        exitos = "FRACAAASOO"
    else:
        exitos = f"{str(exitos-unos)} exito/s"
            
    monitor_exitos.config(text=str(exitos),font=("Arial", 9, "bold"))    

def nuevo():

#EJECUTO LAS FUNCIONES QUE HACEN FUNCIONAR EL PROGRAMA
#ME FUNCIONA SI HAGO UNA NUEVA, PERO SI QUIERO ABRIR UNA NUEVA CON UNA YA ABIERTA NO HACE NADA

    distribucion_datos(datos,datos_base,frame_datos,2)
    distribucion_atributo(caracteristicas,caracteristicas_base,frame_caracteristicas,0)
    distribucion_habilidades(habilidades,habilidades_base,frame_habilidades,0)
    distribucion_tiradas(frame_tiradas)
    distribucion_disciplinas(disciplinas,disciplinas_base,frame_ventajas,1,nombres_disciplinas)
    otras_tiradas(frame_otras_tiradas)
    distribucion_trasfondos(trasfondos,trasfondos_base,frame_ventajas,1,nombres_trasfondos)
    
    # EJECUTO EL LOOP PARA VER LA PANTALLA
    root.mainloop()
    
def abrir():
    global ruta, datos, caracteristicas, habilidades,ruta,lista_madre,disciplinas,trasfondos

    #Selecciono el archivo para desp extraerle la ruta y abrirlo
    archivo = FileDialog.askopenfile(initialdir=".", 
                                      filetypes=(("Fichas de V20 ", "*.pckl"),), 
                                      title = "Abrir ficha de V20.")
    
    ruta = archivo.name #AL LLAMAR AL ATRIBUTO NAME ME QUEDO CON LA RUTA REAL
    # AL USAR EL WITH NO NECESITO USAR EL CLOSE(), XQ CUANDO FINALIZA EL WITH CIERRA AUTOMATICAMENTE
    with open (ruta,"rb") as ficha:
        lista_madre = pickle.load(ficha)
    
    datos                 = lista_madre[0]
    caracteristicas       = lista_madre[1]
    habilidades           = lista_madre[2]
    disciplinas           = lista_madre[3]
    trasfondos            = lista_madre[4] 
    print(disciplinas)
    
    #LISTAS COPIAS PARA QUE LABUREN CUANDO ABRO UNA FICHA NUEVA
    datos_base           = copy.deepcopy(datos)
    caracteristicas_base = copy.deepcopy(caracteristicas)
    habilidades_base     = copy.deepcopy(habilidades)
    disciplinas_base     = copy.deepcopy(disciplinas)
    trasfondos_base      = copy.deepcopy(trasfondos)
    
    distribucion_datos(datos,datos_base,frame_datos,2)
    distribucion_atributo(caracteristicas,caracteristicas,frame_caracteristicas,0)
    distribucion_habilidades(habilidades,habilidades,frame_habilidades,0)
    distribucion_tiradas(frame_tiradas)
    distribucion_disciplinas(disciplinas,disciplinas_base,frame_ventajas,1,nombres_disciplinas)
    otras_tiradas(frame_otras_tiradas)
    distribucion_trasfondos(trasfondos,trasfondos_base,frame_ventajas,1,nombres_trasfondos)
    
    # EJECUTO EL LOOP PARA VER LA PANTALLA
    root.mainloop()

def guardar():
    global ruta, datos, caracteristicas, habilidades,ruta,lista_madre,disciplinas,trasfondos
    #SI LA RUTA ESTA VACIA, LE PIDE QUE ELIJA UNA PARA GUARDAR EL ARCHIVO
    
    #ACA ME ASEGURO QUE TODOS LOS DICTS GUARDEN ACTUALIZADOS
    for clave, objeto in obj_datos.items():
        datos[clave][0]= objeto.text.get()
        
    for clave, objeto in obj_caracteristicas.items():
        caracteristicas[clave][0]= objeto.valor.get()
        
    for clave, objeto in obj_habilidades.items():
        habilidades[clave][0]= objeto.valor.get()
    
    for clave, objeto in obj_disciplinas.items():
        disciplinas[clave][0]= objeto.valor.get()
        disciplinas[clave][3]= objeto.disci.get()
    print(disciplinas)
    
    for clave, objeto in obj_trasfondos.items():
        trasfondos[clave][0]= objeto.valor.get()
        trasfondos[clave][3]= objeto.disci.get()
    print(trasfondos)

    archivo = FileDialog.asksaveasfile(initialdir=".", 
                                      filetypes=(("Fichas de V20 ", "*.pckl"),), 
                                      title = "Guardar ficha de V20.")
    
    ruta,ext = os.path.splitext(archivo.name)  #NAME.ME --> LA RUTA REAL - Ruta --> Nombre Archivo Ext--> La extensión
    
    # Añade la extensión .txt al nombre del archivo si no tiene ya la extensión y me aseguro que solo funcione si selecciona algo
    if archivo is not None:
        ruta,ext = os.path.splitext(archivo.name)  #NAME.ME --> LA RUTA REAL - Ruta --> Nombre Archivo Ext--> La extensión
        if ext != ".pckl":
            ruta = ruta + ".pckl"
        else:
            ruta = archivo.name
    
        with open (ruta, "wb") as picklefile:
            pickle.dump(lista_madre,picklefile)
    else:
        # El usuario canceló la selección de archivo
        print("No se ha seleccionado un archivo para guardar.")


#CONFIGULO EL MENU
menubar = Menu(root)
root.config(menu=menubar)

filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label ="Nueva ficha",command=nuevo)
filemenu.add_command(label ="Abrir ficha",command=abrir)
filemenu.add_command(label ="Guardar ficha",command=guardar)

helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label ="Acerca del Nosferatu")

menubar.add_cascade(label="Archivo",menu=filemenu)
menubar.add_cascade(label="Ayuda",menu=helpmenu)

filemenu.add_separator()
filemenu.add_command(label="Salir",command=root.quit)


# EJECUTO EL LOOP PARA VER LA PANTALLA
root.mainloop()
