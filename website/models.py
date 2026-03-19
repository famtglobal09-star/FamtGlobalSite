from django.db import models

class CallbackRequest(models.Model):

    SERVICE_CHOICES = [
        ('Finance Consulting','Finance Consulting'),
        ('Accounting','Accounting'),
        ('Taxation','Taxation'),
        ('General Inquiry','General Inquiry'),
    ]

    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    service = models.CharField(max_length=100, choices=SERVICE_CHOICES)
    message = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name