from django.urls import path
from .views import *

urlpatterns = [
    path('posts/', BlogDisplay.as_view(), name='post'),
    path('home/', HomePageView.as_view(), name='home'),
    path('posts/<int:pk>/', BlogDetailView.as_view(), name='post_detail'),

]
