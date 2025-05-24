from django.urls import path
from . import views


urlpatterns=[
    path('', views.index, name='index'),
    # path('<int:port_id>',views.index,name='index'),
    path('createaccount/',views.createaccount,name='createaccount'),
    path('nextpage/<int:port_id>/', views.nextpage, name='nextpage'),
    path('nextpage2/<int:resu_id>/',views.nextpage2,name='nextpage2'),
    path('nextpage3/<int:card_id>/',views.nextpage3,name='nextpage3'),

    path('nextpage2/<int:resu_id>/resume1/',views.resume1,name='resume1'),
    path('nextpage2/<int:resu_id>/resume2/',views.resume2,name='resume2'),
    path('nextpage2/<int:resu_id>/resume3/',views.resume3,name='resume3'),
    path('nextpage2/<int:resu_id>/resume4/',views.resume4,name='resume4'),
    path('nextpage2/<int:resu_id>/resume5/',views.resume5,name='resume5'),
    path('nextpage2/<int:resu_id>/resume6/',views.resume6,name='resume6'),

    path('nextpage3/<int:card_id>/card1/',views.card1,name='card1'),
    path('nextpage3/<int:card_id>/card2/',views.card2,name='card2'),
    path('nextpage3/<int:card_id>/card3/',views.card3,name='card3'),
    path('nextpage3/<int:card_id>/card4/',views.card4,name='card4'),
    path('nextpage3/<int:card_id>/card5/',views.card5,name='card5'),
    path('nextpage3/<int:card_id>/card6/',views.card6,name='card6'),

    path('carddynamicform/',views.carddynamicform,name='carddynamicform'),
    path('resumedynamicform/',views.resumedynamicform,name='resumedynamicform'),

    path('nextpage/<int:port_id>/portfolio1/',views.portfolio1,name='portfolio1'),
    path('nextpage/<int:port_id>/portfolio2/',views.portfolio2,name='portfolio2'),
    path('nextpage/<int:port_id>/portfolio3/',views.portfolio3,name='portfolio3'),
    path('nextpage/<int:port_id>/portfolio4/',views.portfolio4,name='portfolio4'),
    path('nextpage/<int:port_id>/portfolio5/',views.portfolio5,name='portfolio5'),

    path('cardreadmore/',views.cardreadmore,name='cardreadmore'),
    path('resumereadmore/',views.resumereadmore,name='resumereadmore'),

]