from django.shortcuts import render
from .models import Portfolios,Cards,Resumes,Createaccount
from django.utils import timezone
import datetime

# Create your views here.
def index(req):
    res=Resumes.objects.all()
    card=Cards.objects.all()
    show = Portfolios.objects.all()
    return render(req,"index.html",{'show':show,'card':card,'res':res})
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
def portfolio1(req):
    return render(req,"portfolio1.html")
def portfolio2(req):
    return render(req,"portfolio2.html")
def portfolio3(req):
    return render(req,"portfolio3.html")
def portfolio4(req):
    return render(req,"portfolio4.html")
def portfolio5(req):
    return render(req,"portfolio5.html")
