from django.urls import path

from .views import SignUpView, SignUpViewTeacher

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('teacher/', SignUpViewTeacher.as_view(), name='teacher')
]