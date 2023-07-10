
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required(login_url='/svt-admin/signin')

def dashboard(request):
    if 'user' in request.session:
        current_user = request.session['user']
        param = {'current_user': current_user}
        return render(request, 'dashboard.html', param)
    else:
        return redirect('signin')
    return render(request, 'signin.html')

def signin(request):

    if request.method == 'POST':
        name = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=name, password=password)
        if user is not None:
            login(request, user)
            request.session['user']=name
            return redirect('dashboard')
        else:
            return render(request, 'signin.html')

    return render(request,'signin.html')

def payment_history(request):
    return render(request, 'payment_history.html')

# course_management -----------------------------------------------------------------------------------

def add_course(request):
    return render(request, 'course/add.html')

def update_course(request):
    return render(request, 'course/update.html')

def delete_course(request):
    return render(request, 'course/delete.html')

def view_course(request):
    return render(request, 'course/view.html')

def logout(request):
    try:
        del request.session['user']
    except:
        return redirect('signin')
    return redirect('signin')



# lead_management -----------------------------------------------------------------------------------
def view_leads(request):
    return render(request, 'leads.html')
