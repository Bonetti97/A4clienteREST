import os
import webapp2
import jinja2
import base64
from controller import Controller
from controllerEntrega import ControllerEntrega



TEMPLATE_DIR = os.path.join(os.path.dirname(__file__), 'templates')
jinja_environment = \
    jinja2.Environment(loader=jinja2.FileSystemLoader(TEMPLATE_DIR))



class BaseHandler(webapp2.RequestHandler):

    def render_template(
        self,
        filename,
        template_values,
        **template_args
        ):
        template = jinja_environment.get_template(filename)
        self.response.out.write(template.render(template_values))
        
        
class showComics(BaseHandler):
    def get(self):     
        cos = Controller().listComics()   
        ent = ControllerEntrega().listEntregas()
        self.render_template('test.html', {'listaComic': cos,'listaEntregas': ent})
        
class AddComic(BaseHandler):
    def get(self):
        self.render_template('test.html', {})
    
    def post(self):
        Controller().addComic(self.request.get('nombreComic'), 
                              self.request.get('descripcionComic'))
        return webapp2.redirect('/')
        
class EditComic(BaseHandler):
    def get(self, comicID):      
        co = Controller().findComicById(int(comicID))
        self.render_template('test.html', {'comic': co})
        
    def post(self):
        id=self.request.get('idComic')
        nombre = self.request.get('nombreComic')
        descripcion = self.request.get('descripcionComic')
        Controller().editComic(id, nombre, descripcion)
        return webapp2.redirect('/')

class DeleteComic(BaseHandler):
    def get(self):
        id=self.request.get('idComic')
        Controller().deleteComic(id)
        return webapp2.redirect('/')
    
class OrdenAlfabetico(BaseHandler):
    def get(self):
        cos=Controller().listaOrden()
        self.render_template('test.html', {'listaComic': cos})
        
class OrdenFecha(BaseHandler):
    def get(self):
        cos=Controller().listaFecha()
        self.render_template('test.html', {'listaComic': cos})
        
class BuscarNombre(BaseHandler):
    def get(self):
        nombre = self.request.get('busquedaNombre')
        cos=Controller().listaNombre(nombre)
        self.render_template('test.html', {'listaComic': cos})
        
class BuscarFechaMayor(BaseHandler):
    def get(self):
        fecha=self.request.get('busquedaFechaMayor')
        cos=Controller().listaFechaMayor(fecha)
        self.render_template('test.html', {'listaComic': cos})
        
class OrdenEntregas(BaseHandler):
    def get(self):
        cos=Controller().listaNumEntregas();
        self.render_template('test.html', {'listaComic': cos})
        
class AddEntrega(BaseHandler):
    def get(self,comicID):
        self.render_template('newEntrega.html', {'comicID':comicID})
    
    def post(self):
        id=self.request.get('idComic')
        archivo = self.request.POST.get("archivoEntrega")
        imgenc = base64.encodestring(archivo.file.read())
        ControllerEntrega().addEntrega(self.request.get('nombreEntrega'),imgenc,id)
        return webapp2.redirect('/')
          
class DeleteEntrega(BaseHandler):
    def get(self):
        id=self.request.get('idEntrega')
        ControllerEntrega().deleteEntrega(id)
        return webapp2.redirect('/')
    
class EditEntrega(BaseHandler):     
    def get(self): 
        id=self.request.get('idEntrega')
        nombre = self.request.get('nombreEntrega')
        ControllerEntrega().editEntrega(id, nombre);
        return webapp2.redirect('/')
    
class OrdenaFechaDesc(BaseHandler):
    def get(self):
        comic = self.request.get('idComic')
        lista=ControllerEntrega().findByDate(comic)
        self.render_template('test.html', {'listaEntregas': lista})

class OrdenNombreInverso(BaseHandler):
    def get(self):
        comic = self.request.get('idComic')
        lista=ControllerEntrega().listEntregasNombreInverso(comic)
        self.render_template('test.html', {'listaEntregas': lista})

class BuscarFechaMayorEntrega(BaseHandler):
    def get(self):
        fecha=self.request.get('busquedaFechaMayorEntrega')
        comic = self.request.get('idComic');
        lista=ControllerEntrega().filtrarPorFecha(fecha,comic)
        self.render_template('test.html', {'listaEntregas': lista})      
        
        
        
        
        
        
        