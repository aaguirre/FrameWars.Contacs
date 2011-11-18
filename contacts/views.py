import logging

from contacts.forms import ContactForm

from pymongo.objectid import ObjectId

from pyramid.response import Response
from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound

from wtforms import TextField, validators

logger = logging.getLogger('contacts')

@view_config(route_name='home',renderer='home.jinja2')
def home(request):
    return {'project':'Contacts'}


@view_config(name='list-contacts',renderer='list-contacts.jinja2')
def list_contacts(request):
    contacts = request.db['contact'].find()
    return {'contacts':contacts}

@view_config(route_name='view-contact',renderer='view-contact.jinja2')
def view_contact(request):
    _id = request.matchdict['id']
    contact = request.db.contact.find_one(dict(_id=ObjectId(_id)))
    contact.pop('_id')
    return {'contact':contact}

@view_config(name='get-file')
def get_file(request):
    _id = request.GET['id']
    fs = request.fs
    image = fs.get(ObjectId(_id)).read()
    return Response(body=image,content_type='image/png')

@view_config(name='new-contact',renderer='new-contact.jinja2')
def new_contact(request):   
    form = ContactForm(request.POST)
    if request.method == 'POST':

        class F(ContactForm):
            pass
        for name in request.POST.items():
            if name[0] not in form._fields.keys() and name[0] != 'submit':
                setattr(F, name[0], TextField(name[0],[validators.Required()]))
                
        form = F(request.POST)
        if form.validate():
            d = dict(request.POST)
            fs = request.fs
            photo = request.POST['photo'].file
            filename = request.POST['photo'].filename
            b = fs.put(photo.read(), filename=filename)
            d['photo'] = b
            d.pop('submit')
            request.db.contact.insert(d)
            return HTTPFound(location=request.relative_url('list-contacts'))
    return {'form':form}      
        
