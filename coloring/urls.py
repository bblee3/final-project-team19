from django.urls import path
from . import views

urlpatterns = [
    path('start/', views.start, name='start'),
    path('settings/', views.settings, name='settings'),
    path('math/', views.math, name='math'),
    path('correct/', views.correct, name='correct'),
    path('incorrect/', views.incorrect, name='incorrect')
]
