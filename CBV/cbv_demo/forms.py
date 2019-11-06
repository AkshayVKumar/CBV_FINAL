from django import forms

class Form_name(forms.Form):
    name=forms.CharField(max_length=10,label="Name : ")