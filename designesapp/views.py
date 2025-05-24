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
<<<<<<< HEAD
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
>>>>>>> f43eb2e559682a614a317aca5eb72cbfe99b5f71
