from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout as django_logout
from .forms import UserForm, UploadFileForm
from django.contrib.auth.decorators import login_required 
from django import forms
from .service import *
import os
import subprocess



def index(request):
	if request.user.is_authenticated:
		if request.method == 'POST':
			user = request.user
			if len(request.FILES) != 0:
				handle_upload_files(get_verified_string(request.user), request.FILES['file'])
				file_name = request.POST['verify_file_name']
				signature_file_name = get_verified_string(request.user) + str(request.FILES['file']).replace(' ', '')
				result = subprocess.run(['./verify.sh', get_plain_string(user) + file_name, get_public_key_location(user), signature_file_name], stdout=subprocess.PIPE)
				if 'OK' in str(result):
					return display_home_page(request, 'OK')
				else:
					return display_home_page(request, 'NOT OK')	
		else:
			return display_home_page(request)
	else:
		return HttpResponseRedirect('/login')

@login_required
def display_home_page(request, verify_message=''):
		files = os.listdir('users/' + str(request.user.username) + '/plain/')
		return render(request, 'app/home.html', {'user': request.user, 'form': UploadFileForm(), 'files': files, 'verify_message': verify_message})


@login_required
def logout(request):
	django_logout(request)
	return HttpResponseRedirect('/')

@login_required
def upload(request):
	if request.method == 'POST':
		form = UploadFileForm(request.POST, request.FILES)
		if form.is_valid():
			handle_upload_files(get_plain_string(request.user), request.FILES['file'])
	return HttpResponseRedirect('/')

@login_required
def sign(request):
	if request.method == 'POST':
		user = request.user
		file_name = request.POST['sign_file_name']
		file_path = get_plain_string(user) + file_name
		output_file_path = get_signed_string(user) + file_name
		result = subprocess.run(['./sign.sh', file_path, get_private_key_location(user), output_file_path], stdout=subprocess.PIPE)
		return_file_path = output_file_path + '.signature'
		with open(return_file_path) as fh:	
			response = HttpResponse(fh.read(), content_type="multipart/mixed")
			response['Content-Disposition'] = 'inline; filename=' + file_name + '.signature'
			return response
	else:
		return HttpResponseRedirect('/')

def register(request):
	if request.method == 'POST':
		form = UserForm(request.POST)
		if form.is_valid():
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			confirm_password = form.cleaned_data['confirm_password']
			email = form.cleaned_data['email']
			new_user = User.objects.create_user(username, email, password)
			new_user.save()
			if not os.path.isdir(get_plain_string(new_user)):
				os.makedirs(get_plain_string(new_user))
			if not os.path.isdir(get_signed_string(new_user)):
				os.makedirs(get_signed_string(new_user))
			if not os.path.isdir(get_verified_string(new_user)):
				os.makedirs(get_verified_string(new_user))
			subprocess.run(['./genkeys.sh', get_user_string(new_user) + 'private.pem', get_user_string(new_user) + 'public.pem'])
			return HttpResponseRedirect('/')
	else:
		form = UserForm()

	return render(request, 'app/register.html', {'form': form})
