from django.urls import path
from .views import newmethod,HomePageView, charge
from . import views
from django.views.generic.base import TemplateView

urlpatterns = [
    path('', HomePageView.as_view(), name="index"),
    path('newmethod/', views.newmethod, name="index"),
    path('charge/', views.charge, name='charge'),
]