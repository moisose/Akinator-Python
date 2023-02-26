# Librerias
import tkinter as tk
from tkinter import messagebox 

# Variables globales
juegos = []
objeto_1 =''
objeto_2 = ''
pregunta = ''
data = ''
arbol = ''
nuevo_objeto = ''
posicion = ''

app = ''
ventana_abrir = ''

# -------------------------------------------------------------------------------------------------
# Archivos
# -------------------------------------------------------------------------------------------------

# CHECK FILE EXISTANCE
# E: el filepath, nombre del archivo
# S: bool
# determina si el archivo existe en la ruta donde se ejecuta el programa
def checkFileExistance(filePath):
    try:
        with open(filePath, 'r') as f:
            return True
    except FileNotFoundError as e:
        return False
    except IOError as e:
        return False


# CREAR ARCHIVO
# E: filepath, lista
# crea el archivo si no existe en la ruta del .py
def crearArchivo(filePath, stringToWrite):
    fo = open(filePath, 'w')
    fo.write(str(stringToWrite))
    fo.close()

# GUARDAR INFORMACION EN ARCHIVO
# E: el path, string a guardar
# S: la cantidad de caracteres escritos
# guardar el string deseado en el archivo seleccionado
def guardar(filePath, stringToWrite):
    fo = open(filePath, "w")  # crea el file si no existe
    fo.write(str(stringToWrite))
    fo.close()

# LEER ARCHIVO
# E: file path
# S: string con contenido
# retorna el contenido del archivo
def leer(filePath):
    try:
        fo = open(filePath, 'r')
        resultado = fo.read()
        fo.close()
        return resultado
    except:
        return []

# CARGAR ARCHIVOS
# Carga en las variables globales la información de los archivos
# Si los archivo no existen los crea
def cargarArchivos():
    global juegos

    if (
        checkFileExistance("files/juegos.txt") == False
    ):  # verifica que todos los archivos existan, y si no lo crea
        crearArchivo("files/juegos.txt", juegos)

    juegos = eval(leer("files/juegos.txt"))

# -------------------------------------------------------------------------------------------------
# Commons
# -------------------------------------------------------------------------------------------------
# Funciones

# GET NEXT ID
# Obtiene el consecutivo siguiente de la lista de detectives
# E: una lista de listas, donde el primer campo es id
# S: numero
def getNextId(lista):
    actual = 0

    for elemento in lista:
        if elemento[0] > actual:
            actual = elemento[0]
    return actual + 1

# IS INTEGER
# E: string
# S: bool
# Determina si el valor es un numero entero
def isInteger(strValue):
    try:  # intentar hacer estas lineas

        intValue = eval(strValue)

        if type(intValue) == int:
            return True
        else:
            return False
    except:
        # si hay exception o error en ejecucion, pasa al except y ejecuta las intrucciones de alli

        return False
# -------------------------------------------------------------------------------------------------
# Árboles
# -------------------------------------------------------------------------------------------------

# Es atomo
# E: arbol
# S: bool
# Retorna True si es un átomo, es decir una raiz ni una hoja
def atomo(arb):
	return not isinstance(arb, list)
# print(atomo(5))


# Es raiz
# E: arbol
# S: numero
# Retorna la raiz del árbol como numero
def raiz(arb):
	if atomo(arb):
		return arb
	else:
		return arb[0]

# Hijo izquierdo
# E: arbol
# S: arbol
# Retorna el hijo izquierdo del árbol
def hijo_izquierdo (arb):
	if atomo(arb):
		return []
	else:
		return arb[1]

# Hijo derecho
# E: arbol
# S: arbol
# Retorna el hijo derecho del arbol
def hijo_derecho(arb):
	if atomo(arb):
		return []
	else:
		return arb[2]

# Es hoja
# E: arbol
# S: bool
# Retorna True si es una hoja, no tiene hijos
def hoja(arb):
	if arb == []:
		return False
	elif atomo(arb) or (hijo_izquierdo(arb) == [] and hijo_derecho(arb) == []):
		return True
	return False

# Crear arbol
# Retorna un arbol creado con los elementos dados
def build_tree(raiz, hijoIzq, hijoDer):
	if hijo_derecho == [] and hijo_derecho == []:
		return raiz
	else:
		return [raiz, hijoIzq, hijoDer]


