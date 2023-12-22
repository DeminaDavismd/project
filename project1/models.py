from django.db import models

# Create your models here.
class Departmentss(models.Model):

    dep_name = models.CharField(max_length=100)
    dep_description = models.TextField()
class Doctor(models.Model):
    doc_name = models.CharField(max_length=100)
    doc_specilization=models.CharField(max_length=100)
    doc_pic = models.ImageField(upload_to='Doctor')

    def __str__(self):
        return self.doc_name + '-('+ self.doc_specilization +')'
class appointmet(models.Model):
    name=models.CharField(max_length=100)
    phone=models.CharField(max_length=50)
    email=models.CharField(max_length=40)
    doc_name=models.ForeignKey(Doctor,on_delete=models.CASCADE)
    booked_date=models.DateField()
    
    def __str__(self) :
        return  self.name
class contact(models.Model):
      name=models.CharField(max_length=100)
      phone=models.CharField(max_length=50)
      Type_query=models.CharField(max_length=40)
      
       
def __str__(self) :
        return  self.name