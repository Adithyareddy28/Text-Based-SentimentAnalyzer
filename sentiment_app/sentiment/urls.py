from django.urls import path
from . import views

urlpatterns = [
    path('', views.sentiment_analysis, name='sentiment'),
]
