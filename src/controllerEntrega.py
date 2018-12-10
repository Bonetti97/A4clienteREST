from suds.client import Client
import entrega
import requests
import json
import time
from pyasn1.debug import scope
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
        #url = "https://photoslibrary.googleapis.com/v1/uploads"
        file_name = archivo.filename
        pa = archivo.file.read()
        name = archivo.filename           
        #data = {pa}
        #scope='https://www.googleapis.com/auth/photoslibrary.appendonly'
        #token = 'eyJhbGciOiJSUzI1NiIsImtpZCI6IjBiMDFhOTU4YjY4MGI2MzhmMDU2YzE3ZWQ4NzQ4YmY0YzBiNmQzZTIiLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiJhY2NvdW50cy5nb29nbGUuY29tIiwiYXpwIjoiODA1NjgxMjcxODgwLXN2cXNmbmtqMzFxMzVmMjA0aXJnMGxwN3UyMGtsNmY5LmFwcHMuZ29vZ2xldXNlcmNvbnRlbnQuY29tIiwiYXVkIjoiODA1NjgxMjcxODgwLXN2cXNmbmtqMzFxMzVmMjA0aXJnMGxwN3UyMGtsNmY5LmFwcHMuZ29vZ2xldXNlcmNvbnRlbnQuY29tIiwic3ViIjoiMTA0NjMyNDEwNDUyODAwMTQyMDI0IiwiZW1haWwiOiJqYXZpYm9uZWRAZ21haWwuY29tIiwiZW1haWxfdmVyaWZpZWQiOnRydWUsImF0X2hhc2giOiJMQUxDSC1jUGFueG9Zak9CVGNUZmZRIiwibmFtZSI6IkphdmkgYm9uZWQiLCJwaWN0dXJlIjoiaHR0cHM6Ly9saDQuZ29vZ2xldXNlcmNvbnRlbnQuY29tLy1IZW02Vl9TcUk0QS9BQUFBQUFBQUFBSS9BQUFBQUFBQUFBQS9BR0Rndy1pUjRrUXZzWmRjTzFsWmJPaHBrdVc1LUlFaC1nL3M5Ni1jL3Bob3RvLmpwZyIsImdpdmVuX25hbWUiOiJKYXZpIiwiZmFtaWx5X25hbWUiOiJib25lZCIsImxvY2FsZSI6ImVzIiwiaWF0IjoxNTQ0NDA4MTM4LCJleHAiOjE1NDQ0MTE3MzgsImp0aSI6IjQ3NjIyMDI2ZTNlMmZhYzNhNWNjODQ5N2MxZGMwNWYxYTJjN2FlODkifQ.EtH71XS_Pu6FNhz4Tuz_sTGMIqgJTiaqBiXA4FsDNcSONuxrQEflk0NXeBz5pnjg5D7PA0yWU9mgzJ65sjTa2h6njU92JLlByghqCa25BaTd92uAH3mgCcsbO1b9yobI4XHYpAQlXAiUcsm9ovxjhY8dmw-2H_IxWyZJJf4r1vAprek-DBVQ2_i4XdTkcIUhfVU-Ec9NoUoMIFGWL7NqoPY6Dc0sFShSmQB-VHsu6jfZlciF06Q5la5Vha6WGugs_-h0TRtVaEpGz2VKV85pLiCUUZwB41XnRtucoKUjWrB6urMwwklHXQ78cS4BdJEsqYWPfvAX6uktCVt0OT4zGA'
        #headerss = {'Authorization':'Bearer '+token,
                   'Content-type':'application/octet-stream',
                   'X-Goog-Upload-File-Name': name,
                   'X-Goog-Upload-Protocol': 'raw',}
        r = requests.post(url, data=pa, headers=headerss)
        #url2="https://www.googleapis.com/auth/photoslibrary.appendonly"
        #r2 = requests.get(url)
        #print r2.headers
        #print r2.text
        #time.sleep(15)
       # print r.headers
        #print(r.status_code, r.reason)
        #print r.text
    
    #Ignorad lo comentado, solo son pruebas que hice.
       
        
        
        #requests.post(service+nombre+'/'+str(idComic),data=json.dumps(archivo), headers={'Content-Type':'application/json'})
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
    
    