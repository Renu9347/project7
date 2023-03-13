from django.shortcuts import render

# Create your views here.
def first(request):
    d={'name':'Renu','age':4}
    return render(request,'first.html',context=d)
