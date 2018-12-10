from suds.client import Client
import entrega
import requests
import json

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

    def addEntrega(self,nombre,archivo,idComic):
        foto = json.dumps(archivo)
        #print foto
        d = {'param1': 'value1', 'param2': 'value2'}
        a = json.dumps(d)
        #headers={'Content-Type':'x-www-form-urlencoded'}
        #Content-Type':'application/json'
        r= requests.post(service+'crearEntrega',foto,headers={'Content-Type':'application/json', 'Accept': 'application/json'})
        print r.json
        print r
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
        lista=requests.get(service+'filtraEntregaFecha/'+str(comic)+'/'+fecha)
        lista=json.loads(lista.text)
        for i in range(len(lista)):
            ent = entrega.Entrega(lista[i]['idEntrega'],lista[i]['nombre'],lista[i]['archivo'],lista[i]['fechaCreacion'],lista[i]['idComic'])
            aux.append(ent)
        return aux
    
    def getFoto(self,idEntrega):
        foto=requests.get(service+'getFoto/'+str(idEntrega))
     
        return foto.text
    
    