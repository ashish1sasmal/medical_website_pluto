from django.db import models
from django.contrib.auth.models import User
# Create your models here.

GENDER_CHOICES=(('M','Male'),('F','Female'))

class Profile(models.Model):
	user=models.OneToOneField(User,on_delete=models.CASCADE)
	
	phone=models.CharField(max_length=10)
	gender=models.CharField(choices=GENDER_CHOICES,max_length=128)

	def __str__(self):
		return f'{self.user.username} Profile'