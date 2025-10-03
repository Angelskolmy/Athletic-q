from django.contrib.auth.models import AbstractUser
from django.db import models

class User_Empleados(AbstractUser):
    Eps= models.CharField(max_length=50, null=True)  
    Sexo_choice=[
        ('Masculino','Masculino'),
        ('Femenino','Femenino')
    ] 
    Sexo= models.CharField(
        choices=Sexo_choice,
        default='', 
        max_length=20, 
        null=True
    ) 
    Cedula= models.IntegerField(unique=True, null=True) 

    def __str__(self): 
        return f"EPS{self.Eps} - Sexo{self.Sexo} - Cedulo{self.Cedula}"