from . import models
from django.forms import ModelForm


class PersonForm(ModelForm):
    class Meta:
        model = models.Person
        fields = ['name', 'email_id', 'contact', 'company',
                 'designation', 'description']





