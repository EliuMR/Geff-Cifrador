import numpy as np
#Xor
def xor(a, b):
    if a==b:
        return 0
    else:
        return 1
from numpy import random
#Generador de semilla
def Semilla(tamano):
    semilla=''
    for j in range(tamano):
        semilla = str(random.randint(2))+semilla
    return semilla
#Polinomio asociado X**57+X**7+1
def recorrer(semilla,registro,longitud):
    #Creamos el registro con la semilla dada
    for i in range(longitud):
        registro[i]=int(semilla[i])
    #creamos un registro auxiliar en el cual se recorrerá el original
    registroaux=np.zeros(longitud)
    #Recorremos los bits a la derecha, menos el primero
    for i in range(longitud-1):
        registroaux[i+1]=int(registro[i])
    #agregamos la primera casilla dependiendo del polinomio
    s57XORs7=xor(registro[56],registro[6])
    registroaux[0]=s57XORs7
    #sale el último bit del registro
    salida=int(registro[-1])
    #cambiamos el auxiliar al original
    registro=registroaux
    return registro,salida
def flujo(semilla,tamano):
    longitud=57
    if len(semilla)==longitud:
        flujo=[]
        #Para el primer corrimiento
        registro=np.zeros(longitud)
        flujo.append(recorrer(semilla,registro,longitud)[1])
        #Para los siguientes corrimientos
        for i in range(tamano-1):
            semillaaux=''
            for i in range(longitud):
                semillaaux=str(int(recorrer(semilla,registro,longitud)[0][longitud-i-1]))+semillaaux
            semilla=semillaaux
            registro=recorrer(semilla,registro,longitud)[0]

            flujo.append(recorrer(semilla,registro,longitud)[1])
        return(flujo)
    else: print('El tamaño de la semilla no corresponde al grado del polinomio asociado al LFSR',len(semilla))
#Polinomio asociado X**32+X**7+X**6+X**2+1
def recorrer1(semilla,registro,longitud):
    #Creamos el registro con la semilla dada
    for i in range(longitud):
        registro[i]=int(semilla[i])
    #creamos un registro auxiliar en el cual se recorrerá el original
    registroaux=np.zeros(longitud)
    #Recorremos los bits a la derecha, menos el primero
    for i in range(longitud-1):
        registroaux[i+1]=int(registro[i])
    #agregamos la primera casilla dependiendo del polinomio
    s32XORs7=xor(registro[31],registro[6])
    s6XORs32XORs7=xor(s32XORs7,registro[5])
    s2XORs6XORs32XORs7=xor(s6XORs32XORs7,registro[1])
    registroaux[0]=s2XORs6XORs32XORs7
    #sale el último bit del registro
    salida=int(registro[-1])
    #cambiamos el auxiliar al original
    registro=registroaux
    return registro,salida
def flujo1(semilla,tamano):
    longitud=32
    if len(semilla)==longitud:
        flujo=[]
        #Para el primer corrimiento
        registro=np.zeros(longitud)
        flujo.append(recorrer1(semilla,registro,longitud)[1])
        #Para los siguientes corrimientos
        for i in range(tamano-1):
            semillaaux=''
            for i in range(longitud):
                semillaaux=str(int(recorrer1(semilla,registro,longitud)[0][longitud-i-1]))+semillaaux
            semilla=semillaaux
            registro=recorrer1(semilla,registro,longitud)[0]

            flujo.append(recorrer1(semilla,registro,longitud)[1])
        return(flujo)
    else: print('El tamaño de la semilla no corresponde al grado del polinomio asociado al LFSR',len(semilla))
#Polinomio asociado X**130+X**3+1
def recorrer2(semilla,registro,longitud):
    #Creamos el registro con la semilla dada
    for i in range(longitud):
        registro[i]=int(semilla[i])
    #creamos un registro auxiliar en el cual se recorrerá el original
    registroaux=np.zeros(longitud)
    #Recorremos los bits a la derecha, menos el primero
    for i in range(longitud-1):
        registroaux[i+1]=int(registro[i])
    #agregamos la primera casilla dependiendo del polinomio
    s130XORs3=xor(registro[129],registro[2])
    registroaux[0]=s130XORs3
    #sale el último bit del registro
    salida=int(registro[-1])
    #cambiamos el auxiliar al original
    registro=registroaux
    return registro,salida
