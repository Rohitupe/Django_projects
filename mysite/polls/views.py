from django.shortcuts import render,redirect
from django.http import HttpResponse
# Create your views here.

def index(request):
    if request.method == 'POST':
        first_value = request.POST['num1']
        second_value = request.POST['num2']

        if first_value or second_value:

            if request.POST['go'] == 'on':
                add = int(first_value) + int(second_value)
                print(add)
                context = {
                    'add':add
                }
                return render(request,'polls/ans.html',context)
                
            else:
                return redirect('index')
        
        else:
            return redirect('index')

    else:
        return render(request,'polls/add.html')
    

def detail(request):
    return HttpResponse("detail page")
