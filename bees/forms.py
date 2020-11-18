from django import forms
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Checkbox

from django.core import validators
from django.core.exceptions import ValidationError

class Contactform(forms.Form):
    nome = forms.CharField(label="Nome", widget=forms.TextInput(attrs={"class" : "form-control"}), 
        validators=[validators.MinLengthValidator(2, "il nome deve avere almeno 2 caratteri"), validators.MaxLengthValidator(40, "il nome non può superare i 40 caratteri")])
    cognome = forms.CharField(label="Cognome", widget=forms.TextInput(attrs={"class" : "form-control"}),
         validators=[validators.MinLengthValidator(2, "il cognome deve avere almeno 2 caratteri"), validators.MaxLengthValidator(40, "il cognome non può superare i 40 caratteri")])
    email = forms.EmailField(label="E-Mail", widget=forms.TextInput(attrs={"class" : "form-control"}),
        validators=[validators.validate_email])
    messaggio = forms.CharField(label="Messaggio", widget=forms.Textarea(attrs={"rows" : 6, "class" : "form-control"}),
        validators=[validators.MaxLengthValidator(300, "il messaggio non può superare i 300 caratteri")])
    captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox)

    def clean_nome(self):
        dati = self.cleaned_data["nome"]
        if dati == "":
            raise ValidationError("Campo obbligatorio")
        return dati

    def clean_cognome(self):
        dati = self.cleaned_data["cognome"]
        if dati == "":
            raise ValidationError("Campo obbligatorio")
        return dati

    def clean_email(self):
        dati = self.cleaned_data["email"]
        if dati == "":
            raise ValidationError("Campo obbligatorio")
        return dati

    def clean_messaggio(self):
        dati = self.cleaned_data["messaggio"]
        if dati == "":
            raise ValidationError("Campo obbligatorio")
        return dati

#https://docs.djangoproject.com/en/3.1/ref/forms/validation/#:~:text=The%20clean()%20method%20on,and%20that%20error%20is%20raised.

