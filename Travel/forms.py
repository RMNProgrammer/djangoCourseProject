from django import forms
from Travel.models import Newsletter
from captcha.fields import CaptchaField

class NameForm(forms.Form):
    name = forms.CharField(max_length=80)
    email = forms.EmailField()
    subject = forms.CharField(max_length=80)
    message = forms.CharField(widget=forms.Textarea)

class ContactForm(forms.Form):
    name = forms.CharField(max_length=80)
    email = forms.EmailField()
    subject = forms.CharField(max_length=80,required=False)
    message = forms.CharField(widget=forms.Textarea)
    captcha = CaptchaField()

class NewsletterForm(forms.ModelForm):
    class Meta:
        model = Newsletter
        fields = '__all__'