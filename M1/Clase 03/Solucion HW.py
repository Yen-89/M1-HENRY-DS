#Ejercicio 1
#operaciones en lista y en arreglo
import numpy as np
lista = [1,2,3,4,5]
arreglo = np.array([1,2,3,4,5])
print(lista)
print(arreglo)

#puedo llamar por el indice
print(lista[1])
print(arreglo[1])

#asignar valores o reemplzar
lista[0] = 0
arreglo[0] = 0
print(lista, "lista")
print(arreglo, "arreglo")

#numpy puede crear una lista rápidamente
arreglo_1 = np.arange(8)
print(arreglo_1)

secuencia = list(range(8))
print(secuencia)

#de otra manera
secuencia_1 = [i for i in range(8)]
print(secuencia, "con i")

#cosas que puede hacer array pero no listas
print(arreglo + 1, "aumentar array") #para que le sume 1 a cada número de lista
print(np.sum(arreglo)) #sumar todos los # del arreglo entre si

#cosas que se pued ehacer con una lista pero no con un array
elemento = [2,3,6, "Hola"]  #si hago esto con array em pasa todos los valores a STR
print(elemento)
vector = np.array(elemento)
print(vector)



#solución punto c ejercicio 1
print("Arreglo de (n,)")
arr_1 = np.array([4,5,6,7])
print(arr_1)
print(arr_1, " Shape =" , arr_1.shape, "\n") #"\n"  imprime un saldo de lineas

print("Arreglo de (2,n)")
arr_2 = np.array([[2,4,6,8]]) #notar los corchetes extras
print(arr_2)
print(arr_2, " Shape =" , arr_2.shape, "\n")

print("Arreglo de (n,1)")
arre_3 = np.array([[2,6,8,9,4]])
print(arre_3.T, " Shape =" , arre_3.T.shape, "\n")

#solución ejercicio 2
enteros = np.arange(0,10)
print(enteros, "ent")

ente = np.arange(10) #forma profesor
print(ente)

print(np.set_printoptions(2)) #para que me muestre sólo con 2 decimales, recordar que siempe va arriba de la variable
equiespaciado = np.linspace(0, 9, 100)
print(equiespaciado, "lispace")
print(equiespaciado.size, "elementos")  #size para sacer cuántos elementos tiene
print(len(equiespaciado))  #otra forma de saber cuantos elementos tiene

#Ejercicio 3    #ejercicio de la mascara
ente_1 = np.arange(10,101)
#divisibles = ente_1%3 == 0  con este muestro True y False de todos los #
divisibles = ente_1[ente_1 % 3 == 0]  #con este solo muestro los # divisibles por 3
print(divisibles)

ente_2 = np.array([2,4,5,7,9,12,35])  #otra forma de hacer mascara
divisibles_2 = ente_2[(ente_2 % 3 == 0) & (ente_2 > 9)]  #se puede hacer doble mascara
print(divisibles_2, "doble mask")

#Ejercicio 4 
ceros = np.zeros((5,10))  #Shape(forma)
print(ceros, "zeros")
#ceros = np.zeros((5,10), dtypw=int)

ceros[(1,3), :] = 1  #acá le digo que me coja la fila 2 y 4 (indices) y toda la columna :  y reemplza por 1
ceros[:, (2,7)] = 2 #coja toda las filas pero coja las columnas 3 y 8 y reemplce por 2
print(ceros, "ceros - unos - dos")

#combinando los dos
ceros_1 = np.zeros((5,10))
ceros_1[1,:] = 1
ceros_1[:,3] = 1
print(ceros_1, "combinado")


