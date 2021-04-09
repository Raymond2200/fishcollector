from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Fish
from .forms import FeedingForm

# Define the home view
def home(request):
  return render(request,'home.html')


def about(request):
    return render(request, 'about.html')

def fishlist(request):
  fish = Fish.objects.all()
  return render(request, 'fish/index.html', {'fish':fish})

def fish_detail(request, fish_id):
  fish = Fish.objects.get(id=fish_id)
  feeding_form = FeedingForm()
  return render(request, 'fish/detail.html', {'fish': fish, "feeding_form": feeding_form})

def fish_c(request):
  return render(request, 'fish/addfish.html')

def create_fish(request):
  Fish.objects.create(
    name= request.POST['name'],
    specie= request.POST['species'],
    description= request.POST['description'],
    age= request.POST['age']
  )
  return redirect('/fishlist')

def delete_fish(request, fish_id):
  f = Fish.objects.get(id=fish_id)
  f.delete()
  return redirect("/fishlist")

def edit_view(request, fish_id):
  fish =Fish.objects.get(id=fish_id)
  feeding_form = FeedingForm()
  return render(request, "fish/edit.html", {'fish': fish})

def edit_fish(request, fish_id):
  this_fish = Fish.objects.get(id=fish_id)
  this_fish.name = request.POST['name']
  this_fish.specie = request.POST['specie']
  this_fish.description = request.POST['description']
  this_fish.age = request.POST['age']
  this_fish.save()
  return redirect('/fishlist')

def meals(request, fish_id):
  fish = Fish.objects.get(id=fish_id)
  return render('fish/meal.html', {"fish":fish})

def add_feeding(request, fish_id):
  form = FeedingForm(request.POST)
  if form.is_valid():
    new_feeding = form.save(commit=False)
    new_feeding.fish_id = fish_id
    new_feeding.save()
  return redirect('detail', fish_id=fish_id)
