from django import forms
from .models import Entry

class AdForm(forms.ModelForm):
	
	class Meta:
		model = Entry
		fields = ('title', 'image', 'price', 'body', 'slug',)