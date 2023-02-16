def NumeroBinario(numero):
    if type(numero) != int or numero < 0: return None #empezamos a evitar que ingresen # no enteros
    elif numero == 0: return 0   #retorna a 0 ya que en bi 0 es 0
    binario = ''  #para ir armando los 0010 lo declaro cómo str vacío
    div_resto = 0   #es el que va a ir tomando los valores de la división
    while numero > 0:   #este loop hasta que la parrte entera sea 0
        div_resto = numero % 2 #acá voy a almacenar lo que devuelva el resto div 2
        numero //= 2  #de acá sólo quiero la parte entera
        binario += str(div_resto) #par air metiendo la información que me va dando el div resto
    return int(binario[::-1])  #el ejercicio me pide que si es un str lo retome como entero (int) , [::-1] significa que traigo todo pero para atrás, ya que si no le pongo eso me scaa el binario al revés



#otra solución 
def NumeroBinario(numero):
    if type(numero) != int or numero < 0: return None 
    elif numero == 0: return 0 
    binario = '' 
    div_resto = 0  
    while numero > 0: 
        div_resto = numero % 2 
        numero //= 2
        binario = str(div_resto) + binario  #para que primero me ponga la div resto y luego lo que va quedando
        return(int(binario))
        #binario += str(div_resto) 
    #return int(binario[::-1])  el -1 significa que vaya hacia atrás
