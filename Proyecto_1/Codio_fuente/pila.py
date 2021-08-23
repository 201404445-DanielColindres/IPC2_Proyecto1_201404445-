from graphviz.backend import view
from graphviz import Digraph
from nodo import nodo

class pila:
    def __init__(self):
        self.ultimo = None
        self.size = 0

        