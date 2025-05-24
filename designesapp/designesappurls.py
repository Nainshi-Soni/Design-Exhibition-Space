from django.urls import path
from . import views


urlpatterns=[
    path('', views.index, name='index'),
    # path('<int:port_id>',views.index,name='index'),
    path('createaccount/',views.createaccount,name='createaccount'),
    path('nextpage/<int:port_id>/', views.nextpage, name='nextpage'),
<<<<<<< HEAD

=======
>>>>>>> 7470f367b19136255d71d845562fe2e026b2e1d1
    path('nextpage2/',views.nextpage2,name='nextpage2'),
    path('nextpage3/',views.nextpage3,name='nextpage3'),
    path('resume1/',views.resume1,name='resume1'),
    path('resume2/',views.resume2,name='resume2'),
    path('resume3/',views.resume3,name='resume3'),
    path('resume4/',views.resume4,name='resume4'),
    path('resume5/',views.resume5,name='resume5'),
    path('resume6/',views.resume6,name='resume6'),
    path('card1/',views.card1,name='card1'),
    path('card2/',views.card2,name='card2'),
    path('card3/',views.card3,name='card3'),
    path('card4/',views.card4,name='card4'),
    path('card5/',views.card5,name='card5'),
    path('card6/',views.card6,name='card6'),
    path('carddynamicform/',views.carddynamicform,name='carddynamicform'),
    path('resumedynamicform/',views.resumedynamicform,name='resumedynamicform'),
    path('nextpage2/<int:resu_id>/',views.nextpage2,name='nextpage2'),
    path('nextpage3/<int:card_id>/',views.nextpage3,name='nextpage3'),
<<<<<<< HEAD
    path('portfolio1/',views.portfolio1,name='portfolio1'),
    path('portfolio2/',views.portfolio2,name='portfolio2'),
    path('portfolio3/',views.portfolio3,name='portfolio3'),
    path('portfolio4/',views.portfolio4,name='portfolio4'),
    path('portfolio5/',views.portfolio5,name='portfolio5'),

=======
    path('nextpage/<int:port_id>/portfolio1/',views.portfolio1,name='portfolio1'),
    path('nextpage/<int:port_id>/portfolio2/',views.portfolio2,name='portfolio2'),
    path('nextpage/<int:port_id>/portfolio3/',views.portfolio3,name='portfolio3'),
    path('nextpage/<int:port_id>/portfolio4/',views.portfolio4,name='portfolio4'),
    path('nextpage/<int:port_id>/portfolio5/',views.portfolio5,name='portfolio5'),
    path('cardreadmore/',views.cardreadmore,name='cardreadmore'),
    path('resumereadmore/',views.resumereadmore,name='resumereadmore'),
>>>>>>> 7470f367b19136255d71d845562fe2e026b2e1d1

]