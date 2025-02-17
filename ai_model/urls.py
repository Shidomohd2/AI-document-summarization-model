from django.urls import path
from . import views

urlpatterns = [
    path('', views.chat_view, name='chat'),  # Handles '/chat/'
    path('load-chat/', views.load_chat_history, name='load_chat'),  # Handles '/chat/load-chat/'
]