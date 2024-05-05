from django.db import models

class Tracking_Helper(models.Model):
    cerated_at=models.DateTimeField(auto_now_add=True)
    last_update=models.DateTimeField(auto_now=True)
    
class Meta:
    #name of table in database
    db_table = ''
    #django can be add or delete
    managed = True
    #humane name readable 
    #verbose_name = 'ModelName'
    #humane name readable to plural
   # verbose_name_plural = 'ModelNames'
        
class Location_Helper(models.Model):  
    address_line_1=models.TextField(max_length=150)
    address_line_2=models.TextField(max_length=150)
    country=models.TextField(max_length=150)
    state=models.TextField(max_length=150)
    Mobile_No=models.IntegerField(max_length=50)
    city=models.CharField(max_length=20)
    zip_code=models.IntegerField(max_length=10) 