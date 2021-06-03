from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate
from django.http import HttpResponseRedirect,JsonResponse,HttpResponse
from django.contrib import messages




def login(request):
	if(request.method=='POST'):
		username=request.POST.get('email')
		password=request.POST.get('password')
		print(username,password)
		user=authenticate(request,username=username,password=password)
		if user is not None:
			auth.login(request,user)
			return redirect("nqueens/")
				
		else:
			messages.info(request,'Invalid Credentials..')
			return redirect("/")			
		
	else:
		return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')
def signup(request):

	if request.method=="POST":
		username=request.POST.get('email')
		name=request.POST.get('name')
		password=request.POST.get('password')

		if(User.objects.filter(username=username).exists()):
			messages.info(request,'Username already Taken')
			return HttpResponseRedirect("signup")
		else:
			user = User.objects.create_user(username=username, password=password,email=username, first_name =name)
			user.save()

			return HttpResponseRedirect('/')

	return render(request,'registration.html')