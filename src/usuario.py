class Usuario(object):
    def __init__(self, token, permiso, id):
        self.id = id;
        self.token = token
        self.permiso = permiso
        
    def comoArray(self):
        return {
            'id':str(self.id),
            'token':self.token,
            'permiso':self.permiso
            }
    def __str__(self):
        return 'id: '+self.id+' token: '+self.token+' permiso: '+self.permiso
