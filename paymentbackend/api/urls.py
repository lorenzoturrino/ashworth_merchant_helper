from django.conf.urls import url

from . import views

app_name = 'api'
urlpatterns = [
    url(r'^best_quote/$', views.best_quote, name='best_quote'),
    url(r'^$', views.index, name='index'),
]