def agregar_elemento(elemento, arb):
	if arb == []:
		return elemento
	elif elemento < raiz(arb):
		return build_tree(raiz(arb), agregar_elemento(elemento, hijo_izquierdo(arb)), hijo_derecho(arb))
	else:
		return build_tree(raiz(arb), hijo_izquierdo(arb), agregar_elemento(elemento, hijo_derecho(arb)))

# print (agregar_elemento(5,a5))

# ---------------------------------------------------------------------------------------------------
# Recorrido de arboles binarios

# Obtener posición
# E: lista y arbol
# S: numero
# Retorna la posicion del arbol en la lista de juegos
def obtener_posicion(lista, arb):
	res = 0 

	for i in lista:
		if i [2] == arb:
			return i[0]-1

# -------------------------------------------------------------------------------------------------

# Esta 1
# E: arbol y elemento
# S: Bool
# Retorna True si el elemento está en el arbol binario 
def esta_1(arb, elemento):
	global juego1
	if arb == []:
		return False
	elif elemento == raiz(arb):
		return True
	else:
		return esta_1(hijo_izquierdo(arb), elemento) + esta_1(hijo_derecho(arb), elemento)
#print(esta_izq(juego1, 'dasdasd'))


# Agragar elemento Akinator
# E: arbol, elemento, pregunta, elemento, elemento actual
# S: arbol binario
# Retorna un árbol bonario con los nuevos elementos agregados
def agregar_elemento_akinator(arb, new, dif, old,  ele_actual):
	global juegos
	# print(arb)
	if arb == []:
		return []

	elif esta_1(hijo_izquierdo(arb), ele_actual) :
		return build_tree(raiz(arb), agregar_elemento_akinator(hijo_izquierdo(arb), new, dif, old, ele_actual), hijo_derecho(arb))
	elif esta_1(hijo_derecho(arb), ele_actual):
		return build_tree(raiz(arb), hijo_izquierdo(arb), agregar_elemento_akinator(hijo_derecho(arb), new, dif, old, ele_actual))
	elif ele_actual == raiz(arb):
		return build_tree(dif, new, old)
#print(agregar_elemento_akinator(juego1, 'Zorra', '¿Come pasto?', 'León', 'León'))

# Agregar elemento nuevo
# E: arbol, elemento, pregunta, elemento
# S: arbol binario
# Retorna un arbol binario nuevo con los primeros elementos agregados 
def agregar_elemento_nuevo(arb, new, dif, old):
	global juego1
	# print(arb)
	if arb == []:
		return build_tree(dif, new, old)
#print(agregar_elemento_akinator(juego1, 'Zorra', '¿Come pasto?', 'León', 'León'))

# Juego datos
# E: arbol
# Recorre el arbol binario y va haciendo preguntas, dependiendo si la respuesta es si o no
# se va recorriendo a la izquierda o a la derecha
# Puede agregar elementos al arbol
def juego_datos(arb):
	global juego1
	print(raiz(arb))
	if arb == []:
		return ''
	elif hoja(arb):
		# print(arb)
		respuesta = input('Era lo que estabas buscando? Y / N: ').title()
		if respuesta == 'Y':
			return 'Gracias por jugar'
		else:
			print('Si no es lo que buscabas, ¿Qué era?')
			new = input('Ingrese la nueva cosa: ')
			dif = input('¿Cuál es la pregunta que diferencia entre ' + str(arb) + ' y ' + str(new) + ' : ')

			opcion = input('Si la cosa fuera ' + str(new) + ' ¿Cuál sería la respuesta? (Si/No)').title()

			if opcion == 'Si':
				opcion1 = new
				opcion2 = arb
			else:
				opcion1 = arb
				opcion2 = new

			juego1 = agregar_elemento_akinator(juego1, opcion2, dif, opcion1, arb)
			print(juego1)
			return

	# print(raiz(arb))
	decision = input('Y / N: ').title()
	if decision == 'N':
		return juego_datos(hijo_izquierdo(arb))
	else:
		return juego_datos(hijo_derecho(arb))

# juego_datos(juego1)

