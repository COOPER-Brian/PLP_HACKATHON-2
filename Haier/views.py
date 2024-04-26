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


def students(request):
    r3=requests.get('https://freetestapi.com/api/v1/students')
    stud = r3.json()
    name = stud[0]['name']
    age = stud[0]['age']
    gender = stud[0]['gender']
    address = stud[0]['address']
    gpa  =  stud[0]['gpa']
    email = stud[0]['email']
    phone = stud[0]['phone']
    
    return render(request, 'students.html', {'name': name, 'age':age, 'gender':gender, 'address':address, 'gpa':gpa,'email':email, 'phone': phone})

