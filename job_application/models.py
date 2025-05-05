from django.db import models

# Create your models here.
class Form(models.Model):
    first_name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=80)
    email = models.EmailField(max_length=100)
    date = models.DateField()
    employment_status = models.CharField(max_length=80)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