# Juego vacio
# Crea un nuevo arbol
def juego_vacio():
	new_tree = []
	return juego_vacio_aux(new_tree)

# Juego vacio aux
# E: arbol
# S: arbol
# Solicita unos datos y con ellos crea un nuevo arbol binario
def juego_vacio_aux(arb):
	value1 = input('Pon el nombre de un objeto (1°):').title()
	value2 = input('Pon el nombre de un objeto (2°):').title()
	dif = input('¿Cuál es la pregunta que diferencia entre ' + value1 + ' y ' + value2 + ' ?')

	opcion = input('Si la cosa fuera ' + str(value1) + ' ¿Cuál sería la respuesta? (Si/No)').title()

	if opcion == 'Si':
		opcion1 = value2
		opcion2 = value1
	else:
		opcion1 = value1
		opcion2 = value2

	x = agregar_elemento_nuevo(arb, opcion1, dif, opcion2)
	print(x)

	

# print(juego_vacio())

#print(agregar_elemento_nuevo([], 'Hola', '¿Sirve para saludar?', 'Adios'))

#------------------------------------------------------------------------------------------------------

# Orden objetos nuevos
# E: none
# S: Arbol
# Retorna un arbol binario con los nuevos elementos agregados
def orden_objetos_nuevos():
	global juegos
	global arbol
	global nuevo_objeto
	global posicion
	global pregunta

	opcion = messagebox.askyesno("Ubicación","Si la cosa fuera " + arbol + ' ¿cuál sería la respuesta? (Si/No)')
	if opcion == True:
		opcion1 = nuevo_objeto
		opcion2 = arbol
	else:
		
		opcion1 = arbol
		opcion2 = nuevo_objeto
	# print('La posicion es: ', posicion)
	# print('La opcion 2 es: ', opcion2)
	# print('La opcion 1 es: ', opcion1)
	# print('La diferencia es: ', pregunta)
	# print('El ele acctual es: ', arbol)
	juegos[posicion][2] = agregar_elemento_akinator(juegos[posicion][2], opcion2, pregunta, opcion1,  arbol)

	messagebox.showinfo("Información","Los datos fueron agregados.")

	#guardar('juegos.txt', juegos) 
	app.state(newstate="normal")

# Pregunta union
# E: none
# S: string
# Solicita la oregunta que va a unir los 2 elementos del arbol binario
def pregunta_union_nuevo():

	def obtener_pregunta_union_nuevo():
		global juegos
		global arbol
		global nuevo_objeto
		global pregunta
		question = value5.get()
		if question.strip() == '':
			error('Error', 'Debe escribir una pregunta.')
		else:
			pregunta = question

			ventana5.destroy()
			orden_objetos_nuevos()

	ventana5 = tk.Toplevel()
	ventana5.geometry('550x125+700+300')
	ventana5.title('ArbolDePreguntasYRespuestas')
	ventana5.resizable(0,0)
	ventana5.iconbitmap('img/hoja.ico')

	tk.Label(ventana5, text='¿Cuál es la pregunta que diferencia entre ' + arbol + ' y ' + nuevo_objeto + '?', font = ('Verdana',8), justify=tk.CENTER, height=2, width=70).place(x=30,y=15)
	value5 = tk.Entry(ventana5, bd=2, width=48)
	value5.place(x=135, y=50, height = 25)
	tk.Button(ventana5, text= 'Aceptar', command = obtener_pregunta_union_nuevo).place(x=250,y=80)

	ventana5.mainloop()

