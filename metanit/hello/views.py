from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponseNotFound
from .models import Person, Fly


# получение данных из бд
def index(request):
    people = Person.objects.all()
    return render(request, "index.html", {"people": people})


# сохранение данных в бд
def create(request):
    if request.method == "POST":
        person = Person()
        person.name = request.POST.get("name")
        person.age = request.POST.get("age")
        person.save()
        fly = Fly()
        fly.paraplan = request.POST.get("paraplan")
        fly.paraplan = request.POST.get("podveska")
        fly.save()
    return HttpResponseRedirect("/")


# изменение данных в бд
def edit(request, id):
    try:
        person = Person.objects.get(id=id)
        fly = Fly.object.get(id=id)
        if request.method == "POST":
            person.name = request.POST.get("name")
            person.age = request.POST.get("age")
            fly.paraplan = request.POST.get("paraplan")
            fly.paraplan = request.POST.get("podveska")
            person.save()
            fly.save()
            return HttpResponseRedirect("/")
        else:
            return render(request, "edit.html", {"person": person}, {"fly": fly})
    except Person.DoesNotExist:
        return HttpResponseNotFound("<h2>Person not found</h2>")


# удаление данных из бд
def delete(request, id):
    try:
        person = Person.objects.get(id=id)
        fly = Fly.object.get(id=id)
        person.delete()
        fly.delete()
        return HttpResponseRedirect("/")
    except Person.DoesNotExist:
        return HttpResponseNotFound("<h2>Person not found</h2>")