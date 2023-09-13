from django.shortcuts import render,redirect
from .models import Person
from .forms import PersonForm
# Create your views here.

def main(request):
    form = PersonForm(request.Post or None)
    if request.Post and form.is_valid():
        form.save()
        return redirect("persons")
    ctx = {
        "form":form
    }
    return render(request,'index.html',ctx)




def person(request):
    persons = Person.objects.all()
    return render(request, 'table.html',{"persons":persons})
