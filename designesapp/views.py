from django.shortcuts import render
from .models import Portfolios,Cards,Resumes

# Create your views here.
def index(req):
    res=Resumes.objects.all()
    card=Cards.objects.all()
    show = Portfolios.objects.all()
    return render(req,"index.html",{'show':show,'card':card,'res':res})
def createaccount(req):
    return render(req,"createaccount.html")
def nextpage(req,port_id):
    show = Portfolios.objects.get(port_id=port_id)
    return render(req,"nextpage.html",{'show':show})
def nextpage3(req,card_id):
    show = Cards.objects.get(card_id=card_id)
    return render(req,"nextpage3.html",{'show':show})
def nextpage2(req,resu_id):
    show = Resumes.objects.get(resu_id=resu_id)
    return render(req,"nextpage2.html",{'show':show})