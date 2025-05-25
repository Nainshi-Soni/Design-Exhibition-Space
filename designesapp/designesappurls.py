from django.urls import path
from . import views


urlpatterns=[
    path('', views.index, name='index'),
    # path('<int:port_id>',views.index,name='index'),
    path('createaccount/',views.createaccount,name='createaccount'),
    path('nextpage/<int:port_id>/', views.nextpage, name='nextpage'),
    path('nextpage2/<int:resu_id>/',views.nextpage2,name='nextpage2'),
    path('nextpage3/<int:card_id>/',views.nextpage3,name='nextpage3'),
    path('logcode/',views.logcode,name='logcode'),

]