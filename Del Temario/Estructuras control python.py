
a= 10
b= 100

if a==10:
    print("Es igual a 10")
else:
    print("Es diferente de 10")

if a==10 & b==10:
    print("Todos son 10")
elif a==10 & b!=10:
    print("Solo a es 10")
elif a!=10 & b==10:
    print("Solo b es 10")
else:
    print("Ninguno es 10")

if a%2!=0 & b%2!=0:
    print("Ambos son impares")
else:
    print("Almenos uno no es impar")



i= 2
if i==2:
    print(i)

if i%2==0:
    print(i)

i=0
while i<10:
    print(i)
    i+=1
    if i==6:
        break


a = ['Hello','World']
b = ['Python',3.9]
c = 'HelloWorldPython'

for char in c:
    print(char)

for item in a:
    print(item)

for each in a:
    print(b)

for item_a, item_b in zip(a, b):
    print(f"Elemento de a: {item_a}, Elemento de b: {item_b}")

for index, value in enumerate(b):
    print(f"Índice: {index}, Valor: {value}")




cuadrados= map(lambda x:x**2,range(10))
print(list(cuadrados))

pares = filter(lambda x: x % 2 ==0, range(20))
print(list(pares))

palabras = ["paloma","PATATA","Colt.9mm","CHIRIMOYA"]
mayusculas = [palabra for palabra in palabras if palabra.isupper()]

print(mayusculas)

imparesDobles= [x*2 for x in range(10) if x%2!=0]
print(list(imparesDobles))

palabros = ["Pepe","Malito","Johnson"]
letras= [x[1] for x in palabros]
print(letras)

liston= [palabras,palabros]
print(liston)
liston= [palabras+palabros]
print(liston)