from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

def login(request):
	if request.method == 'POST':
		user = auth.authenticate(username=request.POST['username'],password=request.POST['password'])
		#Validation of login/return to home page
		if user is not None:
			auth.login(request, user)
			return redirect('home')
		#if login fails, return to login with error
		else:
			return render(request, 'accounts/login.html', {'error':'Those credentials are not valid.'})
	else:
		return render(request, 'accounts/login.html')

def signup(request):
	if request.method == 'POST':
		# User is signing up
		if request.POST['password1'] == request.POST['password2']:
			try:
				user = User.objects.get(username=request.POST['username'])
				return render(request, 'accounts/signup.html', {'error':'That user exists already.'})
			except User.DoesNotExist:
				user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
				auth.login(request, user)
				return redirect('home')
		else:return render(request, 'accounts/signup.html', {'error':'Passwords must match.'})
	else:
		#show the signup page
		return render(request, 'accounts/signup.html')

def logout(request):
	if request.method == 'POST':
		auth.logout(request)
		return redirect('home')
