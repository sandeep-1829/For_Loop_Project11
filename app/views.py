from django.shortcuts import render

# Create your views here.

def forloop(request):
    D={'name1':'sanju','name2':'rohit'}
    return render(request,'forloop.html',context=D)
