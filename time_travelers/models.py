from django.db import models

# Create your models here.
class TimeTraveler(models.Model):
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    email = models.EmailField()
    skill = models.ForeignKey('Skill', on_delete=models.CASCADE, name='skill')
    
    def __str__(self):
        return f'{self.name} {self.last_name} : {self.skill}'
    
class Skill(models.Model):
    skill_choices = [
        ('Beginner', 'Beginner'),
        ('Intermediate','Intermediate'),
        ('Expert', 'Expert'),
    ]  
    skill = models.CharField(max_length=50, choices=skill_choices, default='null')
    
    def __str__(self):
        return f'{self.skill}'