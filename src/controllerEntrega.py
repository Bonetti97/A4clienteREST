from suds.client import Client
import entrega



class ControllerEntrega(object):
    
    wsdl = 'http://localhost:8080/HumilArt/EntregaWebService?WSDL'
    client = Client(wsdl)
    client.options.cache.clear()
    
    def findEntrega(self, idEnt):
        print idEnt
        e = self.client.service.find(idEnt);
        if e:
            en = entrega.Entrega(e['idEntrega'],e['nombre'],e['archivo'],e['fechaCreacion'],e['idComic'])
            return en
        else:
            return None

    def addEntrega(self,nombre,archivo,idComic):
        self.client.service.addEntrega(nombre,archivo,idComic)
    def deleteEntrega(self,entrega):
        self.client.service.remove(entrega)
    def editEntrega(self, entrega, nuevoNombre):
        self.client.service.editEntrega(entrega,nuevoNombre)
        
    def listEntregas(self):
        aux = []
        lista = self.client.service.findAll();
        for i in range(len(lista)):
            ent = entrega.Entrega(lista[i]['idEntrega'],lista[i]['nombre'],lista[i]['archivo'],lista[i]['fechaCreacion'],lista[i]['idComic'])
            aux.append(ent)
        return aux
    
    def listEntregasNombreInverso(self,comic):
        aux = []
        lista = self.client.service.orderInversoNombre(comic);
        for i in range(len(lista)):
            ent = entrega.Entrega(lista[i]['idEntrega'],lista[i]['nombre'],lista[i]['archivo'],lista[i]['fechaCreacion'],lista[i]['idComic'])
            aux.append(ent)
        return aux
            
    def findByDate(self, idComic):
        aux = []
        lista = self.client.service.findByFechaDesc(idComic)
        for i in range(len(lista)):
            ent = entrega.Entrega(lista[i]['idEntrega'],lista[i]['nombre'],lista[i]['archivo'],lista[i]['fechaCreacion'],lista[i]['idComic'])
            aux.append(ent)
        return aux
    
    def findByTamano(self):
        aux = []
        lista = self.client.service.findByTamano();  
        for i in range(len(lista)):
            ent = entrega.Entrega(lista[i]['idEntrega'],lista[i]['nombre'],lista[i]['archivo'],lista[i]['fechaCreacion'],lista[i]['idComic'])
            aux.append(ent)
        return aux
    
    def filtrarPorFecha(self,fecha,comic):
        aux = []
        lista = self.client.service.filtrarPorFecha(fecha,comic);  
        for i in range(len(lista)):
            ent = entrega.Entrega(lista[i]['idEntrega'],lista[i]['nombre'],lista[i]['archivo'],lista[i]['fechaCreacion'],lista[i]['idComic'])
            aux.append(ent)
        return aux
    
    def getFoto(self,idEntrega):
        foto=self.client.service.getFoto(idEntrega)
        return foto
    
    