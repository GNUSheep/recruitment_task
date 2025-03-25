from django import forms

class NameForm(forms.Form):
    pesel = forms.CharField(label="text_box", max_length=100)
