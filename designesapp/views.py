from django.shortcuts import render
from .models import Portfolios

# Create your views here.
def index(req):
    show = Portfolios.objects.all()
    return render(req,"index.html",{'show':show})
def createaccount(req):
    return render(req,"createaccount.html")
def nextpage(req,port_id):
    show = Portfolios.objects.get(port_id=port_id)
    return render(req,"nextpage.html",{'show':show})
def nextpage3(req):
    return render(req,"nextpage3.html")
def nextpage2(req):
    return render(req,"nextpage2.html")