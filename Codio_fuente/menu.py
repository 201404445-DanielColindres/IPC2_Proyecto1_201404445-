from archivo import archivo

opcion =0
confirmarArchivo = False
archivo = archivo()

def continuar(a): 
    qwe = input(a)

def cargarArchivo():
    nuevoValor = archivo.carga()
    if  nuevoValor != False:
        continuar('Archivo Cargado con exito! ')
        print(nuevoValor)
        confirmarArchivo = True
    else:
        print('Paso algo inesperado')
    
def procesarArchivo():
    print(archivo.procesar())

def escribirArchivo():
    pass

def mostrarDatos():
    print('''

-----------------------------------------------------------------
Datos del estudiante:
    > Daniel José Colindres Fuentes
    > 201404445
    > Introducción a la Programacion y Computación 2 sección "A"
    > Ingenieria en Ciencias y Sistemas
    > 4to Semestre
-----------------------------------------------------------------
    
    ''')
    continuar('Presione enter para continuar')

def generarGrafica():
    pass

def menuPrincipal ():
    global opcion
    while True:
        
        print('''
-------------------------------------
Menú Principal:
    1. Cargar Archivo
    2. Procesar Archivo
    3. Escribir Achivo Salida
    4. Mostrar datos del estudiante
    5. Generar Gráfica
    6. Salir
-------------------------------------

        ''')

        opcion = int(input("Ingrese una opcion:\n"))
        
        if opcion == 1:
            cargarArchivo()
        elif opcion == 2:
            terreno = input('Ingrese el terreno que desea calcular:\n')
            procesarArchivo(terreno)
        elif opcion == 3:
            print("3")
        elif opcion == 4:
            mostrarDatos()
        elif opcion == 5:
            print("5")
        elif opcion == 6:
            break
        
