from django.shortcuts import render
from main.models import Skills, Message
from django.http import HttpResponseRedirect
# Create your views here.

def main(request):
    skills= Skills.objects.all()
    return render(request, 'portfolio.html')

def message(request):
    if request.method=='POST':
        message=Message()
        message.name=request.POST.get('name')
        message.email=request.POST.get('email')
        message.text=request.POST.get('message')
        message.save()
        return HttpResponseRedirect('/')