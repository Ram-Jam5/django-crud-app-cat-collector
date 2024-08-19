from django.shortcuts import render, redirect 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView

from .models import Cat, Toy
from .forms import FeedingForm
# Create your views here.

# views.py
def home(request):
    # Send a simple HTML response
    return render(request, 'home.html')
# Render the about.html page.
def about(request):
    return render(request, 'about.html')

    # Render the cats/index.html template with the cats data
def cat_index(request):
    cats = Cat.objects.all()
    return render(request, 'cats/index.html', {'cats': cats})

def cat_detail(request, cat_id):
    cat = Cat.objects.get(id=cat_id)
    toys_cat_doesnt_have = Toy.objects.exclude(id__in = cat.toys.all().values_list('id'))  # Fetch all toys
    feeding_form = FeedingForm()
    return render(request, 'cats/detail.html', {
        'cat': cat,
        'feeding_form': feeding_form,
        'toys': toys_cat_doesnt_have  # Pass toys to the template
    })



def add_feeding(request, cat_id):
    # create a ModelForm instance using the data in request.POST
    form = FeedingForm(request.POST)
    # validate the form
    if form.is_valid():
        # don't save the form to the db until it
        # has the cat_id assigned
        new_feeding = form.save(commit=False)
        new_feeding.cat_id = cat_id
        new_feeding.save()
    return redirect('cat-detail', cat_id=cat_id)


class CatCreate(CreateView):
    model = Cat
    fields = ['name', 'breed', 'description', 'age']

  
class CatUpdate(UpdateView):
    model = Cat
    fields = {'breed','description', 'age'}

class CatDelete(DeleteView):
    model = Cat
    success_url = '/cats/'

class ToyCreate(CreateView):
    model = Toy
    fields = '__all__'

class ToyList(ListView):
    model = Toy

class ToyDetail(DetailView):
    model = Toy

class ToyUpdate(UpdateView):
    model = Toy
    fields = ['name', 'color']

class ToyDelete(DeleteView):
    model = Toy
    success_url = '/toys/'

def associate_toy(request, cat_id, toy_id):
    # Note that you can pass a toy's id instead of the whole object
    Cat.objects.get(id=cat_id).toys.add(toy_id)
    return redirect('cat-detail', cat_id=cat_id)

def remove_toy(request, cat_id, toy_id):
    # Look up the cat
    cat = Cat.objects.get(id=cat_id)
    # Look up the toy 
    cat.toys.remove(toy_id)
    # toy = Toys.objects.get()
    # Remove the toy from the cat
    return redirect('cat-detail', cat_id=cat.id)
