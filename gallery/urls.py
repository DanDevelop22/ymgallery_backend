from django.urls import path
from .views import PaintLastAPIView, PaintRecommendedAPIView, PaintFilterAPIView

urlpatterns = [
   path('paint-last/', PaintLastAPIView.as_view()),
   path('paint-recommended/', PaintRecommendedAPIView.as_view()),
   path('paint-filter/', PaintFilterAPIView.as_view())
]