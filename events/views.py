from django.shortcuts import render
from .forms import SampleForm
import sys
import os
from PIL import Image as im
from numpy import array
from numpy import vectorize as vec
from numpy import binary_repr as binary
from numpy import dstack as ds


def home(request):
	sampleform = SampleForm
	if request.method == "POST":
		user_input = request.FILES['user_input']
		secret_data_path = request.FILES['secret_data_path']
		image = im.open(user_input)
		arr = array(image)
		print(arr)
		#secret_data = open(secret_data_path,'r+')
		secret_content = secret_data_path.read()
		data = ""
		for x in secret_content:
			data = data + chr(x)
		print(data)
		sys.stdout.flush()
		return render(request, 'home.html', {'sampleform' : sampleform, 'data' : data})
	return render(request, 'home.html', {'sampleform' : sampleform})
