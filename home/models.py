from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.six import python_2_unicode_compatible

# Create your models here.
@python_2_unicode_compatible
class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	snake_score = models.IntegerField(default=0)
	pong_score = models.IntegerField(default=0)
	pacman_score = models.IntegerField(default=0)

	def __str__(self):
		return "username: " + str(self.user.username) + " | snake score: " + str(self.snake_score) + " | pong score: " + str(self.pong_score) + " | pacman score: " + str(self.pacman_score)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
	if created:
		Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
	instance.profile.save()
