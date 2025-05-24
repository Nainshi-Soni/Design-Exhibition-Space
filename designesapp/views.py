from django.shortcuts import render
from .models import Portfolios,Cards,Resumes,Createaccount
from django.utils import timezone
import datetime

# Create your views here.
def index(req):
    show = Portfolios.objects.all()
    return render(req,"index.html",{'show':show})
def createaccount(req):
    if req.method=="POST":
        name=req.POST['name']
        email=req.POST['email']
        contactno=req.POST['contactno']
        passw=req.POST['passw']
        cpassw=req.POST['cpassw']
        date=datetime.date.today()
        createaccount=Createaccount(name=name,email=email,contactno=contactno,passw=passw,cpassw=cpassw,date=date)
        createaccount.save()
        return render(req,"index.html")
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
def portfolio1(req,port_id):
    show = Portfolios.objects.get(port_id=port_id)
    return render(req,"portfolio1.html",{'show':show})
def portfolio2(req,port_id):
    show = Portfolios.objects.get(port_id=port_id)
    return render(req,"portfolio2.html",{'show':show})
def portfolio3(req,port_id):
    show = Portfolios.objects.get(port_id=port_id)
    return render(req,"portfolio3.html",{'show':show})
def portfolio4(req,port_id):
    show = Portfolios.objects.get(port_id=port_id)
    return render(req,"portfolio4.html",{'show':show})
def portfolio5(req,port_id):
    show = Portfolios.objects.get(port_id=port_id)
    return render(req,"portfolio5.html",{'show':show})
def cardreadmore(req):
    card=Cards.objects.all()
    return render(req,"cardreadmore.html",{'card':card})
def resumereadmore(req):
    res=Resumes.objects.all()
    return render(req,"resumereadmore.html",{'res':res})