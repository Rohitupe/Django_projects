# front app views

from django.shortcuts import render,redirect
from . models import Contact,Image
# Create your views here.
def index(request):

    images = Image.objects.all()[:10]

    context={
        'images':images
    }

    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']

        db_save = Contact(db_name=name,db_email=email,db_message=message)
        db_save.save()
        return redirect('index')
    return render(request,'index.html',context)

def gallery(request):
    images = Image.objects.all()
    context={
        'images':images
    }
    return render(request,'gallery.html',context)

def generic(request):
    return render(request,'generic.html')