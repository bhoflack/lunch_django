from django.conf.urls.defaults import *

urlpatterns = patterns('lunch_django.lunch.views',
    (r'^$', 'index'),
    (r'^(?P<product_id>\d+)/order/$', 'order'),
)
