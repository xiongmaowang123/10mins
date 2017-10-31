from django.shortcuts import render


def index(request):
    return render(request, 'index.html',{})

def detail(request):
    return render(request, 'detail.html',{})

def searchpage(request):
    return render(request, 'searchpage.html',{})

def myinfo(request):
    return render(request, 'myinfo.html',{})

def writeAtc(request):
    return render(request, 'write.html',{})

def geRenXingXi(request):
    return render(request, 'geRenXingXi.html',{})
