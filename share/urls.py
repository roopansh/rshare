from django.conf.urls import url
from . import views

app_name='share'

urlpatterns = [
    #index page
    url(r'^$', views.home, name='home'),

    # upload page
    url(r'^upload/$', views.index, name='index'),

    #login
    url(r'^login/$', views.login_user, name='login'),

    #logout
    url(r'^logout/$', views.logout_user, name='logout'),

    #signup feature
    url(r'^register/$', views.register, name='register'),

    #public list
    url(r'^public/$', views.public, name='public'),

    # download link using pk
    url(r'^download/(?P<file_id>[0-9]+)/$', views.downloadfile, name='download'),

    # validating password
    url(r'^download/(?P<file_id>[0-9]+)/pass$', views.password_validate, name='password_validate'),

]
