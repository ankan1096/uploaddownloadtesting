from django import forms
from .models import StegoObjctStore
from django.forms import ModelForm

class SampleForm(forms.Form):

	user_input = forms.ImageField()
	secret_data_path = forms.FileField()
	stego_image = forms.FileField()
	
class StegoForm(ModelForm):
	class Meta:
		model = StegoObjctStore
		fields = ('name', 'image')