# Abrir juego
# E: arbol binario
# S: messagebox o string
# Recorre el arbol binario de busqueda haciendo preguntas
# Si la respuesta e lo que buscaba termina el programa
# Si la respuesta es diferente, pregunta el nuevo elemento y llama a la funcion pregunta_union_nuevo()
def abrir_juego(arb, iteracion = 0):
	global juegos
	global posicion
	global nuevo_objeto
	global arbol
	# print('la iteracion es: ', iteracion)
	if iteracion == 0:
		ventana_abrir.destroy()
		posicion = obtener_posicion(juegos, arb)
		# print(posicion)
	def obtener_nuevo_dato():
		global juegos
		global nuevo_objeto

		dato = value4.get()
		if dato.strip() == '':
			error('Error', 'Debe escribir un objeto.')
		else:
			nuevo_objeto = dato.title()

			ventana4.destroy()
			pregunta_union_nuevo()

	#arb = juegos[numero][2]

	if arb == []:
		return ''
	elif hoja(arb):
		# print(arb)
		arbol = arb
		respuesta = messagebox.askyesno("Ubicación",arbol + ' \n¿Era lo que estabas buscando?')
		if respuesta :
			messagebox.showinfo("Información","Gracias por jugar!!")
			app.state(newstate="normal")
			return
		else:

			ventana4 = tk.Toplevel()
			ventana4.geometry('400x125+700+300')
			ventana4.title('ArbolDePreguntasYRespuestas')
			ventana4.resizable(0,0)
			ventana4.iconbitmap('img/hoja.ico')

			tk.Label(ventana4, text='Si no es lo que buscabas, ¿Qué era?: ', font = ('Verdana',8)).place(x=95,y=15)
			value4 = tk.Entry(ventana4, bd=2, width=48)
			value4.place(x=60, y=50, height = 25)
			tk.Button(ventana4, text= 'Aceptar', command = obtener_nuevo_dato).place(x=175,y=80)
			return

			ventana4.mainloop()

	# print(raiz(arb))
	#decision = input('Y / N: ').title()
	decision = messagebox.askyesno("Application",raiz(arb))
	if decision :
		return abrir_juego(hijo_izquierdo(arb), iteracion+1)
		
	else:
		return abrir_juego(hijo_derecho(arb), iteracion+1)

# Abrir datos
# Crea una pantalla con las opciones de los juegos existentes para abrir
def abrir_datos():
	global juegos
	global ventana_abrir

	def validar_numero():
		global juegos
		n1 = eleccion.get()
		# print(n1)
		if isInteger(n1):
			n1 = int(n1)
			for i in juegos:
				if i[0] == n1:
					num = i[0] -1
					# print(num)
					abrir_juego(juegos[num][2])
		else:
			error('Formato', 'Debe ser un número de las opciones.')

	app.withdraw()
	ventana_abrir = tk.Toplevel()
	ventana_abrir.geometry('615x700+700+200')
	ventana_abrir.title('ArbolDePreguntasYRespuestas')
	# ventana_abrir.resizable(0,0)
	ventana_abrir.iconbitmap('img/hoja.ico')
	# ventana_abrir.config(bg='white')

	tk.Label(ventana_abrir, text = 'ÁRBOLES DISPONIBLES:', font = ('Verdana',11), width=45, height = 2, borderwidth=2, relief="ridge", bg='#00466b', fg='white').place(x=112,y=25)
	tk.Button(ventana_abrir, text='Regresar', font = ('Verdana',10), command=lambda:regresar(ventana_abrir)).place(x=15,y=15)

	y = 75
	for i in juegos:
		# print(i)
		bot = tk.Label(ventana_abrir, text = str(i[0]) + '. ' + str(i[1]), font = ('Verdana',10), width=50, height = 2, borderwidth=2, relief="groove")
		bot.place(x=115,y=y)
		# bot.config(command = lambda:abrir_juego(juegos[i[0]-1][2]))
		y += 35

	y += 50
	tk.Label(ventana_abrir, text='Digite el número del árbol: ', font = ('Verdana',11), relief="solid", width=30, height=1).place(x=185,y=y-30)
	eleccion = tk.Entry(ventana_abrir, bd=2, width=5)
	eleccion.place(x=295,y=y)
	tk.Button(ventana_abrir, text='Cargar', command = validar_numero, font = ('Verdana',10), width=7).place(x=279, y=y+25)

	ventana_abrir.mainloop()
#---------------------------------------------------------------------------------

# Orden objetos
# Dependiendo de la respuesta, forma un nuevo arbol binario con los datos guardados en las globals
def orden_objetos():
	global objeto_1
	global objeto_2
	global pregunta
	global juegos

	opcion = messagebox.askyesno("Ubicación","Si la cosa fuera " + objeto_1 + ' ¿cuál sería la respuesta? (Si/No)')
	if opcion == True:
		opcion1 = objeto_1
		opcion2 = objeto_2
	else:
		opcion1 = objeto_2
		opcion2 = objeto_1

	x = agregar_elemento_nuevo([], opcion1, pregunta, opcion2)
	print(x)

	messagebox.showinfo("Información","Los datos fueron agregados.")

	id = getNextId(juegos)
	juegos.append([id, data, x])
	#guardar('juegos.txt', juegos) 
	app.state(newstate="normal")

