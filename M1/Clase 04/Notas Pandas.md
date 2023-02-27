En Pandas en vez de array se utiliza Series, es fundamental las series en pd
Otra función importante es que deja leer y escribir archivos de CSV,Excel y BD SQL

Las series es lo que se vio en Numpy cómo un vector y todos los tipos de datos deben ser iguales
Las tablas también tiene indices auqnue no se ven
Varias series una al lado de la otra forman un DATAFRAME, el dataframe es una tabla de excel, tiene la misma estructura, el DF puede tener elementos de distintos tipos

.value_counts() se puede tomar cómo para ver resultados

NULLO y NAN es lo mismo para pd

.lamda es para declarar una función anónima en Python

El DATAFRAME es una sucesión de filas y columnas(series), es una tabla. También lleva encabezados, el DF se puede crear a partir de un diccionario, de una lista, de una lista de listas, de una lista de diccionarios, etc
La más usada es la de a partir de un diccionario
Se pueden importan de un CSV, SQL, Excel

Se utiliza mayormente un Key(llave) cómo Str

{'juan': [6, 7, 8], 'ana': [7, 7, 7], 'roberto': [7, 5, 9]}
'juan' es el Key [6, 7, 8] es el value

DATETIME sirve para trabajar con fechas, y estas fechas para poder guardarlas se deben de poner en STR

REINDEXAR 

RENAME es para renombrar las filas y columnas

Para eliminar columnas es con DEL
Tambien se puede eliminar con POP que me la saca de la DF pero me guarda lo que eliminó en una variable o serie

Para elimnar filas es con DROP

Para ordenar es con df.sort_values y df.sort_index

Para buscar filas
df.iloc[i,j]  la i es de indice 

Si ene l sep del read no le pongo nada, va a tomar por defecto la coma ','
Si vemos que el archivo es un UTF-8 hay mejor prevenir y ponerlo en encoding


python '.\Repaso Pandas.py'   