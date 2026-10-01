from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('post/<slug:slug>/', views.post, name='post'),
    path('data-product-management/', views.dpm, name='dpm'),
    path('data_ai-gov/', views.datagovernance, name='datagov'),


]