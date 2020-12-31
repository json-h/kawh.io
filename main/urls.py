from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('import/', views.import_league, name='import'),
    path('player/<str:p_id>', views.player, name='player'),
    path('search/', views.search, name='search'),
    path('success/', views.success, name='success'),
]