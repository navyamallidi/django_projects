from django.shortcuts import render
from .models import Contact
from django.http import HttpResponse
# Create your views here.

def index(request):
	if request.method == 'POST':
		contact=Contact()
		name=request.POST.get('name')
		email=request.POST.get('email')
		problem=request.POST.get('problem')
		suggestion=request.POST.get('suggestion')
		contact.name=name
		contact.email=email
		contact.problem=problem
		contact.suggestion=suggestion
		contact.save()
		return HttpResponse("<h5> THANKS FOR YOUR SUGGESTION<h5>")




	return render (request,"index.html")