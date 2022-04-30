from django import forms


class SampleForm(forms.Form):

	user_input = forms.ImageField()
	secret_data_path = forms.FileField()
	