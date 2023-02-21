import numpy as np

#para crear una lista con np,debo de poner np.array antes del arreglo [], acaso con lista se puede hacer derecho
#se puede observar que al momento de imprimir estos dos, el array no pone ,
lista = [1,2,3,4,5]
array = np.array(lista)
print(lista)
print(array)

#matriz es una lista de listas
matriz = [[1,2,3],
          [4,5,6],
          [7,8,9]]

print(matriz[1][2])  #queremos encontra el # de la fila 1 - columna 2

#no hay necesidad de crear una lista para un arreglo
array_1 = np.array([1,2,3,4])  
print(array_1)
print(type(array_1))

#arange con secuencia - es un range pero en np
secuencia = np.arange(1,23)
print(secuencia, "secuencia")

#con impares
impares = np.arange(1,26,2)   #del 1 hasta el 26 pero de 2 en 2 
print(impares, "impares secuencia con arange")

#se puede hacer de manera más técnica
print(np.arange(start=2, stop=10, step=2))

#linspace si es inclusivo con los # finales, es para calcular la distancia entre cada valor
secuencia_1 = np.linspace(1, 21, 5, dtype=int)
print(secuencia_1, "linspace")

#predefinidos con zeros, ones , full, linspace, full_like, etc
ceros = np.zeros(5) #este me llna con ceros los # que imprimo
print(ceros, "zeros")

unos = np.ones(5)
print(unos, "ones")
print(unos.dtype, "tipo")

unos_1 = np.ones((2,3))  #me crea una matriz de 1
print(unos_1)

custom = np.full((2,5), 5)  #2 filas de 5 columnas y de puros 5
print(custom, "full")
print(custom ** 2) #y quiero agregar todo eso al cuadrado y esto no se puede hacer con una lista

base = np.linspace(2,6,4)
print(np.full_like(base, np.pi), "full like")  #a diferencia del linspace si me llena todo

#aeleatorio   rand es un metodo de random
#array de # al azar
aeleatorio = np.random.rand(5,3)   #5 filas por 3 columnas
print(aeleatorio, "aeleatorio")

enteros = np.random.randint(1,10,(2,3))
print(enteros, "randint")

#multiplicación con lista y arreglo
#En lista si multiplicamos a * b nos da error
#en array nos deja hacerlo derecho, es una de las diferencias
x = np.array([1,2,3]) 
y = np.array([3,4,5])
print(x * y)  #esto sería un vector

#en suma si se deja hacer la suma para los dos, pero lo ejecuta de manera diferente
ab = [1,2,3]
ba = [4,5,6]

print(ab + ba)
print(x + y)

#matriz 2d con lista dentro de una lista
b = np.array([[9.0,8.0,7.0],[6.0,5.0,4.0]])
print(b)

#saber las dimensiones de las matrices
print(x.ndim)

#Trabajar con Shape(forma)
print(b.shape)
print(x.shape)

#rshape para cambiar las dimensiones de las matrices o arreglos(arrays)


#solución punto c ejercicio 1
arr_1 = np.array([4,5,6,7])
print(arr_1)
print(" Shape =" , arr_1.shape)

arr_2 = np.array([[2,4]])
print(arr_2)
print(" Shape =" , arr_2.shape)

arre_3 = np.array([[2,6,8,9,4]]).T
print(arre_3, " Shape =" , arre_3.shape)