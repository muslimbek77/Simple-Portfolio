from django.urls import path
from portfolio.views import index
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('',index,name='home'),
]+staticfiles_urlpatterns()

