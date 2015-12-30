from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
# Create your models here.

class WishCamp(models.Model):
	user = models.ForeignKey(User)
	title = models.CharField(max_length=255)
	hobby_involved = models.CharField(max_length=255)
	description = models.TextField()
	number_of_people = models.IntegerField(default=0)
	published_date = models.DateTimeField(default=timezone.now)
	estimated_date = models.DateField()

	def publish(self):
		published_date = timezone.now()
		published_date.save()

	def __unicode__(self):
		return self.title
	class Meta:
		app_label = 'wishcamps'

class PersonalInfo(models.Model):
	name = models.CharField(max_length=100)
	camp = models.ForeignKey(WishCamp)
	Age = models.CharField(max_length=2, validators=[RegexValidator(r'^\d{1,10}$')])
	NRIC = models.CharField(max_length=10)
	Organisation = models.CharField(max_length=100)

	class Meta:
		unique_together = (("NRIC", "camp"),)  
		app_label = 'wishcamps'