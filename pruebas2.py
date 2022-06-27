
import random as rn
import numpy as np


op=0

def op_uno():
    lis_uno=[]
    lis_dos=[]

    for n in range(0,20):
        lis_uno.append(rn.randrange(20,500))
    print("---------------- Lista 1 ------------------")
    print(lis_uno)
    print("\n")
    print("--------------------- Lista uno mayor a menor ----------------------")
    lis_uno.sort(reverse=True)
    print(lis_uno)
    print("\n")

    print("------------------------------ Lista 2 -----------------------------")
    lis_dos=lis_uno.copy()
    print(lis_dos)

def op_dos():
    lista=[]

    for n in range(0,20):
        lista.append(rn.randrange(50,1000))
    arreglo=np.array(lista)

    print("Numero mayor",arreglo.max())
    print("Menor",arreglo.min())
    print("Suma",arreglo.sum())
    print("Promedio",arreglo.mean())
    print("Completo",arreglo)

    arr_copy=arreglo.copy()

    print("Copia",arr_copy)
def op_tres():
    # Metodo 1
    lis_uno=[]
    lis_dos=[]
    lis_tres=[]
    lis_cuatro=[]
    lis_cinco=[]

    for n in range(0,5):
        lis_uno.append(rn.randrange(0,300))
        lis_dos.append(rn.randrange(0,300))
        lis_tres.append(rn.randrange(0,300))
        lis_cuatro.append(rn.randrange(0,300))
        lis_cinco.append(rn.randrange(0,300))


    arreglo=np.matrix([lis_uno,lis_dos,lis_tres,lis_cuatro,lis_cinco])

    print(arreglo.mean())
    print(arreglo.sum())
    print(arreglo.max())
    print(arreglo.min())
    print(arreglo.diagonal())
    #faltala diagonal inversa
    print(arreglo)

    




while op!= 4:
    print("1 -> Lisatas")
    print("2 -> Vectores")
    print("3 -> Matrices")
    print("4 -> Salir")
    op=int(input("Ingrese opcion: "))

    if op==1:
        print(op_uno())
    if op==2:
        print(op_dos())
    if op==3:
        print(op_tres())
    if op==4:
        print("Salir")
    
