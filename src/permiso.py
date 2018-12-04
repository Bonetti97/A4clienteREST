class Permiso(object):
    def __init__(self, id, nombre):
        self.id = id
        self.nombre = nombre
        
    def comoArray(self):
        return {
            'idPermiso':str(self.id),
            'nombre':self.nombre
            }
    def __str__(self):
        return 'id: '+str(self.id)+' nombre '+self.nombre