from pila import pila
import easygui
import codecs
import re

class archivo:

    def __init__(self):
        self.baseDatos = {}
    
    def carga(self):        
        cargarArchivo = easygui.fileopenbox(default=('*.xml'))
        try:
            entrada_doc= codecs.open(cargarArchivo,'r',encoding='utf-8')
           
            control=0
            control_ingreso=0
            diccionario={}

            for linea in entrada_doc:    
                linea = linea.rstrip().lstrip()
                if linea.startswith('<terreno>'):
                    #agregar los datos obtenidos a la pila
                    control_ingreso += 1
                    pass
                else:
                    #-------------------Nombre del terreno-----------------
                    nombreT = re.search('<terreno nombre="(.+?)">', linea)
                    if nombreT:
                        #print(nombreT.group(1))
                        diccionario["nombre_terreno:"+str(control_ingreso)]=nombreT.group(1)
                    #-------------------organizacion de dimenciones y posiciones-----------------
                    dimension = re.search('<dimension>', linea)
                    if dimension:
                        control = 1
                    posI = re.search('<posicioninicio>', linea)
                    if posI:
                        control = 2
                    posF = re.search('<posicionfin>', linea)
                    if posF:
                        control = 3
                    #-------------------Posiciones del terreno-----------------
                    posInfo = re.search('<posicion (.+?)</posicion>', linea)
                    if posInfo:
                        #print(posInfo.group(1))
                        px = re.search("x=\"(.+?)\"", linea)
                        px= str((px.group(1)))
                        py = re.search("y=\"(.+?)\"", linea)
                        py= str((py.group(1)))
                        val= re.search(">(.+?)<", linea)
                        val= (val.group(1))
                        #print(px + " " + py + " " + val)
                        diccionario["["+px+","+py+"]:"+str(control_ingreso)]=val
                    #-------------------extraccion de dimenciones y posiciones-----------------
                    if control == 1:
                        dimension_m = re.search('<m>(.+?)</m>', linea)
                        if dimension_m:
                            #print(dimension_m.group(1))
                            diccionario["dim_m:"+str(control_ingreso)]=dimension_m.group(1)   

                        dimension_n = re.search('<n>(.+?)</n>', linea)            
                        if dimension_n:
                            #print(dimension_n.group(1))
                            diccionario["dim_n:"+str(control_ingreso)]=dimension_n.group(1)

                    if control ==2:
                        dimension_Ix = re.search('<x>(.+?)</x>', linea)
                        if dimension_Ix:
                            # print(dimension_Ix.group(1)) 
                            diccionario["inicio_x:"+str(control_ingreso)]= dimension_Ix.group(1)

                        dimension_Iy = re.search('<y>(.+?)</y>', linea)
                        if dimension_Iy:
                            #print(dimension_Iy.group(1))
                            diccionario["inicio_y:"+str(control_ingreso)]=dimension_Iy.group(1)

                    if control ==3:
                        dimension_Fx = re.search('<x>(.+?)</x>', linea)
                        if dimension_Fx:
                            #print(dimension_Fx.group(1))
                            diccionario["final_x:"+str(control_ingreso)]=dimension_Fx.group(1)
                            
                        dimension_Fy = re.search('<y>(.+?)</y>', linea)
                        if dimension_Fy:
                            #print(dimension_Fy.group(1))
                            diccionario["final_y:"+str(control_ingreso)]=dimension_Fy.group(1)
            self.baseDatos = diccionario
            return diccionario
        except:
        #       print(Exception())
            return False

    def procesar(self,terreno):
        kbase = self.baseDatos
        for k in kbase:  
            if kbase["ombre_terreno"] == terreno:
                break

        '''
        kbase = self.baseDatos
        for k in kbase:
              print(str(k)+" "+kbase[str(k)])
        '''