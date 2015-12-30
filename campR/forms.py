from django import forms
from .models import PersonalInfo

class JoinForm(forms.ModelForm):
	class Meta:
		model = PersonalInfo
		exclude = ('registered_date',)
