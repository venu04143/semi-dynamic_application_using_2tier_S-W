from django.shortcuts import render

# Create your views here.

def jonsnow(request):
    data='The White Wolf'
    d={'king':data,'realname':'kit harington'}


    return render(request,'jonsnow.html',context=d)