import datetime
import controller
class Comic(object):
    def __init__(self, id, nombre, descripcion, fechaCreacion):
        self.idComic = id
        self.nombre = nombre
        self.descripcion = descripcion
        self.fechaCreacion = fechaCreacion
   #     self.idUsuario = idUsuario
        self.listaEntrega=controller.Controller().getEntregasComic(id)
        
    def comoArray(self):
        return {
            'idComic':str(self.idComic),
            'nombre':self.nombre,
            'descripcion':self.descripcion,
            'fechaCreacion':self.fechaCreacion,
            'usuario':self.idUsuario
            }
    def __str__(self):
        return 'id: '+str(self.idComic)+' nombre '+self.nombre+' descripcion: '+self.descripcion+ 'fechaCreacion'+ self.fechaCreacion + 'usuario: '+ self.idUsuario
