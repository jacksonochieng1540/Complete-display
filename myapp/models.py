from django.db import models

class Visitor(models.Model):
    ip_address = models.GenericIPAddressField(unique=True)
    visit_count = models.IntegerField(default=0)
    first_visit = models.DateTimeField(auto_now_add=True)
    last_visit = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.ip_address} - {self.visit_count} visits"