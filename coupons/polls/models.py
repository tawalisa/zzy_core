from django.db import models

# Create your models here.
class User(models.Model):
	loginname = models.CharField(max_length=200)
	password = models.CharField(max_length=64)
	email = models.CharField(max_length=200)
	phonenum = models.CharField(max_length=32)
	def __unicode__(self):
		return self.loginname
