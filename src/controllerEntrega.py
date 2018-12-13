from suds.client import Client
import entrega
import requests
import json
import cgi
import dropbox
from requests.utils import _null


service = 'http://localhost:8080/A4servidorREST/webresources/entity.entrega/'

class ControllerEntrega(object):
    
 
    def findEntrega(self, idEnt):
        print idEnt
        e = requests.get(service+str(idEnt))
        e=json.loads(e.text)
      
        if e:
            en = entrega.Entrega(e['idEntrega'],e['nombre'],e['archivo'],e['fechaCreacion'],e['idComic'])
            return en
        else:
            return None

    def addEntrega( self,nombre,archivo,idComic):
        if isinstance(archivo, cgi.FieldStorage): #si es archivo
            link = self.dropboxAPI(archivo)        
        else:    
            link = archivo
            
        url = json.dumps(link)
        requests.post(service+nombre+'/'+idComic , data=url, headers={'Content-type': 'application/json'} )
        
      
    def deleteEntrega(self,entrega):
        requests.delete(service+str(entrega))
    def editEntrega(self, entrega, nuevoNombre):
        requests.put(service+str(entrega)+'/'+nuevoNombre)
     
    def getIdComic(self,idEntrega):
       
        id = requests.get(service+'getComic/'+idEntrega)
        
        return id.text
        
    def listEntregas(self):
        aux = []
        lista = requests.get(service+'findAll')
        lista=json.loads(lista.text)
        for i in range(len(lista)):
            ent = entrega.Entrega(lista[i]['idEntrega'],lista[i]['nombre'],lista[i]['archivo'],lista[i]['fechaCreacion'],lista[i]['idComic'])
            aux.append(ent)
        return aux
    
    def listEntregasNombreInverso(self,comic):
        aux = []
        lista = requests.get(service+'ordenaEntregaNombreInverso/'+str(comic))
        lista=json.loads(lista.text)
        for i in range(len(lista)):
            ent = entrega.Entrega(lista[i]['idEntrega'],lista[i]['nombre'],lista[i]['archivo'],lista[i]['fechaCreacion'],lista[i]['idComic'])
            aux.append(ent)
        return aux
            
    def findByDate(self, idComic):
        aux = []
        lista = requests.get(service+'ordenaEntregaFecha/'+str(idComic))
        lista=json.loads(lista.text)
        for i in range(len(lista)):
            ent = entrega.Entrega(lista[i]['idEntrega'],lista[i]['nombre'],lista[i]['archivo'],lista[i]['fechaCreacion'],lista[i]['idComic'])
            aux.append(ent)
        return aux
    
    
    def filtrarPorFecha(self,fecha,comic):
        aux = []
        lista=requests.get(service+'filtraEntregaFecha/'+str(comic)+'/'+str(fecha))
        print lista.text
        lista=json.loads(lista.text)
        for i in range(len(lista)):
            ent = entrega.Entrega(lista[i]['idEntrega'],lista[i]['nombre'],lista[i]['archivo'],lista[i]['fechaCreacion'],lista[i]['idComic'])
            ent.fechaCreacion = ((ent.fechaCreacion).encode('ascii','ignore'))[:10]
            aux.append(ent)
        return aux
    
    def dropboxAPI(self,archivo):
        token = 'ogFMOweiOtMAAAAAAAABzJdFNV3pa3DmR6IKHV8YEknQBFnhwZbWchvApJJMzCd8'
        dbx = dropbox.Dropbox(token) #Conexion con mi cuenta de dropbox    
        f = archivo.file #leo archivo
        response = dbx.files_upload(f.read(), '/Imagenes/'+archivo.filename, mute=True) #Subimos el archivo a mi cuenta de dropbox a la carpeta Imagenes
        respuesta = dbx.sharing_create_shared_link(response.path_lower, False);#Creamos un shared link, para poder compartir la foto y que se vea luego.   
        url = respuesta.url[0:len(respuesta.url)-4]#Esto lo he visto en internet, me ha salvao la vida. El link ke te da esto no es "inyectable" en un img src en html, pero si cambias los parametros finales funciona. Hay que quitarle 4 caracteres ( que es lo que hago con el [0:len(respuesta.url)-4] ), es una funcion de python para dividir un string
        url = url + "raw=1"    #sustituyo por raw=1
        return url
    