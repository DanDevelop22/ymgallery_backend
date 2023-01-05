from django.urls import path
from .views import PaintLastAPIView

urlpatterns = [
   path('paint-last/', PaintLastAPIView.as_view())
]