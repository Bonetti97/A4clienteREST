
import comic
import entrega
import requests
import json
import usuario

from datetime import datetime
from django.template.defaultfilters import length

service = 'http://localhost:8080/A4servidorREST/webresources/entity.comic/'


class Controller(object):
   

    def findComicById(self, idComic):
        c = requests.get(service+str(idComic))
        c=json.loads(c.text)
       
        if c:
            cam = comic.Comic(c['idComic'],c['nombre'],c['descripcion'],c['fechaCreacion'])
            return cam
        else:
            return None
        
    def findUsuario(self, id):
        c = requests.get('http://localhost:8080/A4servidorREST/webresources/entity.usuario/'+id)
        c=json.loads(c.text)
     
        if c:
            cam = usuario.Usuario(c['idtoken'],c['permiso'],c['idUsuario'])
            return cam
        else:
            return None 
    def premium(self):
        requests.put('http://localhost:8080/A4servidorREST/webresources/entity.usuario/premium')       

    def addComic(self,nombre,descripcion):
        requests.post(service+nombre+'/'+descripcion)
    def deleteComic(self,comic):
        requests.delete(service+str(comic))
    def editComic(self, comic, nuevoNombre,nuevaDescripcion):
        requests.put(service+str(comic)+'/'+nuevoNombre+'/'+nuevaDescripcion)
    
    def login(self):
        o = requests.get('http://localhost:8080/A4servidorREST/webresources/entity.usuario/'+'getID')
        return o.text
        
    
    def listComics(self,idUsuario):    
        listaComics = []
        lista = requests.get(service+'findByUsuario/'+idUsuario)
       
        lista=json.loads(lista.text)
       
        for i in range(len(lista)):
            comi = comic.Comic(lista[i]['idComic'],lista[i]['nombre'],lista[i]['descripcion'],lista[i]['fechaCreacion'])
            
            fec = ((comi.fechaCreacion).encode('ascii','ignore'))[:10]
            comi.fechaCreacion = fec
            listaComics.append(comi)
        return listaComics
    
    def listaOrden(self):
        aux=[]
        lista= requests.get(service+'ordenaComicAlfabetico')
        lista=json.loads(lista.text)
        for i in range(len(lista)):
            comi = comic.Comic(lista[i]['idComic'],lista[i]['nombre'],lista[i]['descripcion'],lista[i]['fechaCreacion'])
            fec = ((comi.fechaCreacion).encode('ascii','ignore'))[:10]
            comi.fechaCreacion = fec
            aux.append(comi)
        return aux
    
    def listaFecha(self):
        aux=[]
        lista=requests.get(service+'ordenaComicFecha')
        lista=json.loads(lista.text)
        for i in range(len(lista)):
            comi = comic.Comic(lista[i]['idComic'],lista[i]['nombre'],lista[i]['descripcion'],lista[i]['fechaCreacion']) 
            fec = ((comi.fechaCreacion).encode('ascii','ignore'))[:10]
            comi.fechaCreacion = fec
            aux.append(comi)
        return aux
    
    def listaNombre(self,nombre):
        aux=[]
        lista=requests.get(service+'buscaNombre/'+nombre)
        lista=json.loads(lista.text)
        for i in range(len(lista)):
            comi = comic.Comic(lista[i]['idComic'],lista[i]['nombre'],lista[i]['descripcion'],lista[i]['fechaCreacion'])
            fec = ((comi.fechaCreacion).encode('ascii','ignore'))[:10]
            comi.fechaCreacion = fec
            aux.append(comi)
        return aux
    
    def listaFechaMayor(self,fecha):
        aux=[]
        lista=requests.get(service+'buscaFecha/'+str(fecha))
        lista=json.loads(lista.text)
        for i in range(len(lista)):
            comi = comic.Comic(lista[i]['idComic'],lista[i]['nombre'],lista[i]['descripcion'],lista[i]['fechaCreacion'])
            fec = ((comi.fechaCreacion).encode('ascii','ignore'))[:10]
            comi.fechaCreacion = fec
            aux.append(comi)
        return aux
    
    def listaNumEntregas(self):
        aux=[]
        lista=requests.get(service+'ordenaComicEntrega')
        lista=json.loads(lista.text)
        for i in range(len(lista)):
            comi = comic.Comic(lista[i]['idComic'],lista[i]['nombre'],lista[i]['descripcion'],lista[i]['fechaCreacion'])
            fec = ((comi.fechaCreacion).encode('ascii','ignore'))[:10]
            comi.fechaCreacion = fec
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
        
    
    def splashApi(self,nombre):
        url='https://api.unsplash.com/search/photos/?client_id=2bcb4891c83542f24955be2b647d4e68184448bfe84e99c75f829f4d2449c575'
        r = requests.get(url+'&query='+nombre)
        lista = r.json()
        if lista['total'] == 0:
            return 'https://bigseoagency.com/wp-content/uploads/2018/03/error-404-foxplay.png'
        imagenAleatoria= lista['results'][0]['urls']['small']
        return imagenAleatoria
    
    def flickr(self,tag):
        clave = "b56fe120d5d60193cdff938b0af0ed91"
        #secreto = '7941625e2330f77c'
        url = 'https://api.flickr.com/services/rest/?method=flickr.photos.search&format=json&api_key='+clave+'&tags='+tag
        r = requests.get(url);
       
        r = r.text[14:]
        r = r[:-1]
        respuesta = json.loads(r)
        lista=  respuesta['photos']['photo']
       
        listaUrl = []
        for i in range(len(lista)):
            
            secret = lista[i]['secret']
            farm = lista[i]['farm']
            server = lista[i]['server']  
            id=lista[i]['id']
            urlfoto = 'http://farm'+str(farm)+'.staticflickr.com/'+str(server)+'/'+str(id)+'_'+str(secret)+'_z.jpg'
            listaUrl.append(urlfoto)
        
        

        return listaUrl
        
        
        
        
