from typing import Any, Dict
from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from .models import Dog
from django.views.generic.edit import CreateView
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.urls import reverse

class Home(TemplateView):
    template_name = "home.html" 

class About(TemplateView):
    template_name = "about.html"

class DogList(TemplateView):
    template_name = "doglist.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["dogs"] = Dog.objects.all() # Here we are using the model to query the database for us.
        return context
    
class DogCreate(CreateView):
    model = Dog
    fields = ['breed', 'img', 'life_expectancy']
    template_name = "dog_create.html"
    success_url = "/dogs/"

class DogDetail(DetailView):
    model = Dog
    template_name = "dogs_detail.html"

class DogUpdate(UpdateView):
    model = Dog
    fields = ['breed', 'img', 'life_expectancy']
    template_name = "dog_update.html"
    success_url = "/dogs/"


class DogDelete(DeleteView):
    model = Dog
    template_name = "dog_delete.html"
    success_url = "/dogs/"

class MixCreate(View):

    def post(self, request, pk):
        breed1 = request.POST.get("breed1")
        breed2 = request.POST.get("breed2")
        dog = Dog.objects.get(pk=pk)
        Mix.objects.create(breed1=breed1, breed2=breed2,dog=dog)
        return redirect('dog_detail', pk=pk)
    
    

dog = [
    Dog('Rottweiler', 'https://encrypted-tbn0.gstatic.com/licensed-image?q=tbn:ANd9GcQFPkhWBCMG__t60W8L5ZlkHmgRkBiuM8zq-8-jsCD7d2WxR1meWMRTx8wgK0CvcNCygXy9irTJpojZhsc', '10 years')
]