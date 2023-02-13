from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=90)
    email = models.EmailField()
    subject = models.CharField(max_length=40)
    message = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_date']
        verbose_name = ' message'

    def __str__(self):
        return self.subject