from django.urls import path
from .views import CoursesListView, CourseDetailView

urlpatterns = [
    path('post/<int:pk>/', CourseDetailView.as_view(), name='course_item'),
    path('', CoursesListView.as_view(), name='home')
]