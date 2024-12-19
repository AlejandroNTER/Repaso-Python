import json
from colorama import Fore
from agenda.entidades.nota import Nota
class MetodosCrud:
    def guardarLista(listaNotas):
        #Metodo que guarda la lista directamente a JSON
        try:
            with open("proyecto_agenda/agenda/recursos/archivoNotas.json", "w") as file:
                json.dump(listaNotas,file, indent=2)
                file.close()
        except ValueError:
             print(Fore.RED + "Error en el archivo json")

    def mostrarNotas(listaNotas):
            #Metodo que muestra la lista por pantalla
            print(listaNotas)

    def cargarNotas():
        #Metodo que carga la lista de JSON
        listaNotas= list()
        file= open("proyecto_agenda/agenda/recursos/archivoNotas.json","r")
        contenido= json.load(file)
        listaNotas.append(contenido)
        file.close()
        return listaNotas

    def buscarNotaPorId(id,listaNotas):
        #Metodo que busca por id en la lista en sesion
        listaDeIds= [t["id"] for t in listaNotas]
        try:
             indice= listaDeIds.index(id)
        except ValueError:
            indice=None
        if indice is not None:
             print(listaNotas[indice])
        else:
            print(Fore.RED + f"No se encuentra la nota con id {id}")
    
    def buscarNotaPorTitulo(titulo,listaNotas):
        #Metodo que busca por titulo en la lista en sesion
        listaDeTitulos= [t['titulo'] for t in listaNotas]
        try:
             indice= listaDeTitulos.index(titulo)
        except ValueError:
            indice=None
        if indice is not None:
             print(listaNotas[indice])
        else:
            print(Fore.RED + f"No se encuentra la nota con titulo {titulo}")


    def actualizarNotaPorTitulo(titulo,listaNotas):
        #Metodo que busca por titulo en la lista en sesion y despues permite modificar los parametros
        nuevoTitu=""
        nuevoCont=""
        
        listaDeTitulos= [t['titulo'] for t in listaNotas]
        try:
             indice= listaDeTitulos.index(titulo)
        except ValueError:
            indice=None
        if indice is not None:
            nota=listaNotas[indice]
            opcion = input(Fore.YELLOW + "¿Quieres modificar el titulo? S/N")
            if opcion=="S" or opcion=="s":
                            nuevoTitu= input(Fore.YELLOW + "Introduce el nuevo titulo de la nota:")
                            nota["titulo"] = nuevoTitu
            opcion = input("¿Quieres modificar el contenido? S/N")
            if opcion=="S" or opcion=="s":
                            nuevoCont= input(Fore.YELLOW + "Introduce el nuevo contenido de la nota:")
                            nota["contenido"] = nuevoCont           
        else:
            print(Fore.RED + f"No se encuentra la nota con titulo {titulo}")

    def borrarNotaPorTitulo(titulo,listaNotas):
        #Metodo que busca por titulo en la lista en sesion y borrar la nota si la encuentra
        listaDeTitulos= [t['titulo'] for t in listaNotas]
        try:
             indice= listaDeTitulos.index(titulo)
        except ValueError:
            indice=None
        if indice is not None:
             listaNotas.remove(listaNotas[indice])
        else:
            print(Fore.RED + f"No se encuentra la nota con titulo {titulo}")