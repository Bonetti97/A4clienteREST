

class Entrega(object):
    def __init__(self, idEntrega, nombre, archivo, fechaCreacion,idComic):
        self.idEntrega = idEntrega
        self.nombre = nombre
        self.archivo = archivo
        self.fechaCreacion = fechaCreacion
        self.idComic = idComic
        
    def comoArray(self):
        return {
            'idEntrega':str(self.idEntrega),
            'nombre':self.nombre,
            'archivo':self.archivo,
            'fechaCreacion':self.fechaCreacion,
            'idComic':self.idComic
            }
    def __str__(self):
        return 'id: '+str(self.idComic)+' nombre '+self.nombre+' fechaCreacion: '+self.descripcion
