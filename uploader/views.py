import re
import string
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import *

# def upload_file(request):
#     if request.method == 'POST':
#         form = UploadForm(request.POST, request.FILES)
#         if form.is_valid():
#             handle_uploaded_file(request.FILES['file'])
#             return HttpResponseRedirect('/success/url/')
#     else:
#         form = UploadForm()
#     return render(request, '.html', {'form': form})

def upload_file(request):
    if request.method == 'POST':
    	form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
        	frequency = {}
        	handle_uploaded_file=request.FILES['file'].read()
			match_pattern = re.findall(r'\b[a-z]{3,15}\b', handle_uploaded_file)
			for word in match_pattern:
    			count = frequency.get(word,0)
    			frequency[word] = count + 1
				frequency_list = frequency.keys()[:5]
        	return render(request, 'home.html', {'form': form,
        											'frequeny_list':frequeny_list})
    else:
        form = UploadForm()
    return render(request, 'home.html', {'form': form})

# def handle_uploaded_file(file, filename):
#     if not MEDIA_ROOT('upload/'):
#        	MEDIA_ROOT.mkdir('upload/')
#     with open('upload/' + filename, 'wb+') as destination:
#         for chunk in file.chunks():
#             destination.write(chunk)
