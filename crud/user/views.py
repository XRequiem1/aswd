from django.shortcuts import render, redirect
from .models import Person
from django.db.models import Avg, Sum, Max, Min
from .forms import AddForm
def index(request):
    makeMen()
    people = Person.objects.all()
    print(people)
    return render(request, 'user/index.html', context={'people': people})

def create(request):
    if request.method == 'POST':
        form = AddForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data('name')
            surname = form.cleaned_data('name')
            age = form.cleaned_data('name')
            gender = form.cleaned_data('name')
            birthDay = form.cleaned_data('name')
            men, _ = form.cleaned_data('name')
            men, _ = Person.objects.get_or_create(name=name, surname=surname, age=age,
                                                  gender=gender, birthDay=birthDay)
            return redirect('home')
        else:
            form = AddForm()
            return render(request, 'user/create.html', context={'form': form})
    else:
        form = AddForm()
        return render(request, 'user/create.html', context={'form': form})

def update(request, id):
    try:
        men = Person.objects.get(id=id)
        if request.method == 'POST':
            men.name = request.POST.get('name')
            men.surname = request.POST.get('name')
            men.age = request.POST.get('name')
            men.gender = request.POST.get('name')
            men.birthDay = request.POST.get('name')
            men.save()
            return redirect('home')
        else:
            return render(request, 'user/update.html', context={'men': men})

    except:
        return redirect('create')

def delete(request, id):
    try:
        men = Person.objects.get(id=id)
        men.delete()
        return redirect('home')
    except:
        return redirect('create')


def makeMen():
    p = Person.objects.create(name='Tom1', surname='Ouihdg', age=18, gender=True, birthDay='2011-12-12')
    p = Person.objects.create(name='Tom2', surname='Ouihdg', age=19, gender=True, birthDay='2011-12-12')
    p = Person.objects.create(name='Tom3', surname='Ouihdg', age=20, gender=True, birthDay='2011-12-12')
    p = Person.objects.create(name='Tom4', surname='Ouihdg', age=21, gender=True, birthDay='2011-12-12')
    p = Person.objects.create(name='Tom5', surname='Ouihdg', age=22, gender=True, birthDay='2011-12-12')
