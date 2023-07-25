from django.db import models

# Create your models here.
class About(models.Model):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    date = models.DateField()

    def __str__(self):
        return self.name

class Extra(models.Model):
    fname = models.CharField(max_length=20)
    lname = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = "extra"
    
    def __str__(self):
        return self.fname
    