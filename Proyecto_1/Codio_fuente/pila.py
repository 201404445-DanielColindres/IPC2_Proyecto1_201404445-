from graphviz.backend import view
from graphviz import Digraph
from nodo import nodo

class pila:
    def __init__(self):
        self.ultimo = None
        self.size = 0

    def apilar(self, valor):
        nuevo = nodo(valor)
        if(self.size == 0):
            self.ultimo = nuevo
            nuevo.siguiente = None
            self.size = 1
        else:
            nuevo.siguiente = self.ultimo
            self.ultimo = nuevo
            self.size +=1

   
