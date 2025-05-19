from django.urls import path
from . import views


urlpatterns=[
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


]