from django.conf.urls import url

from . import views

app_name = 'authenticate'
urlpatterns = [
    url(r'^$', views.authentificate),
    url(r'login', views.login),
    url(r'logout', views.logout),
    url(r'register', views.register)
]
