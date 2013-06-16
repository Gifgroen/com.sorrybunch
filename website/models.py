from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Article(models.Model):
	title = models.CharField(max_length = 32)
	body = models.TextField()
	author = models.ForeignKey(User)
	placed = models.DateTimeField(auto_now = True, auto_now_add = True)
	
class Gig(models.Model):
	name = models.CharField(max_length = 32)
	place = models.CharField(max_length = 32)
	link = models.URLField()
	date = models.DateTimeField()