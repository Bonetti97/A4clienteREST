import webapp2
from paste import httpserver
import viewsTest

app = webapp2.WSGIApplication([
        ('/',viewsTest.showComics),
        ('/nuevoComic',viewsTest.AddComic),
        ('/nuevaEntrega',viewsTest.AddEntrega),
        ('/editarComic',viewsTest.EditComic),
        ('/editarEntrega',viewsTest.EditEntrega),
        ('/eliminarComic',viewsTest.DeleteComic),
        ('/eliminarEntrega',viewsTest.DeleteEntrega),
        ('/ordenFecha',viewsTest.OrdenFecha),
        ('/buscarNumEntregas', viewsTest.OrdenEntregas),
        ('/buscarFechaMayor', viewsTest.BuscarFechaMayor),
        ('/buscarFechaMayorEntrega',viewsTest.BuscarFechaMayorEntrega),
        ('/ordenFechaEntrega',viewsTest.OrdenaFechaDesc),
        ('/ordenNombreInverso',viewsTest.OrdenNombreInverso),
        ('/buscarNombre', viewsTest.BuscarNombre)
        
        ],
        debug=True)

def main():
    httpserver.serve(app, host='127.0.0.1', port='8282')
if __name__ == '__main__':
    main()