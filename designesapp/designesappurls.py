from django.urls import path
from . import views


urlpatterns=[
    path('portfolio1/',views.portfolio1,name='portfolio1'),
    path('portfolio2/',views.portfolio2,name='portfolio2'),
    path('portfolio3/',views.portfolio3,name='portfolio3'),
    path('portfolio4/',views.portfolio4,name='portfolio4'),
    path('portfolio5/',views.portfolio5,name='portfolio5'),
]