from . import views
from django.urls import path

urlpatterns = [
    path('', views.home),
    path('dictionary/<code>', views.dictionary),
    path('search/en/', views.search_en),
    path('search/es/', views.search_es),
]
