# front app views

from django.shortcuts import render,redirect
from . models import Contact
# Create your views here.
def index(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']

        db_save = Contact(db_name=name,db_email=email,db_message=message)
        db_save.save()
        return redirect('index')

    return render(request,'index.html')

def gallery(request):
    
    return render(request,'gallery.html')

def generic(request):
    return render(request,'generic.html')