from django.shortcuts import render

# Create your views here.
def index(req):
    return render(req,"index.html")
def resume1(req):
    return render(req,"resume1.html")
def resume2(req):
    return render(req,"resume2.html")
def resume3(req):
    return render(req,"resume3.html")
def resume4(req):
    return render(req,"resume4.html")
