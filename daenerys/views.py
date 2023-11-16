from django.shortcuts import render

# Create your views here.
def dany(request):
    queen='asssume this  data is from database'
    venu={'assume':queen,'Realname':'Emilia'}
    return render(request,'queen.html',context=venu)
