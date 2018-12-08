from suds.client import Client
import comic
import entrega
import requests
import json
import datetime

service = 'http://localhost:8080/A4servidorREST/webresources/entity.comic/'
class Controller(object):
    

    def findComicById(self, idComic):
        c = requests.get(service+str(idComic))
        c=json.loads(c.text)
        print c
        if c:
            cam = comic.Comic(c['idComic'],c['nombre'],c['descripcion'],c['fechaCreacion'])
            return cam
        else:
            return None

    def addComic(self,nombre,descripcion):
        requests.post(service+nombre+'/'+descripcion)
    def deleteComic(self,comic):
        requests.remove(service+str(comic))
    def editComic(self, comic, nuevoNombre,nuevaDescripcion):
        self.client.service.editComic(comic,nuevoNombre,nuevaDescripcion)

    def listComics(self):
        listaComics = []
        lista = requests.get('http://localhost:8080/A4servidorREST/webresources/entity.comic/findAll')
        lista=json.loads(lista.text)
        for i in range(len(lista)):
            comi = comic.Comic(lista[i]['idComic'],lista[i]['nombre'],lista[i]['descripcion'],lista[i]['fechaCreacion'])
            listaComics.append(comi)
        return listaComics
    
    def listaOrden(self):
        aux=[]
        lista= requests.get(service+'ordenaComicAlfabetico')
        lista=json.loads(lista.text)
        for i in range(len(lista)):
            comi = comic.Comic(lista[i]['idComic'],lista[i]['nombre'],lista[i]['descripcion'],lista[i]['fechaCreacion'])
            aux.append(comi)
        return aux
    
    def listaFecha(self):
        aux=[]
        lista=requests.get(service+'ordenaComicFecha')
        lista=json.loads(lista.text)
        for i in range(len(lista)):
            comi = comic.Comic(lista[i]['idComic'],lista[i]['nombre'],lista[i]['descripcion'],lista[i]['fechaCreacion'])
            aux.append(comi)
        return aux
    
    def listaNombre(self,nombre):
        aux=[]
        lista=requests.get(service+'buscaNombre/'+nombre)
        lista=json.loads(lista.text)
        for i in range(len(lista)):
            comi = comic.Comic(lista[i]['idComic'],lista[i]['nombre'],lista[i]['descripcion'],lista[i]['fechaCreacion'])
            aux.append(comi)
        return aux
    
    def listaFechaMayor(self,fecha):
        aux=[]
        lista=requests.get(service+'buscaFecha/'+str(datetime.datetime.strptime(fecha,"%Y-%m-%d")))
        lista=json.loads(lista.text)
        for i in range(len(lista)):
            comi = comic.Comic(lista[i]['idComic'],lista[i]['nombre'],lista[i]['descripcion'],lista[i]['fechaCreacion'])
            aux.append(comi)
        return aux
    
    def listaNumEntregas(self):
        aux=[]
        lista=requests.get(service+'ordenaComicEntrega')
        lista=json.loads(lista.text)
        for i in range(len(lista)):
            comi = comic.Comic(lista[i]['idComic'],lista[i]['nombre'],lista[i]['descripcion'],lista[i]['fechaCreacion'])
            aux.append(comi)
        return aux
    
    def getEntregasComic(self,comic):
        aux=[]
        lista=requests.get('http://localhost:8080/A4servidorREST/webresources/entity.entrega/filtraEntregaComic/'+str(comic))
        lista=json.loads(lista.text)
        for i in range(len(lista)):
            entregas=entrega.Entrega(lista[i]['idEntrega'],lista[i]['nombre'],lista[i]['archivo'],lista[i]['fechaCreacion'],lista[i]['idComic'])
            aux.append(entregas)
        return aux
        
    
    
        
