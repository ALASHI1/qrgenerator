from django import forms

class Geoapiform(forms.Form):
    def __init__(self, address):
        self.address = address