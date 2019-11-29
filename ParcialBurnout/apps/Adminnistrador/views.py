from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response


# Create your views here.

#def index(request):
    #return HttpResponse('<a href="{% url 'index' %}" >Home</a>')
    #return render(request, 'templates/index.html', {})
    #return render(request, 'templates/index.html', {})

def Homepage(request):
    #CB
     return render(request,'home.html')

def Login_user(request):
    #CB
     return render(request,'login_user.html')

def test(request):
    #CB
     return render(request,'test.html')

def Dataphp(request):
    #CB
     return render(request,'operar.php')

def Dbz11111(request):
    #CB
     return render(request,'accion.php')