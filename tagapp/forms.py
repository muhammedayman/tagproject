from tagapp.models import TagModel
from django import forms

class SnippetForm(forms.ModelForm):
	class Meta:
		model=TagModel
		fields=['title']