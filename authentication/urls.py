from django.urls import path
from .views import *

urlpatterns = [
    path('login/', LoginApiView.as_view()),
    path('register/', RegisterCreateApiView.as_view())
]