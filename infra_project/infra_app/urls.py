from django.urls import path

from . import views

app_name = 'infra_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('second/', views.second_pages, name='second_pages'),

]
