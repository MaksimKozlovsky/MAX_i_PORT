from django import forms


class City_Form(forms.Form):
    name = forms.CharField(max_length=50)
