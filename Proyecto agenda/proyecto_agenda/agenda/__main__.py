from agenda.funciones.metodos import MetodosCrud
from agenda.entidades.nota import Nota
from colorama import Fore
import os

class Main:
    #Esta es la clase principal, funciona a traves de un menu que se repite de manera indefinida mientras una variable auxiliar llamada menu no se vuelva 7 
    def main():
        os.system('cls') #Borrado de consola
        listaNotas = MetodosCrud.cargarNotas() #Llamamos al metodo que carga la lista a traves de un archivo json
        menu=0
        while menu!=7:
            try: 
                    print(Fore.GREEN + "Menu principal:")
                    print(Fore.YELLOW + "1. Agregar nota\n2. Mostrar notas\n3. Buscar notas por id\n4. Buscar notas por titulo\n5. Actualizar nota por id\n6. Borrar nota por titulo\n7. Salir")
                    menu= int(input(Fore.CYAN + "Introduce un numero:"))
                    if menu<1 or menu>7:
                        print("Solo números del 1 al 7")
                    else:
                        match menu:
                            case 1: #La primera opción añade una nota a la lista en sesión
                                id= int(input(Fore.YELLOW + "Introduce el id numerico:"))
                                titulo = input(Fore.YELLOW + "Introduce el titulo de la nota:")
                                contenido= input(Fore.YELLOW + "Introduce el contenido:")
                                nuevaNota = Nota(id,titulo,contenido)
                                listaNotas.append(nuevaNota.__dict__)
                            case 2: #La segunda opción muestra la lista en sesion
                                MetodosCrud.mostrarNotas(listaNotas)
                                
                            case 3: #La tercera opcion busca una nota por un id proporcionado por pantalla
                                id = int(input(Fore.YELLOW + "Introduce el Id numerico de la nota:"))
                                MetodosCrud.buscarNotaPorId(id,listaNotas)
                            case 4: #La cuarta opcion busca una nota por un titulo proporcionado por pantalla
                                titu = input(Fore.YELLOW + "Introduce el titulo de la nota:")
                                MetodosCrud.buscarNotaPorTitulo(titu,listaNotas)
                            case 5: #La quinta opcion permite modificar una de las notas (encontrandola por titulo) a traves de prompts por pantalla
                                titu = input(Fore.YELLOW + "Introduce el titulo de la nota:")
                                MetodosCrud.actualizarNotaPorTitulo(titu,listaNotas)
                                
                            case 6: #La sexta opcion borra una nota por titulo
                                titu = input(Fore.YELLOW + "Introduce el titulo de la nota:")
                                MetodosCrud.borrarNotaPorTitulo(titu,listaNotas)
                            case 7: #La septima opcion provoca que termine el menu y guarda la lista en sesion en un archivo json
                                os.system('cls')
                                try:
                                    print(Fore.GREEN + "Aplicación cerrada, guardando cambios...")
                                    MetodosCrud.guardarLista(listaNotas)
                                    menu=7
                                except:
                                     print(Fore.RED + "Error al salir")
            except ValueError:
                    print(Fore.RED + "Se requiere un valor numérico del 1 al 7") #Si se introduce algo distinto de un numero se captura el error
    if __name__ == '__main__':
            main()