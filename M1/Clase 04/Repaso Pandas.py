import pandas as pd
import numpy as np

disciplinas = pd.Series(["Matempatica", "Historia", "Economía", "Programación"], dtype="string") #dtype es opcional
print(disciplinas)  #automaticamente me indexa 
print(disciplinas[2]) #ejemplo de traer el indice

#si se quiere hacer un diccionario
dicc = pd.Series({"Matemáticas": 6.0, "Economía" : 4.5, "Programación": 8.5})
print(dicc)

#Atributos
numeros = pd.Series([3,4,5,5,6,7,7])
print(numeros)

#algunos atributos
print((numeros).dtype)
print((numeros).size)
print((numeros).index)  #es lo mismos que range en np

#Métodos
print(numeros.count())  # es para saber la cantidad de elementos que no son nulos o NaN
print(numeros.sum())  #me suma todos los elementos
print(numeros.cumsum())  #es para ver el acumulado de la suma
print(numeros.value_counts())  #me da las frecuencias, o sea cuantas veces aparece cada elemento

#un resumen estadistico de todo cóm la media, moda, etc
print(numeros.describe())

#operadores
print(numeros * 3)

#con el applay puedo aplicar una función
print(numeros.apply(lambda x: x**2+3))  #le va a aplicar(apply) esta función a todos los elementos de la serie

#aplicar máscara
print(numeros > 5)

#para ordenar los valores o elementos
print(numeros.sort_values())
print(numeros.sort_index())
#elimina los datos desconocidos o nulos
#numeros = numeros.dropna()
#numeros.dropna(inplace = True)

#Dataframe
##Creación Dataframe a partide un diccionario
notas = dict(juan=[6,7,8], ana=[7,7,7], roberto=[7,5,9]) #se puede hacer así, siempre que los key sean STR o sino toca hacerlo en modo clásico
df = pd.DataFrame(notas, index=["1° Parcial", "2° Parcial", "3° Parcial"])   #para asignarle nombres a las filas es con .index
print(df)

df = pd.read_csv("colesterol.csv", sep=';', decimal=',')
print(df)
print(df["edad"])
print(type(["edad"])) #tipo
print(df["edad"].mean()) #media

#atributos
print(df.info())  #me da toda la información de la DF
print(df.shape)  #las dimensiones del DF
print(df.size)  #cuenta la cantidad de valores de todo el DF
print(df.columns)  #devuelve la lista con el nombre de las columnas
print(df.columns[3])
print(df.index)  #me trae los indices
print(df.head(10))  #me muestra las 5 primeras filas, puedo decir cuantas 
print(df.tail())  #me muestra los ultimos 5 o los que yo quiera

#Agregar columnas   #este me agrega los datos que quiero y si falta datos este me lo pone cómo Nulos
df["agregados"] = pd.Series([3,4,7,8,9,12])
print(df)

df["agregados"] * 10
print(df)

#Eliminar columnas
del df["agregados"]
print(df)

#Eliminar filas
#df = pd.read_cvs('colesterol.csv')
#print(df.drop([1, 3]))
#otra manera 
#df.drop([2], inplace = True)

#Eliminar Null o NaN
#print(df.dropna())

#Filtrar filas es como una mascara que lelva la filtro pero de variso campos
print(df[(df['sexo'] == 'H') & (df['colesterol'] > 210)])

#Buscar por filas
print(df.iloc[4])  # me trajo todos los datos de esa fila
print(df.iloc[4,2])  #ahora fila - columna  (i,j)

print(df.describe())  #tipo estadistica