from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('about/', views.about, name = 'about'),
    path('fishlist/', views.fishlist, name = 'index'),
    path('fish/<int:fish_id>/', views.fish_detail, name='detail'),
    path('fish/c/', views.fish_c, name="fishc"),
    path('fish/create/', views.create_fish, name="createfish"),
    path('fish/<int:fish_id>/delete', views.delete_fish, name='fish_delete'),
    path('fish/<int:fish_id>/edit', views.edit_view, name='fish_update'),
    path('fish/<int:fish_id>/edited', views.edit_fish, name="editfish"),
    path('fish/<int:fish_id>/add_feeding/', views.add_feeding, name='add_feeding'),
]