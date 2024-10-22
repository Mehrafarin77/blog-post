from django.shortcuts import render
from .models import *
from django.views.generic import ListView, TemplateView, DetailView

# Create your views here.
class BlogDisplay(ListView):
    model = Blog
    template_name = 'posts.html'
    context_object_name = 'all_posts'

class HomePageView(TemplateView):
    template_name = 'home.html'


class BlogDetailView(DetailView):
    model = Blog
    template_name = 'post_detail.html'
    context_object_name = 'blog'