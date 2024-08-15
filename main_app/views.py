from django.shortcuts import render 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Cat
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
    return render(request, 'cats/detail.html', {'cat': cat})

class CatCreate(CreateView):
    model = Cat
    fields = '__all__'
  
class CatUpdate(UpdateView):
    model = Cat
    fields = {'breed','description', 'age'}

class CatDelete(DeleteView):
    model = Cat
    success_url = '/cats/'