# Pregunta union
# Crea una pantalla y hace una pregunta que será utilizada como la pregunta union
# de los dos elementos del arbol binario
def pregunta_union():
	global objeto_1
	global objeto_2
	global pregunta
	def obtener_pregunta_union():
		global pregunta
		question = value3.get()
		if question.strip() == '':
			error('Error', 'Debe escribir una pregunta.')
		else:
			pregunta = question

			ventana3.destroy()
			orden_objetos()

	ventana3 = tk.Toplevel()
	ventana3.geometry('550x125+700+300')
	ventana3.title('ArbolDePreguntasYRespuestas')
	ventana3.resizable(0,0)
	ventana3.iconbitmap('img/hoja.ico')

	tk.Label(ventana3, text='¿Cuál es la pregunta que diferencia entre ' + objeto_1 + ' y ' + objeto_2 + '?', font = ('Verdana',8), justify=tk.CENTER, height=2, width=70).place(x=30,y=15)
	value3 = tk.Entry(ventana3, bd=2, width=48)
	value3.place(x=135, y=50, height = 25)
	tk.Button(ventana3, text= 'Aceptar', command = obtener_pregunta_union).place(x=250,y=80)

	ventana3.mainloop()

# Objeto 2
# Pregunta cual es el objeto numero 2 que se agregará al arbol binario
def objeto2():
	def obtener_objeto_2():
		global objeto_2

		objeto = value2.get()
		if objeto.strip() == '':
			error('Error', 'Debe escribir un objeto.')
		else:
			objeto_2 = objeto.title()

			ventana2.destroy()
			pregunta_union()

	ventana2 = tk.Toplevel()
	ventana2.geometry('400x125+700+300')
	ventana2.title('ArbolDePreguntasYRespuestas')
	ventana2.resizable(0,0)
	ventana2.iconbitmap('img/hoja.ico')

	tk.Label(ventana2, text='Pon el nombre de un objeto (2°):', font = ('Verdana',10)).place(x=90,y=15)
	value2 = tk.Entry(ventana2, bd=2, width=48)
	value2.place(x=60, y=50, height = 25)
	tk.Button(ventana2, text= 'Aceptar', command = obtener_objeto_2).place(x=175,y=80)

	ventana2.mainloop()

# Objeto 1
# Pregunta cual es el objeto numero 1 que se agregará al arbol binario
def objeto1():

	def obtener_objeto_1():
		global objeto_1
		objeto = value1.get()
		if objeto.strip() == '':
			error('Error', 'Debe escribir un objeto.')
		else:
			objeto_1 = objeto.title()

			ventana.destroy()
			objeto2()

	ventana = tk.Toplevel()
	ventana.geometry('400x125+700+300')
	ventana.title('ArbolDePreguntasYRespuestas')
	ventana.resizable(0,0)
	ventana.iconbitmap('img/hoja.ico')

	tk.Label(ventana, text='Pon el nombre de un objeto (1°):', font = ('Verdana',10)).place(x=90,y=15)
	value1 = tk.Entry(ventana, bd=2, width=48)
	value1.place(x=60, y=50, height = 25)
	tk.Button(ventana, text= 'Aceptar', command = obtener_objeto_1).place(x=175,y=80)

	ventana.mainloop()


# Cerrar programa
# E: nombre de la ventana
# S: none
def close_window (ventana):
	ventana.destroy()

# ----------------------
# Regresar
# E: string
# Elimina la ventana ectual y abre el menu principal
def regresar(x_ventana):
    app.state(newstate="normal")
    x_ventana.destroy()

# Fucion para showmessage
# --------------------------------------

# Mensaje emergente
# E: 2 strings
# Crea un messagebox con los datos ingresados
def mensaje_emergente(texto1, texto2):
    messagebox.showinfo(texto1, texto2)

# Error
# E: 2 strings
# Crea un messagebox de error con los datos ingresados
def error(texto1, texto2):
    messagebox.showerror(texto1, texto2)

