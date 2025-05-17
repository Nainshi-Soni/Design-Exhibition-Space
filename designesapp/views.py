from django.shortcuts import render
from .models import Portfolios

# Create your views here.
def index(req):
    sh=Portfolios.objects.all()
    return render(req,"index.html",{'show':sh})
def createaccount(req):
    return render(req,"createaccount.html")
def nextpage(req):
    sh=Portfolios.objects.all()
    return render(req,"nextpage.html",{'show':sh})
def nextpage3(req):
    return render(req,"nextpage3.html")
def nextpage2(req):
    return render(req,"nextpage2.html")