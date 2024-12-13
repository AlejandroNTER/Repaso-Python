def showAnimal(name,n_legs):
    print(f"El nombre es {name} y tiene {n_legs} piernas.")

showAnimal("Pikachu",4)

def dameCosas(*args):
    print(len(args))

dameCosas(4,2,5,1)

def sumaYResta(num1,num2):
    suma=num1+num2
    resta=num1-num2
    return suma,resta

print(sumaYResta(4,3))

respueta=sumaYResta(4,3)
print(type(respueta))

def multiplicar(num1,num2):
    multiplicacion=num1*num2
    return multiplicacion 

print(multiplicar(2,3))

def obtenerResto(num1,num2):
    modulo=num1%num2
    return modulo 

print(obtenerResto(6,2))

def multiplicarEnFuncion(num1,num2):
    return multiplicar(num1,num2)

print(multiplicarEnFuncion(2,3))

def datosUsuario(nombre,email="Sin determinar"):
    print(nombre,email)

print(datosUsuario("Virginia"))

def sumarRetrogrago(num):
    suma=num
    while num >1:
        suma=suma+num-1
        print(suma)
        num-=1
    return suma

sumarRetrogrago(5)

cuadrado = lambda x: x**2
square = cuadrado(2)
print(square)

cuadradoMayor= lambda x: True if x**2>999 else False
resp= cuadradoMayor(20)
print(resp)

multi= lambda x,y: x*y
resp= multi(3,3)
print(resp)

palabras=["Warframe","Cyberpunk","Spideman","Dead by daylight"]
orden=sorted(palabras,key=lambda palabro:palabro[1])
print(orden)

def doble(*args):
    listaDobles=list()
    for each in args:
        listaDobles.append(each*2)
    return listaDobles

print(doble(2,3,4,5))

def cuadradoPares(*args):
    listaCuadrados=list()
    for each in args:
        if each %2==0:
            listaCuadrados.append(each**2)
    return listaCuadrados

print(cuadradoPares(2,3,4))

def sumaDeCeldasLista(lista1,lista2):
    listaFinal=list()
    i=0
    for each in lista1:
        listaFinal.append(each+lista2[i])
        i+=1
    return listaFinal

print(sumaDeCeldasLista([2,4,5],[3,5,1]))

def cuentaAs(lista):
    
    listaAs=list()
    for each in lista:
        contAs=0
        for letra in each:
            if letra == "a" or letra=="A":
                contAs+=1
        listaAs.append(contAs)
    return listaAs

print(cuentaAs(["Patata","Vino","Almeja","Concha"]))
    
def mostrarNegativos(lista):
    listaNegativos=list()
    for each in lista:
      if each <0:
                listaNegativos.append(each)
    return listaNegativos

print(mostrarNegativos([2,-4,1,-1,-7]))

def sacarNumeros(string):
    sumaString=0
    for caracter in string:
        if caracter.isdigit():
            sumaString+= int(caracter)
    return sumaString

print(sacarNumeros("Hola me llamo 4 y tengo 5 años."))
