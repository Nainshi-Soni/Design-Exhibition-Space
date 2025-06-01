from django.http import FileResponse, Http404
from django.conf import settings
from django.urls import reverse
from django.shortcuts import render,redirect
from django.core.exceptions import ObjectDoesNotExist
from .models import Portfolios,Cards,Resumes,Createaccount,login
from django.contrib import messages
from django.core.mail import send_mail
from django.utils import timezone
import datetime
import razorpay
import os


# Create your views here.
def index(req):
    show = Portfolios.objects.all()
    return render(req,"index.html",{'show':show})
def choosepage(req):
    if 'user_email' not in req.session:
        return redirect('index')
    return render(req, 'choosepage.html')
def createaccount(req):
    if req.method=="POST":
        name=req.POST['name']
        email=req.POST['email']
        contactno=req.POST['contactno']
        passw=req.POST['passw']
        cpassw=req.POST['cpassw']
        date=datetime.date.today()
        if cpassw==req.POST['passw']:
            createaccount=Createaccount(name=name,email=email,contactno=contactno,passw=passw,cpassw=cpassw,date=date)
            createaccount.save()
            subject = 'Welcome to the Design Exhibition Space'
            message = f'''
            Dear {name},
            Craft Your Creative Identity!
            Explore a curated collection of professional templates designed to elevate your personal brand. Whether you're building your portfolio, updating your resume, or designing a standout business card, you'll find inspiration and practical tools here.
            Username: {email}
            Password:{passw}
            🖌️ Choose from modern, minimalist, and artistic styles
            📁 Customize templates for print or digital use
            💼 Perfect for designers, creatives, and job-seekers

    
            Start creating. Stand out with design that speaks.'''
            from_email = 'nainshisoni28042001@gmail.com'
            recipient_list = [email]

            # Send email
            send_mail(subject, message, from_email, recipient_list)
            return redirect('index')
        else:
          msg="❗Oops! Your passwords don’t match. Please re-enter the same password in both fields." 
          return render(req,"createaccount.html",{'msg':msg})
    return render(req,"createaccount.html")
def logcode(req):
    if req.method=="POST":
        email=req.POST.get('email')
        passw=req.POST.get('passw')
        try:
            user=Createaccount.objects.get(email=email,passw=passw)
            req.session['user_email']=email
            return redirect('choosepage')
        except Createaccount.DoesNotExist:  
            return render(req,'index.html',{'msg':'Invalid User'})
    return render(req,"createaccount.html")

def nextpage(req,port_id):
    show = Portfolios.objects.get(port_id=port_id)
    is_logged_in = 'user_email' in req.session
    return render(req,"nextpage.html",{'show':show, 'is_logged_in': is_logged_in})
def nextpage3(req,card_id):
    show = Cards.objects.get(card_id=card_id)
    is_logged_in = 'user_email' in req.session
    return render(req,"nextpage3.html",{'show':show, 'is_logged_in': is_logged_in})
def nextpage2(req,resu_id):
    show = Resumes.objects.get(resu_id=resu_id)
    is_logged_in = 'user_email' in req.session
    return render(req,"nextpage2.html",{'show':show, 'is_logged_in': is_logged_in})

def resume1(req,resu_id):
    show = Resumes.objects.get(resu_id=resu_id)
    return render(req,"resume1.html",{'show':show})
def resume2(req,resu_id):
    show = Resumes.objects.get(resu_id=resu_id)
    return render(req,"resume2.html",{'show':show})
def resume3(req,resu_id):
    show = Resumes.objects.get(resu_id=resu_id)
    return render(req,"resume3.html",{'show':show})
def resume4(req,resu_id):
    show = Resumes.objects.get(resu_id=resu_id)
    return render(req,"resume4.html",{'show':show})
def resume5(req,resu_id):
    show = Resumes.objects.get(resu_id=resu_id)
    return render(req,"resume5.html",{'show':show})
def resume6(req,resu_id):
    show = Resumes.objects.get(resu_id=resu_id)
    return render(req,"resume6.html",{'show':show})

def card6(req,card_id):
    show = Cards.objects.get(card_id=card_id)
    return render(req,"card6.html",{'show':show})
def card5(req,card_id):
    show = Cards.objects.get(card_id=card_id)
    return render(req,"card5.html",{'show':show})
def card4(req,card_id):
    show = Cards.objects.get(card_id=card_id)
    return render(req,"card4.html",{'show':show})
def card3(req,card_id):
    show = Cards.objects.get(card_id=card_id)
    return render(req,"card3.html",{'show':show})
def card2(req,card_id):
    show = Cards.objects.get(card_id=card_id)
    return render(req,"card2.html",{'show':show})
def card1(req,card_id):
    show = Cards.objects.get(card_id=card_id)
    return render(req,"card1.html",{'show':show})

def resumedynamicform(req):
    return render(req,"resumedynamicform.html")
def carddynamicform(req):
    return render(req,"carddynamicform.html")


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
    if 'user_email' not in req.session:
        return redirect('index')
    res=Resumes.objects.all()
    return render(req,"resumereadmore.html",{'res':res})

client = razorpay.Client(auth=(settings.RAZORPAY_API_KEY,settings.RAZORPAY_API_SECRET_KEY))

def payment(req):
    order_amount=1000
    order_currency='INR'
    payment_order=client.order.create(dict(amount=order_amount,currency=order_currency,payment_capture=1))
    payment_order_id=payment_order['id']
    context={
        'amount':10, 'api_key':settings.RAZORPAY_API_KEY, 'order_id':payment_order_id
    }


    return render(req,'payment.html',context)
