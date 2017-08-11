from django.conf.urls import url, include
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import views as auth_views
from . import views

app_name='app'

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^login/$', auth_views.LoginView.as_view(template_name='app/login.html'), name='login'),
	url(r'^logout/$', views.logout, name='logout'),
	url(r'^register/$', views.register, name='register'),
	url(r'^upload/$', views.upload, name='upload'),
	url(r'^sign/$', views.sign, name='sign')
	
]