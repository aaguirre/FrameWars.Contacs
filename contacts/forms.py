from wtforms import Form, TextField, validators,FileField
import cgi

class FileRequired(validators.Required):
    """
    Required validator for file upload fields.
    """
    def __call__(self, form, field):
        if not isinstance(field.data, cgi.FieldStorage):
            if self.message is None:
                self.message = field.gettext(u'This field is required.')

            field.errors[:] = []
            raise validators.StopValidation(self.message)

class ContactForm(Form):
    firstname = TextField(u'Firstname',[validators.Required()])
    lastname = TextField(u'Lastname',[validators.Required()])
    photo = FileField(u'Photo',[FileRequired()])
    email = TextField(u'Email',[validators.Email()])
    
