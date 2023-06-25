from django.db import models

# Create your models here.
class Register(models.Model):
    UserName = models.CharField(max_length= 30)
    DOB = models.DateTimeField(default=1/1/2000)
    CourseName = models.CharField(max_length=30)
    Location = models.CharField(max_length=30)
    Password = models.CharField(max_length=10)

    class Meta:
        db_table="Register"