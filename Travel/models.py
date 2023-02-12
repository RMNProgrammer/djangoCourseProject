from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=90)
    email = models.EmailField()
    subject = models.CharField(max_length=40)
    message = models.TextField()
    created_data = models.DateTimeField(auto_now_add=True)
    update_data = models.DateTimeField(auto_now=True)