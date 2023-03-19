from django import forms
from Travel.models import Contact

class NameForm(forms.Form):
    name = forms.CharField(max_length=80)
    email = forms.EmailField()
    subject = forms.CharField(max_length=80)
    message = forms.CharField(widget=forms.Textarea)

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact 
        fields = '__all__'