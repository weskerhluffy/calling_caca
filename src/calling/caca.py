'''
Created on 23/02/2018

@author: 

XXX: https://uva.onlinejudge.org/index.php?option=onlinejudge&page=show_problem&problem=183
'''

import logging
import sys
from sys import stdin
from collections import defaultdict

nivel_log = logging.ERROR
#nivel_log = logging.DEBUG
logger_cagada = None

class nodo_caca():
    def __init__(self):
        self.nombre = ""
        self.visitado = False
        self.visitado_transputa = False
        self.vecinos = []
        self.vecinos_transputa = []
    def __repr__(self):
#        return "{}:{}:{}".format(self.nombre, list(map(lambda x:x.nombre, self.vecinos)), list(map(lambda x:x.nombre, self.vecinos_transputa)))
        return "{}".format(self.nombre)
        
def calling_caca_kosacarajo_ordena(nodo, pila_nodos):
    pila_rec = []
    pila_rec.append((nodo, None))
    nodo.visitado = True
    while(pila_rec):
        nodo_act, itera = pila_rec.pop()
        if itera is None:
            itera = iter(nodo_act.vecinos)
        vecino = next(itera, None)
        if vecino:
            pila_rec.append((nodo_act, itera))
            if not vecino.visitado:
                vecino.visitado = True
                pila_rec.append((vecino, None))
        else:
            pila_nodos.append(nodo_act)

def calling_caca_kosacarajo_junta_componentes(nodo, miembros):
    pila_rec = []
    pila_rec.append((nodo, None))
    nodo.visitado_transputa = True
    while(pila_rec):
        nodo_act, itera = pila_rec.pop()
        if itera is None:
            itera = iter(nodo_act.vecinos_transputa)
        vecino = next(itera, None)
        if vecino:
            pila_rec.append((nodo_act, itera))
            if not vecino.visitado_transputa:
                vecino.visitado_transputa = True
                pila_rec.append((vecino, None))
        else:
            miembros.append(nodo_act)
    

def calling_caca_kosacarajo(nodos):
    pila_nodos = []
    cir_culos = []
    for nodo in nodos:
        if not nodo.visitado:
            calling_caca_kosacarajo_ordena(nodo, pila_nodos)
    
    while pila_nodos:
        nodo = pila_nodos.pop()
        if not nodo.visitado_transputa:
            miembros = []
            calling_caca_kosacarajo_junta_componentes(nodo, miembros)
            cir_culos.append(miembros)
#    logger_cagada.debug("los cir culotes {}".format(cir_culos))
    return cir_culos

def calling_caca_core(nodos):
    mierdas = calling_caca_kosacarajo(nodos)
    return mierdas

def caca_comun_lee_linea_como_num():
    return int(stdin.readline().strip())

def caca_comun_lee_linea_como_monton_de_numeros():
    return list(map(int, stdin.readline().strip().split(" ")))

def caca_comun_lee_linea():
    return stdin.readline().strip()

def calling_caca_main():
    shit = 0
    caca, mierda = caca_comun_lee_linea_como_monton_de_numeros()
    while(caca or mierda):
        fuck = ""
        ass = []
        if mierda:
            nodos_por_nombre = defaultdict(nodo_caca)
            nodos = []
            nombres_agregados = set()
            for _ in range(mierda):
                nombre1, nombre2 = caca_comun_lee_linea().split(" ")
                nodo1 = nodos_por_nombre[nombre1]
                nodo2 = nodos_por_nombre[nombre2]
                
                nodo1.vecinos.append(nodo2)
                nodo2.vecinos_transputa.append(nodo1)
                
                if nombre1 not in nombres_agregados:
                    nodo1.nombre = nombre1
                    nodos.append(nodo1)
                    nombres_agregados.add(nombre1)
                    
                if nombre2 not in nombres_agregados:
                    nodo2.nombre = nombre2
                    nodos.append(nodo2)
                    nombres_agregados.add(nombre2)
                    
            ass = calling_caca_core(nodos)
        fuck = "\n".join(map(lambda lista:", ".join(list(map(lambda x:x.nombre, lista))), ass))
        logger_cagada.debug("pero la puta madre\n{}".format(fuck))
        print("Calling circles for data set {}:".format(shit + 1))
        if fuck:
            print("{}".format(fuck))
            
            
        caca, mierda = caca_comun_lee_linea_como_monton_de_numeros()
        shit += 1
        if(caca):
            print("")
            
            
            
            

if __name__ == '__main__':
        FORMAT = "[%(filename)s:%(lineno)s - %(funcName)20s() ] %(message)s"
        logging.basicConfig(level=nivel_log, format=FORMAT)
        logger_cagada = logging.getLogger("asa")
        logger_cagada.setLevel(nivel_log)
        calling_caca_main()
