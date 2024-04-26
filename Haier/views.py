from django.shortcuts import render
import requests

# Create your views here.
def base(request):
    r1= requests.get('https://dog.ceo/api/breeds/image/random')
    breed = r1.json()
    dog = breed['message']
    return render(request, 'base.html', {'dog' : dog})

def randomfacts(request):
    return render(request,'randomfacts.html')
