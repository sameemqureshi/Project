from django.db import models




class Company(models.Model):
    company_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    address=models.TextField()
    Domain=models.CharField(max_length=100,choices=(('IT','IT'),
                                                    ('Production','Production'),
                                                    ('Marketing','Marketing')))
    is_active=models.BooleanField()
    def  __str__(self):
        return self.name +"  "+self.address
    
    
    
class Entity(models.Model):
    entity_id=models.AutoField(primary_key=True)
    entity_name=models.CharField(max_length=50)
    is_active=models.BooleanField(default=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    def __str__(self):
        return self.entity_id+ self.entity_name


# Create your models here.
