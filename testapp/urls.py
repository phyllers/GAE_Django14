from django.conf.urls.defaults import *

urlpatterns = patterns('testapp.views',
    (r'^$', 'list_greetings'),
    (r'^sign$', 'create_greeting')
)