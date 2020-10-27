from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('rooms/<str:room_name>/', views.room, name='room'),
    # CMD version
    path('logout/', views.logout, name='logout'),
    path('login/', views.login, name='login'),
    path('list/', views.get_rooms_list, name='list'),
    path('get/', views.get_messages, name='get'),
    path('send/', views.send_message, name='send'),
]