def flujo2(semilla,tamano):
    longitud=130
    if len(semilla)==longitud:
        flujo=[]
        #Para el primer corrimiento
        registro=np.zeros(longitud)
        flujo.append(recorrer2(semilla,registro,longitud)[1])
        #Para los siguientes corrimientos
        for i in range(tamano-1):
            semillaaux=''
            for i in range(longitud):
                semillaaux=str(int(recorrer2(semilla,registro,longitud)[0][longitud-i-1]))+semillaaux
            semilla=semillaaux
            registro=recorrer2(semilla,registro,longitud)[0]

            flujo.append(recorrer2(semilla,registro,longitud)[1])
        return(flujo)
    else: 
        print('El tamaño de la semilla no corresponde al grado del polinomio asociado al LFSR',len(semilla))
#cifrador de flujo usando el generador de Geffe
def Geffe(tamano):
    salida=''
    semilla=Semilla(57)
    a1=flujo(semilla,tamano)
    semilla=Semilla(32)
    a2=flujo1(semilla,tamano)
    semilla=Semilla(130)
    a3=flujo2(semilla,tamano)
    #print(a1,a2,a3)
    #La salida del generador:
    for i in range(tamano):
        b=xor((a1[i] and a2[i]),((not a1[i]) and a3[i]))
        salida=str(b)+salida
    return(salida)
#convertir una letra a binario
def ascii_a_binario(letra):
    # Extraer su valor entero
    valor = ord(letra)
    # Convertirlo a binario
    return "{0:08b}".format(valor)
#convertir a ascci un byte
def binario_a_ascii(binario):
    # Convertir binario a decimal
    valor = int(binario, 2)
    # Convertir el decimal a su representación ASCII
    return chr(valor)
#Un texto completo a binario
def TextoBinario(texto):
    conversion=''
    for i in range(len(texto)):
        conversion=conversion+ascii_a_binario(texto[i])
    return conversion
#Cadena binaria a texto
def BinarioTexto(binario):
    texto=''
    longitud=int(len(binario)/8)
    for i in range(longitud):
        aux=binario_a_ascii(binario[0+8*i:8+8*i])
        texto=aux+texto
    return texto[::-1] #Para que nos regrese el texto invertido, sino regresa el texto invertido
#Encriptar mediante geff xor con la clave
def Encriptar(string):
    stringBinario=TextoBinario(string)
    llave=Geffe(len(stringBinario))
    encriptado=''
    for i in range(len(stringBinario)):
        encriptado=encriptado+str(xor(llave[i],stringBinario[i]))
    textoEncriptado=BinarioTexto(encriptado)
    #print(encriptado)
    #print(stringBinario)
    llaveA=BinarioTexto(llave)
    #print('La llave en binario es: ',llave)
    return llaveA,textoEncriptado
#Decifrador mediante llaver xor mensaje encriptado
def Desencriptar(llave,textoEncriptado):
    binarioString=TextoBinario(textoEncriptado)
    llave=TextoBinario(llave)
    #print(binarioString)
    desifrado=''
    for i in range(len(binarioString)):
        desifrado=desifrado+str(xor(llave[i],binarioString[i]))
    #print(desifrado)
    textoDesifrado=BinarioTexto(desifrado)
    return textoDesifrado
#Menu
def Menu():
    print('---------------------------------------')
    print('Eliga lo deseado: ')
    print('1-Cifrar Texto')
    print('2-Descifrar texto')    
    print('---------------------------------------')
    eleccion=int(input())
    if eleccion==1:
        print('Escriba el texto a cifrar')
        texto=input()
        textoEncriptado=Encriptar(texto)
        print(textoEncriptado)
    elif eleccion==2:
        print('Escriba la llave')
        llave=input()
        print('Escriba el teto cifrado')
        textoEncriptado=input()
        texto=Desencriptar(llave, textoEncriptado)
        print(texto)
    else:
        print('Escriba una elección válido (1,2)')
Menu()