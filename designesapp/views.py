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
def resume1(req):
    return render(req,"resume1.html")
def resume2(req):
    return render(req,"resume2.html")
def resume3(req):
    return render(req,"resume3.html")
def resume4(req):
    return render(req,"resume4.html")
def resume5(req):
    return render(req,"resume5.html")
def resume6(req):
    return render(req,"resume6.html")
def card6(req):
    return render(req,"card6.html")
def card5(req):
    return render(req,"card5.html")
def card4(req):
    return render(req,"card4.html")
def card3(req):
    return render(req,"card3.html")
def card2(req):
    return render(req,"card2.html")
def card1(req):
    return render(req,"card1.html")
def resumedynamicform(req):
    return render(req,"resumedynamicform.html")
def carddynamicform(req):
    return render(req,"carddynamicform.html")