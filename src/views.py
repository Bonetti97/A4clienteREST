import os
import webapp2
import jinja2
from controller import Controller



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
        self.render_template('comics.html', {'listaComic': cos})
        
class AddComic(BaseHandler):
    def get(self):
        self.render_template('newComic.html', {})
    
    def post(self):
        Controller().addComic(self.request.get('nombreComic'), 
                              self.request.get('descripcionComic'))
        return webapp2.redirect('/')
        
class EditComic(BaseHandler):
    def get(self, comicID):      
        co = Controller().findComicById(int(comicID))
        self.render_template('editarComic.html', {'comic': co})
        
    def post(self,comicID):
        nombre = self.request.get('nombreComic')
        descripcion = self.request.get('descripcionComic')
        Controller().editComic(comicID, nombre, descripcion)
        return webapp2.redirect('/')

class DeleteComic(BaseHandler):
    def get(self, comicID):
        Controller().deleteComic(comicID)
        return webapp2.redirect('/')
    
class OrdenAlfabetico(BaseHandler):
    def get(self):
        cos=Controller().listaOrden()
        self.render_template('comics.html', {'listaComic': cos})
        
class OrdenFecha(BaseHandler):
    def get(self):
        cos=Controller().listaFecha()
        self.render_template('comics.html', {'listaComic': cos})
        
class BuscarNombre(BaseHandler):
    def get(self):
        nombre = self.request.get('busquedaNombre')
        cos=Controller().listaNombre(nombre)
        self.render_template('comics.html', {'listaComic': cos})
        
class BuscarFechaMayor(BaseHandler):
    def get(self):
        fecha=self.request.get('busquedaFechaMayor')
        print fecha
        cos=Controller().listaFechaMayor(fecha)
        self.render_template('comics.html', {'listaComic': cos})
        
class OrdenEntregas(BaseHandler):
    def get(self):
        cos=Controller().listaNumEntregas();
        self.render_template('comics.html', {'listaComic': cos})



        
        
        
        
        
        
        
        
        
        
        
        