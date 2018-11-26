from suds.client import Client
import comic
import entrega



class Controller(object):
    
    wsdl = 'http://localhost:8080/HumilArt/ComicWebService?WSDL'
    client = Client(wsdl)
    client.options.cache.clear()

    def findComicById(self, idComic):
        c = self.client.service.findComicById(idComic)
        if c:
            cam = comic.Comic(c['idComic'],c['nombre'],c['descripcion'],c['fechaCreacion'])
            return cam
        else:
            return None

    def addComic(self,nombre,descripcion):
        self.client.service.addComic(nombre,descripcion)
    def deleteComic(self,comic):
        self.client.service.remove(comic)
    def editComic(self, comic, nuevoNombre,nuevaDescripcion):
        self.client.service.editComic(comic,nuevoNombre,nuevaDescripcion)

    def listComics(self):
        listaComics = []
        lista = self.client.service.findAll()
        for i in range(len(lista)):
            comi = comic.Comic(lista[i]['idComic'],lista[i]['nombre'],lista[i]['descripcion'],lista[i]['fechaCreacion'])
            listaComics.append(comi)
        return listaComics
    
    def listaOrden(self):
        aux=[]
        lista=self.client.service.encontrarPorNombreAlfabetico();
        for i in range(len(lista)):
            comi = comic.Comic(lista[i]['idComic'],lista[i]['nombre'],lista[i]['descripcion'],lista[i]['fechaCreacion'])
            aux.append(comi)
        return aux
    
    def listaFecha(self):
        aux=[]
        lista=self.client.service.encontrarPorFecha();
        for i in range(len(lista)):
            comi = comic.Comic(lista[i]['idComic'],lista[i]['nombre'],lista[i]['descripcion'],lista[i]['fechaCreacion'])
            aux.append(comi)
        return aux
    
    def listaNombre(self,nombre):
        aux=[]
        lista=self.client.service.buscarNombre(nombre);
        for i in range(len(lista)):
            comi = comic.Comic(lista[i]['idComic'],lista[i]['nombre'],lista[i]['descripcion'],lista[i]['fechaCreacion'])
            aux.append(comi)
        return aux
    
    def listaFechaMayor(self,fecha):
        aux=[]
        lista=self.client.service.buscarPorFechaMayor(fecha);
        for i in range(len(lista)):
            comi = comic.Comic(lista[i]['idComic'],lista[i]['nombre'],lista[i]['descripcion'],lista[i]['fechaCreacion'])
            aux.append(comi)
        return aux
    
    def listaNumEntregas(self):
        aux=[]
        lista=self.client.service.buscarPorNumEntrega();
        for i in range(len(lista)):
            comi = comic.Comic(lista[i]['idComic'],lista[i]['nombre'],lista[i]['descripcion'],lista[i]['fechaCreacion'])
            aux.append(comi)
        return aux
    
    def getEntregasComic(self,comic):
        aux=[]
        lista=self.client.service.getEntregasComic(comic);
        for i in range(len(lista)):
            entregas=entrega.Entrega(lista[i]['idEntrega'],lista[i]['nombre'],lista[i]['archivo'],lista[i]['fechaCreacion'],lista[i]['idComic'])
            aux.append(entregas)
        return aux
        
    
    
        
