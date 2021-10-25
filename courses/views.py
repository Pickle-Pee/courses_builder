from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post


class CoursesListView(ListView):
    model = Post
    template_name = 'home.html'


class CourseDetailView(DetailView):
    model = Post
    template_name = 'course_item.html'
