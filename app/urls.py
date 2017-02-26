from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views

urlpatterns=[
    url(r'^$', views.index, name="homepage"),
    url(r'^login/$', auth_views.login, name="login"),
    url(r'^logout/$', auth_views.logout, name="logout"),
    url(r'^password_change/$', auth_views.password_change),
    url(r'^password_reset/$', auth_views.password_reset),
    
]
