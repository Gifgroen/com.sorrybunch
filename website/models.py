from django.db import models
from django.contrib.auth.models import User

from django.db.models.signals import pre_save

# Create your models here.
class Article(models.Model):
	title = models.CharField(max_length = 32)
	body = models.TextField()
	author = models.ForeignKey(User)
	placed = models.DateTimeField(auto_now = True, auto_now_add = True)
	
class Gig(models.Model):
	name = models.CharField(max_length = 32)
	place = models.CharField(max_length = 256)
	link = models.URLField()
	date = models.DateField()

class Video(models.Model):
	video_id = models.CharField(max_length = 64, unique = True)
	width = models.IntegerField()
	height = models.IntegerField()
	active = models.BooleanField(default = True, editable = False)

def make_video_active(sender, **kwargs):
	pre_save.disconnect(make_video_active, sender = Video)
	old_videos = Video.objects.filter(active = True)
	for v in old_videos:
		v.active = False
		v.save()
	pre_save.connect(make_video_active, sender = Video)
	video = kwargs['instance']
	video.active = True

pre_save.connect(make_video_active, sender = Video)