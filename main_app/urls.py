from django.urls import path
from . import views
from .models import Dog

urlpatterns = [
path('', views.Home.as_view(), name ="Home"),
path('about/', views.About.as_view(), name = "About"),
path('dogs/',views.DogList.as_view(), name ="doglist.html"),
path('dogs/new/', views.DogCreate.as_view(), name="dog_create"),
path('dogs/<int:pk>/', views.DogDetail.as_view(), name='dogs_detail'),
path('dogs/<int:pk>/update', views.DogUpdate.as_view(), name='dog_update'),
path('dogs/<int:pk>/delete',views.DogDelete.as_view(), name="dog_delete"),
path('dogs/<int:pk>/mix/new/', views.MixCreate.as_view(), name="mix_create"),

]