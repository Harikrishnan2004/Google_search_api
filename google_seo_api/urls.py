from django.urls import path
from . import views

app_name = "api"

urlpatterns = [
    path('/home', views.home, name='home'),
    path('/search_links', views.get_links, name='links'),
    path('/search_images', views.get_images, name='images'),
    path('/search_pdfs', views.get_pdfs, name='pdfs')
]