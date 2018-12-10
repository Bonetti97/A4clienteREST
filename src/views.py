import os
import webapp2
import jinja2
from controller import Controller
import requests



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
    
        
        
class login(BaseHandler):
    def get(self):
        self.render_template('login.html', {})

class guardarSesion(BaseHandler):
    def get(self,idUsuario):
        #Controller().login(idUsuario)
        return webapp2.redirect("/showComics/"+idUsuario);
        
class invitado(BaseHandler):
    def get(self): 
         
        cos = Controller().listComics(str(2)) 
        self.render_template('invitado.html', {'listaComic': cos})
        
class showComics(BaseHandler):
    def get(self,idUsuario): 
        o = Controller().login()  
        usuario = Controller().findUsuario(o)
        cos = Controller().listComics(o) 
       
        
        self.render_template('comics.html', {'listaComic': cos , 'permiso' : usuario.permiso})
        
class AddComic(BaseHandler):
    def get(self):
        self.render_template('newComic.html', {})
    
    def post(self):
        Controller().addComic(self.request.get('nombreComic'), 
                              self.request.get('descripcionComic'))
        id = Controller().login()
        return webapp2.redirect('/showComics/'+id )
        
class EditComic(BaseHandler):
    def get(self, comicID):      
        co = Controller().findComicById(int(comicID))
        self.render_template('editarComic.html', {'comic': co})
        
    def post(self,comicID):
        nombre = self.request.get('nombreComic')
        descripcion = self.request.get('descripcionComic')
        Controller().editComic(comicID, nombre, descripcion)
        id = Controller().login()
        return webapp2.redirect('/showComics/'+id)

class DeleteComic(BaseHandler):
    def get(self, comicID):
        Controller().deleteComic(comicID)
        id = Controller().login()
        return webapp2.redirect('/showComics/'+id)
    
class doPremium(BaseHandler):
    def get(self):
        Controller().doPremium()
        id = Controller().login()
        return webapp2.redirect('/showComics/'+id)    
    
class OrdenAlfabetico(BaseHandler):
    def get(self):
        o = Controller().login()  
        usuario = Controller().findUsuario(o)
        cos=Controller().listaOrden()
        self.render_template('comics.html', {'listaComic': cos, 'permiso' : usuario.permiso})
        
class OrdenFecha(BaseHandler):
    def get(self):
        o = Controller().login()  
        usuario = Controller().findUsuario(o)
        cos=Controller().listaFecha()
        self.render_template('comics.html', {'listaComic': cos,'permiso' : usuario.permiso})
        
class BuscarNombre(BaseHandler):
    def get(self):
        o = Controller().login()  
        usuario = Controller().findUsuario(o)
        nombre = self.request.get('busquedaNombre')
        cos=Controller().listaNombre(nombre)
        self.render_template('comics.html', {'listaComic': cos,'permiso' : usuario.permiso})
        
class BuscarFechaMayor(BaseHandler):
    def get(self):
        o = Controller().login()  
        usuario = Controller().findUsuario(o)
        fecha=self.request.get('busquedaFechaMayor')
        cos=Controller().listaFechaMayor(fecha)
        self.render_template('comics.html', {'listaComic': cos,'permiso' : usuario.permiso})
        
class OrdenEntregas(BaseHandler):
    def get(self):
        o = Controller().login()  
        usuario = Controller().findUsuario(o)
        cos=Controller().listaNumEntregas();
        self.render_template('comics.html', {'listaComic': cos,'permiso' : usuario.permiso})



        
        
        
        
        
        
        
        
        
        
        
        