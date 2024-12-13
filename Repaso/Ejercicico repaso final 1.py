
import json


listaEmpleados=list()
EmpleadoTest= {"id": 1,"nombre": "Anselmo","edad": 31,"departamento": "Tesorios", "salario": 45.7}
listaEmpleados.append(EmpleadoTest)


def agregarEmpleado(id,nombre,edad,departamento,salario):
    nuevoEmpleado= {"id": id,"nombre": nombre,"edad": edad,"departamento": departamento, "salario": salario}
    listaEmpleados.append(nuevoEmpleado)
def buscarEmpleadoPorId(id):
    for empleado in listaEmpleados:
        if empleado.get("id")==id:
            print(empleado)
def borrarEmpleadoPorId(id):
    for empleado in listaEmpleados:
        if empleado.get("id")==id:
            listaEmpleados.remove(empleado)
def mostrarEmpleados():
        print(listaEmpleados)
def guardarEmpleados():
    fichero1= open("listaDeEmpleados.json","w")
    for empleado in listaEmpleados:
        json.dump(empleado,fichero1)
    fichero1.close()
def cargarEmpleados():

    fichero1= open("listaDeEmpleados.json","r")
    contenido= json.load(fichero1)
    listaEmpleados.append(contenido)
    fichero1.close()

menu=0
while menu!=7:
    print("Menu principal:")
    print("1. Agregar empleado\n2. Buscar empleado por ID\n3. Eliminar empleado por ID\n4. Mostrar todos los empleados\n5. Guardar empleados en un archivo\n6. Cargar empleados desde un archivo\n7. Salir")
    menu= int(input("Introduce un numero:"))
    if menu<1 or menu>7:
        print("Solo números del 1 al 7")
    else:
        match menu:
            case 1:
                id = int(input("Introduce el id:"))
                nombre= input("Introduce el nombre:")
                edad= int(input("Introduce la edad:"))
                departamento= input("Introduce el departamento:")
                salario= float(input("Introduce el salario:"))
                agregarEmpleado(id,nombre,edad,departamento,salario)
            case 2:
                id = int(input("Introduce el id:"))
                buscarEmpleadoPorId(id)
            case 3:
                id = int(input("Introduce el id:"))
                borrarEmpleadoPorId(id)
            case 4:
                mostrarEmpleados()
            case 5:
                guardarEmpleados()
            case 6:
                cargarEmpleados()
            case 7:
                menu=7

