from django.urls import path
from game_app import views

urlpatterns = [
    path('', views.game_view, name='game'),
]
