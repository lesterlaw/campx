from django import forms
from .models import WishCamp, PersonalInfo
from django.forms.extras.widgets import SelectDateWidget
from django.core.exceptions import ValidationError

class WishForm(forms.ModelForm):
	estimated_date = forms.CharField(widget=SelectDateWidget)
	class Meta:
		model = WishCamp
		exclude = ('published_date', 'user','number_of_people')

class WishJoinForm(forms.ModelForm):
	class Meta:
		model = PersonalInfo
		exclude = ('camp',)

	def clean(self):
		cleaned_data = super(WishJoinForm, self).clean()
		NRIC = cleaned_data.get('NRIC')
		camp_id = cleaned_data.get('camp_id')

		if NRIC and camp_id:
			try:
				Pcq.objects.get(
					NRIC=NRIC,
					camp_id=camp_id,
				)
			except Pcq.DoesNotExist:
				# Yay
				pass
			else:
				raise forms.ValidationError(("Error message goes here"))