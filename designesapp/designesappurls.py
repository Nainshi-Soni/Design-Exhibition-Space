from django.urls import path
from . import views


urlpatterns=[
    path('',views.index,name='index'),
    path('createaccount',views.createaccount,name='createaccount'),
    path('nextpage',views.nextpage,name='nextpage'),
    path('nextpage2',views.nextpage2,name='nextpage2'),
    path('nextpage3',views.nextpage3,name='nextpage3'),

]