# Ventana nuevo
# Crea una ventana para empezar a crear nuevos arboles
def ventana_nuevo():
	def obtener_tematica():
		global data
		dato = tema.get()
		if dato.strip() == '':
			error('Error', 'Debe escribir una temática.')
		else:
			data = dato.title()
			vent_new.destroy()
			objeto1()

	app.withdraw()

	vent_new = tk.Toplevel()
	vent_new.title('Nuevo Juego')
	vent_new.geometry('600x200+700+300')
	vent_new.resizable(0,0)
	vent_new.iconbitmap('img/hoja.ico')

	tk.Button(vent_new, text = 'Regresar', font = ('Verdana',10), command = lambda:regresar(vent_new)).place(x=15,y=15)
	tk.Label(vent_new, text = 'Escriba la temática del nuevo juego', font = ('Verdana',12)).place(x=150,y=50)
	tema = tk.Entry(vent_new, bd=2, width=48)
	tema.place(x=150, y=85, height = 25)

	tk.Button(vent_new, text='Siguiente', font = ('Verdana',10), command = obtener_tematica).place(x=260,y=120)

	vent_new.mainloop()

# Cantidad tabs
# E: numero
# S: string
# Retorna un string de tabs
def cantidad_tabs(num):
	return '\t' * num

# Imprimir arboles
# E: arbol binario
# S: string
# Retorna un string del arbol binario ordenado por raiz, hijos izquierdo e hijo derecho
def imprimir_arboles(arb, ite = 0):
	if arb == []:
		return []
	elif ite == 0:
		return ['Raiz: > ' + str(raiz(arb)) + '\n\n'] + imprimir_arboles(hijo_izquierdo(arb), ite+1) + imprimir_arboles(hijo_derecho(arb), ite+1)
	elif ite > 0:
		return [cantidad_tabs(ite) + '- ' + str(raiz(arb)) + '\n\n'] + imprimir_arboles(hijo_izquierdo(arb), ite+1) + imprimir_arboles(hijo_derecho(arb), ite+1)

# Abrir ventana datos
# E: numero
# S: string
# Crea una ventana y muestra el arbol binario ordenado seleccionado
def abrir_ventana_datos(num):
	global juegos

	ventana_datos_2 = tk.Toplevel()
	ventana_datos_2.title('Ver datos')
	ventana_datos_2.geometry('1200x600+300+200')
	ventana_datos_2.resizable()
	ventana_datos_2.iconbitmap('img/hoja.ico')

	x = imprimir_arboles(juegos[num][2])
	#print(x)

	scroll_bar = tk.Scrollbar(ventana_datos_2)
	scroll_bar.pack(side=tk.RIGHT, fill=tk.Y)

	mylist = tk.Text(ventana_datos_2, yscrollcommand = scroll_bar.set, width = 132, height=37, font = ('Verdana',10))
	for i in x:
		mylist.insert(tk.END, i)
	#mylist.insert(tk.END, x)

	# mylist.pack(side = tk.LEFT, fill=tk.BOTH)
	mylist.place(x=120,y=0)
	scroll_bar.config(command = mylist.yview)

	tk.Button(ventana_datos_2, text = 'Regresar', font = ('Verdana',10), command = lambda:regresar(ventana_datos_2)).place(x=15,y=15)

	# print(x)
	# tk.Label(ventana_datos_2, text = x, justify=tk.LEFT).place(x=15,y=15)

	ventana_datos_2.mainloop()

