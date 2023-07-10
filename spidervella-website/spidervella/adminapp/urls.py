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

from django.urls import path
from . import views as admin_views

urlpatterns = [
    path('dashboard',admin_views.dashboard, name="dashboard" ), 

    path('signin',admin_views.signin, name="signin" ), 

    path('payment_history',admin_views.payment_history, name="payment_history" ), 

    path('course/add',admin_views.add_course, name="add_course" ), 
    path('course/update',admin_views.update_course, name="update_course" ),
    path('course/delete',admin_views.delete_course, name="delete_course" ), 
    path('course/view',admin_views.view_course, name="view_course" ), 
    path('logout',admin_views.logout, name="logout"),
 





]
