from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    if request.method == 'POST':
        first_value = int(request.POST['num1'])
        second_value = int(request.POST['num2'])
        add = first_value + second_value
        print(add)
        context = {
            'add':add
        }
        return render(request,'polls/ans.html',context)
    else:
        return render(request,'polls/index.html')
    

def detail(request):
    return HttpResponse("detail page")
