from django.conf.urls import url

from .models import Work, WorkCategory

from . import views

app_name = 'works'
urlpatterns = [
    url(r'^$', views.all, name='all'),
    url(r'^categories/(?P<work_category_slug>\w+)/$', views.category, name='category'),
    url(r'^categories/(?P<work_category_slug>\w+)/(?P<work_id>\w+)$', views.detail, name='detail'),
]
