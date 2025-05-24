from django.contrib import admin
from .models import Portfolios,Cards,Resumes,Createaccount

# Register your models here.
admin.site.register(Portfolios)
admin.site.register(Cards)
admin.site.register(Resumes)
admin.site.register(Createaccount)