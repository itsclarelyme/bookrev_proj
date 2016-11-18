from django.conf.urls import url
from . import views

urlpatterns=[
	url(r'^$', views.index),
	url(r'^home$', views.home),
	url(r'^addbook$', views.addbook),
	url(r'^display/(?P<id>\d+)$', views.displaybook),
	url(r'^user/(?P<id>\d+)$', views.index),
	url(r'^login/process$', views.login),
	url(r'^register/process$', views.register),
	url(r'^addbook/process$', views.addbookprocess),
	url(r'^addreview/process$', views.addreviewprocess),
	url(r'^profile/(?P<id>\d+)$', views.userprofile)


]