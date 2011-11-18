from pyramid.config import Configurator
from pyramid.events import subscriber
from pyramid.events import NewRequest
import pymongo
from gridfs import GridFS

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)
    config.scan()

    config.add_static_view('static', 'contacts:static', cache_max_age=3600)
    config.add_route('home', '/')
    config.add_route('view-contact', '/view-contact/{id}')
    config.include('pyramid_jinja2')
    config.add_jinja2_search_path("contacts:templates")                    
                    
    def add_mongo_db(event):
        settings = event.request.registry.settings
        url = settings['mongodb.url']
        db_name = settings['mongodb.db_name']
        db = settings['mongodb_conn'][db_name]
        event.request.db = db
        event.request.fs = GridFS(db)
    db_uri = settings['mongodb.url']
    conn = pymongo.Connection(db_uri)
    config.registry.settings['mongodb_conn'] = conn
    config.add_subscriber(add_mongo_db, NewRequest)
                        
    return config.make_wsgi_app()