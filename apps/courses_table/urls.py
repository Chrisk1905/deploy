from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^create$', views.add_course),
    url(r'^courses/destory/(?P<course_id>\d*)$', views.destory),
    url(r'^courses/delete/(?P<course_id>\d*)$', views.delete),
]
