from django.db import models

# Create your models here.
class TimeDestination(models.Model):
    name = models.CharField(max_length=50)
    type = models.ForeignKey('Type', on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.name}'
    
class Type(models.Model):
    type_choices=[
        ('Historical', 'Historical'),
        ('Futuristic', 'Futuristic'), 
        ('Mythical', 'Mythical',)
    ]  
    type = models.CharField(max_length=10, choices=type_choices, default='null')
    
    def __str__(self):
        return f'{self.type}'