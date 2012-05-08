from django.db import models
from django import forms
from datetime import date
# Create your models here.

class Delegates(models.Model):
    username = models.CharField(max_length=40)
    password = models.CharField(max_length=30)
    fname = models.CharField(max_length = 30)
    sname = models.CharField(max_length = 30)
    email = models.EmailField()
    dob = models.DateField()
    class Meta:
        verbose_name_plural = "Delegates"
        
    def __unicode__(self):
        return self.fname.capitalize()+" "+self.sname.capitalize()
  

def validate_username(value):
    if Delegates.objects.filter(username=value).exists():
        raise forms.ValidationError(u'Username Already Taken')


class RegistrationForm(forms.Form):
    username = forms.CharField(max_length=40,
                               validators=[validate_username],
                               widget=forms.TextInput(attrs = {"autocomplete ": "off"}))
    
    password = forms.CharField(widget=forms.PasswordInput())
    
    confirm_password = forms.CharField(widget=forms.PasswordInput())
    fname = forms.CharField(max_length = 30)
    sname = forms.CharField(max_length = 30)
    dob = forms.DateField(initial = date.today)
    email = forms.EmailField()

    def clean(self):
        cleaned_data = super(forms.Form,self).clean()
        # Match Passwords
        if 'password' in cleaned_data and 'confirm_password' in cleaned_data:
            if cleaned_data.get('password') != cleaned_data.get('confirm_password'):
                self._errors['password'] = [u'Passwords must match.']
                self._errors['confirm_password'] = [u'Passwords must match.']
        return cleaned_data
            
