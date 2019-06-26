from django.shortcuts import render,redirect
from django.contrib import messages
# Create your views here.

def index(request):
    return render(request,'weblet/index.html',{})

def rmspace(request):
    i_text = request.GET.get('text','default')
    i = ''
    if i_text:
        if request.GET.get('rspace') == 'on':
            i = i_text.replace(" ","")  
        if request.GET.get('rspace') == 'off':
            return redirect('rm_space')

    else:
        return redirect('index')
        
    context = {
        'text':i_text,
        'removed':i,
        }
    return render(request,'weblet/rmspace.html',context)

    
