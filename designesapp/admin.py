from django.contrib import admin
from .models import Portfolios,Cards,Resumes,Createaccount,login,DownloadRecord,PortfolioDownloadRecord

# Register your models here.
admin.site.register(Portfolios)
admin.site.register(Cards)
admin.site.register(Resumes)
admin.site.register(Createaccount)
admin.site.register(login)
admin.site.register(DownloadRecord)
admin.site.register(PortfolioDownloadRecord)