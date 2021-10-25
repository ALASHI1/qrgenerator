from .models import *
from django import forms

class Qrform(forms.ModelForm):
    class Meta:
        model = Qrcode
        fields = ['name']

class Qrfileform(forms.ModelForm):
    class Meta:
        model = Qrfilecode
        fields = ['name','uploads']

class Qraudioform(forms.ModelForm):
    class Meta:
        model = Qraudiocode
        fields = ['name','uploads']

class Qrpdfform(forms.ModelForm):
    class Meta:
        model = Qrpdfcode
        fields = ['name','uploads']

class Geoform(forms.Form):
	address = forms.CharField(label='Your address', max_length=500)

class ContactCard(forms.Form):
	name = forms.CharField(label='Your name', max_length=500)
	email = forms.CharField(label='Your email', max_length=500)
	phone = forms.CharField(label='Your phone', max_length=500)
	url = forms.CharField(label='Your website', max_length=500)

