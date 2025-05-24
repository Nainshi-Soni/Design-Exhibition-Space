from django.urls import path
from . import views


urlpatterns=[
    path('', views.index, name='index'),
    # path('<int:port_id>',views.index,name='index'),
    path('createaccount/',views.createaccount,name='createaccount'),
    path('nextpage/<int:port_id>/', views.nextpage, name='nextpage'),
    path('nextpage2/<int:resu_id>/',views.nextpage2,name='nextpage2'),
    path('nextpage3/<int:card_id>/',views.nextpage3,name='nextpage3'),
    path('portfolio1/',views.portfolio1,name='portfolio1'),
    path('portfolio2/',views.portfolio2,name='portfolio2'),
    path('portfolio3/',views.portfolio3,name='portfolio3'),
    path('portfolio4/',views.portfolio4,name='portfolio4'),
    path('portfolio5/',views.portfolio5,name='portfolio5'),

]