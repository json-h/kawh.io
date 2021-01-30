from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('import/', views.import_league, name='import'),
    path('player/<str:p_id>', views.player, name='player'),
    path('players-list/<str:stat>', views.players_list, name='players-list'),
    path('compare/<int:week_num>', views.compare, name='compare'),
    path('search/', views.search, name='search'),
    path('refresh/', views.refresh, name='refresh'),
    path('success/', views.success, name='success'),
    path('league/', views.league, name='league'),
    path('test/', views.test, name='test'),
]