from django.conf.urls import url
#同じ階層から
from . import views

urlpatterns=[url(r'^$',views.index,name='index')]