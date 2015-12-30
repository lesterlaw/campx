from django.db import models
from django.utils import timezone
from django.core.validators import RegexValidator
# Create your models here.
class PersonalInfo(models.Model):
	name = models.CharField(max_length=100)
	age = models.CharField(max_length=2, validators=[RegexValidator(r'^\d{1,10}$')])
	NRIC = models.CharField(max_length=10, unique=True, error_messages={'unique':"This NRIC has already been registerted for the camp!"})
	organisation = models.CharField(max_length=100)
	registered_date = models.DateTimeField(default=timezone.now)

	def publish(self):
		published_date = timezone.now()
		published_date.save()

	def __unicode__(self):
		return self.name

	class Meta:
		app_label = 'campR'