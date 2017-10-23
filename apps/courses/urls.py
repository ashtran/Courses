from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^courses/create$', views.create),
    url(r'^courses/destroy/(?P<course_id>\d+)$', views.show),
    url(r'^(?P<course_id>\d+)/destroy/confirm$', views.destroy),
]
