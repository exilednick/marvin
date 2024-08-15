from django.urls import path
from . import views

urlpatterns = [
    path('word_frequency', views.word_frequency_analysis, name='word_frequency_analysis'),
    path('search_history', views.get_search_history, name='search_history'),
]
