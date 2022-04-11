from django.db import models

# Create your models here.
# here we have Position and Employee model. for any model there will be a primary key which will be 
# automatically created by Django ORM (Object Relational Mapping)
class Position(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):   #str function in a django model returns a string that is exactly rendered as the display name of instances for that model.
        return self.title

class Employee(models.Model):  #inherited models class with Model namespace
    emp_code = models.CharField(max_length=20)  
    fullname = models.CharField(max_length=100)  
    emp_email = models.EmailField()  
    mobile = models.CharField(max_length=15) 
    position = models.ForeignKey(Position, on_delete=models.CASCADE) 




