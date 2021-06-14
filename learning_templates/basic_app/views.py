from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    #return HttpResponse("Basic One")
    mydict={"val":"press is okay","number":100}
    return render(request,"basic_app/index.html",context=mydict)


def relative(request):
    #return HttpResponse("Basic One")
    mydict={"val":"press is okay"}
    return render(request,"basic_app/relative_url_templates.html",context=mydict)


def other(request):
    #return HttpResponse("Basic One")
    mydict={"val":"press is okay"}
    return render(request,"basic_app/other.html",context=mydict)


def base(request):
    return render(request,"basic_app/base.html")
