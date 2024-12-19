class Nota:
    """Clase objeto principal"""
   
    def __init__(self,id,titulo,contenido):
        self.id=id
        self.titulo=titulo
        self.contenido=contenido
        
    def getId(self):
        """Funcion que devuelve el titulo de la nota"""
        return self.id
    def getTitulo(self):
        """Funcion que devuelve el titulo de la nota"""
        return self.titulo
    def getContenido(self):
        """Funcion que devuelve el contenido de la nota"""
        return self.contenido
    def setTitulo(self,nuevoTitulo):
        """Funcion que asigna el titulo de la nota"""
        self.titulo=nuevoTitulo
    def setContenido(self,nuevoContenido):
        """"Funcion que asigna el contenido de la nota"""
        self.contenido=nuevoContenido
    def setId(self,nuevoId):
        """Funcion que devuelve el contenido de la nota"""
        self.id=nuevoId