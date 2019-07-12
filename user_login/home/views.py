from django.shortcuts import render
from .models import User_data
# Create your views here.
def index(request):
    data = User_data.objects.all()
    context = {
        'data':data
    }
    return render(request,'index.html',context)