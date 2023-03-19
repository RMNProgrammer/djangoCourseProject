from django import forms

class NameForm(forms.Form):
    name = forms.CharField(max_length=80)
    email = forms.EmailField()
    subject = forms.CharField(max_length=80)
    message = forms.CharField(widget=forms.Textarea)