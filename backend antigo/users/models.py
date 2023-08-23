from django.db import models
from dateutil.relativedelta import relativedelta
from django.utils import timezone
from django.contrib.auth.models import User

class Training_level(models.Model):
    level = models.CharField(max_length=20)

    def __str__(self):
        return self.level


class User(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)
    email = models.EmailField(blank=False, null=False)
    adress = models.CharField(max_length=200,blank=False, null=False)
    date_of_birth = models.DateField()
    profile_picture = models.ImageField(upload_to='users_pictures', blank=True, null=True)
    training_level = models.ForeignKey(Training_level, on_delete=models.DO_NOTHING, blank=True)


    def __str__(self):
        return self.name


class Measurements(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='measurements')
    height = models.FloatField(blank=False, null=True)
    weight = models.FloatField(blank=False, null=True)
    arms = models.FloatField(blank=False, null=True) #braço
    chest = models.FloatField(blank=False, null=True) #peito
    waist = models.FloatField(blank=False, null=True) #cintura
    hips = models.FloatField(blank=False, null=True) #quadril
    legs = models.FloatField(blank=False, null=True) #perna
    body_pictures = models.ImageField(upload_to='users_pictures', blank=True)
    date_register = models.DateField(default=timezone.now)
    
    
    def __str__(self):
        return self.user.name
    
    def imc(self):
        height_m = self.height / 100
        imc = self.weight / (height_m ** 2)
        return imc
