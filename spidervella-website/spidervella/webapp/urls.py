"""spidervella_web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views as pages_views

urlpatterns = [
    path('',pages_views.index, name="home" ), 

    path('programs',pages_views.programs, name="programs" ),
    path('program-details',pages_views.program_details, name="programs details" ),

    path('events',pages_views.events, name="events" ),

    path('news',pages_views.news, name="news" ),

    path('about',pages_views.about, name="about" ),

    path('contact',pages_views.contact, name="contact" ),

    path('maintenance',pages_views.maintenance, name="maintenance" ),

    path('privacy-policies',pages_views.privacy_policies, name="policies" ),

     path('terms-and-conditions',pages_views.terms_and_conditions, name="terms conditions" ),

     path('get-training',pages_views.get_training, name="get training" ),
]
