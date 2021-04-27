from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.exceptions import ValidationError
from django.core import serializers

from .models import Person

from datetime import date

def index(request) :
    if not request.user.is_authenticated :
        return redirect('usuarios/login')

    data = {
        'coaches': Person.objects.filter(deleted=0)
    }
    
    return render(request, 'views/crud.html', data)

def view(request, target=0) :
    if target :
        person = Person.objects.get(id=target)

        if person :
            return HttpResponse(serializers.serialize('json', [person]))

    return HttpResponse("[{'error':1,message:'Registro no encontrado'}]")

def create(request) :
        try:
            newPerson = Person(
                first_name=request.POST.get('first_name'), 
                last_name=request.POST.get('last_name'),
                email=request.POST.get('email'),
                phone=request.POST.get('phone'),
                location=request.POST.get('location'),
                role=request.POST.get('role'),
                created_at=str(date.today())
            )
            newPerson.save()

        except ValidationError as e :
            print(e)

        return redirect('/')

def update(request, target=0) :
    try:
        if target :
            person = Person.objects.get(id=target)

            if person :
                person.first_name = request.POST.get('first_name')
                person.last_name = request.POST.get('last_name')
                person.email = request.POST.get('email')
                person.phone = request.POST.get('phone')
                person.location = request.POST.get('location')
                person.role = request.POST.get('role')
                person.updated_at=str(date.today())
                person.save()
    
    except ValidationError as e :
            print(e)

    return redirect('/')

def delete(request, target=0) :
    try:
        if target :
            person = Person.objects.get(id=target)

            if person :
                person.deleted=1
                person.updated_at=str(date.today())
                person.save()
    
    except ValidationError as e :
            print(e)
    
    return redirect('/')