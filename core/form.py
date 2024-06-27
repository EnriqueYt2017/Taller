from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from django_recaptcha.fields import ReCaptchaField

from .models import *

class VehiculoForm(ModelForm):
    captcha = ReCaptchaField()
    class Meta:
        model = Vehiculo
        fields = '__all__'

class MantenimientoForm(ModelForm):
    captcha = ReCaptchaField()
    class Meta:
        model = Mantenimiento
        fields = '__all__'

class ContactForm(forms.Form):
    captcha = ReCaptchaField()
    name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    asunto = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea)
