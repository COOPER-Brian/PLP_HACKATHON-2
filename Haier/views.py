from django.shortcuts import render
import requests

# Create your views here.
def base(request):
    r1= requests.get('https://dog.ceo/api/breeds/image/random')
    breed = r1.json()
    dog = breed['message']
    return render(request, 'base.html', {'dog' : dog})

def randomfacts(request):
    r2= requests.get('https://uselessfacts.jsph.pl/random.json?language=en')
    random = r2.json()
    text = random['text']
    return render(request,'randomfacts.html', {'text':text})