# Ventana datos
# Crea una ventana con los arboles disponibles para ver sus datos
def ventana_datos():
	global juegos

	def validar_numero():
		global juegos
		n1 = eleccion.get()
		# print(n1)
		if isInteger(n1):
			n1 = int(n1)
			for i in juegos:
				if i[0] == n1:
					num = i[0] -1
					print(num)
					ventana_datos.destroy()
					abrir_ventana_datos(num)
		else:
			error('Formato', 'Debe ser un número de las opciones.')

	app.withdraw()

	ventana_datos = tk.Toplevel()
	ventana_datos.title('Ver datos')
	ventana_datos.geometry('615x700+700+200')
	# ventana_datos.resizable(0,0)
	ventana_datos.iconbitmap('img/hoja.ico')

	tk.Button(ventana_datos, text = 'Regresar', font = ('Verdana',10), command = lambda:regresar(ventana_datos)).place(x=15,y=15)
	tk.Label(ventana_datos, text = 'ÁRBOLES DISPONIBLES:', font = ('Verdana',11), width=45, height = 2, borderwidth=2, relief="ridge", bg='#00466b', fg='white').place(x=112,y=25)

	y = 75
	for i in juegos:
		# print(i)
		bot = tk.Label(ventana_datos, text = str(i[0]) + '.     ' + str(i[1]), font = ('Verdana',10), width=20, height = 2, borderwidth=2, relief="groove")
		bot.place(x=230,y=y)
		# bot.config(command = lambda:abrir_juego(juegos[i[0]-1][2]))
		y += 35

	y += 50
	tk.Label(ventana_datos, text='Digite el número del árbol: ', font = ('Verdana',11), relief='solid', width=30, height=1).place(x=185,y=y-30)
	eleccion = tk.Entry(ventana_datos, bd=2, width=5)
	eleccion.place(x=295,y=y)
	tk.Button(ventana_datos, text='Cargar', command = validar_numero, font = ('Verdana',10), width=7).place(x=279, y=y+25)

	ventana_datos.mainloop()

# Guardar datos
# Guarda los datos del programa
def guardar_datos():
	global juegos
	guardar('files/juegos.txt', juegos) 
	messagebox.showinfo("Informacion","Se han guardado los datos del árbol exitosamente.")

# Menu pricipal
# Crea la interfaz del menu principal
def menu_principal():
	global app
	app = tk.Tk()
	app.title('Ejemplo de Arbol Binario')
	app.geometry('600x400+700+200')
	app.resizable(0,0)
	app.iconbitmap('img/hoja.ico')

	# If you want a border, the option is borderwidth. You can also choose the relief of the border: "flat", "raised", "sunken", "ridge", "solid", and "groove".

	# For example:
	# l1 = Label(root, text="This", borderwidth=2, relief="groove")

	tk.Label(app, text = 'Ejemplo de uso de árboles binarios:\nJuego de Preguntas y Respuestas', width=40, height = 3, borderwidth=2, relief="ridge", font = ('Verdana',12)).place(x=100,y=15)
	new = tk.PhotoImage(file='img/new2.png')
	b1 = tk.Button(app, text = 'Nuevo', image = new, width = 150, height=75, command = ventana_nuevo)
	b1.place(x=40, y=180)

	# play = tk.PhotoImage(file='play_1.png')
	# tk.Button(app, text = 'Nuevo', image = play, width = 150, height=75).place(x=40, y=270)

	abrir = tk.PhotoImage(file='img/abrir.png')
	tk.Button(app, text = 'Nuevo', image = abrir, width = 150, height=75, command = abrir_datos).place(x=220, y=180)

	datos = tk.PhotoImage(file='img/datos.png')
	tk.Button(app, text = 'Nuevo', image = datos, width = 150, height=75, command = ventana_datos).place(x=125, y=270)

	guardar = tk.PhotoImage(file='img/guardar.png')
	tk.Button(app, text = 'Nuevo', image = guardar, width = 150, height=75, command = guardar_datos).place(x=400, y=180)

	salir = tk.PhotoImage(file='img/salir.png')
	tk.Button(app, text = 'Nuevo', image = salir, width = 150, height=75, command = lambda:close_window(app)).place(x=300, y=270)

	tk.Label(app, text='Autor: Moisés Solano Espinoza\nTaller de Programación\n2021', height=4, width=57, justify=tk.CENTER, font = ('Verdana',8)).place(x=125,y=100)
	img_arbol = tk.PhotoImage(file='img/arbol2.png')
	# img_arbol = img_arbol.subsample(5,5)
	tk.Label(app, image=img_arbol).place(x=150,y=90)

	cargarArchivos()
	app.mainloop()

menu_principal()

juego1 = ['¿Maulla?',
					['¿Vuela?', ['¿Vuela de noche?', 'Murciélago', 'Pájaro'], 'Perro'],
					['¿Vive en la Sabana Africana?', 'León', 'Gato']
					]