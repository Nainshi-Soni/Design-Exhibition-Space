from django.shortcuts import render,redirect
from django.core.exceptions import ObjectDoesNotExist
from .models import Portfolios,Cards,Resumes,Createaccount,login
from django.contrib import messages
from django.core.mail import send_mail
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
          msg="Please enter same password" 
          return render(req,"createaccount.html",{'msg':msg})
    return render(req,"createaccount.html")
def logcode(req):
    if req.method=="POST":
        email=req.POST.get('email')
        passw=req.POST.get('passw')
        try:
            user=Createaccount.objects.get(email=email,passw=passw)
            return redirect('index')
        except Createaccount.DoesNotExist:  
            return render(req,'index.html',{'msg':'Invalid User'})
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