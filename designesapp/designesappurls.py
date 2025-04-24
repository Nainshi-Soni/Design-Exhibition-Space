from django.urls import path
from . import views


urlpatterns=[
    # path('',views.index,name='index'),
    path('',views.portfolio1,name='portfolio1'),
]