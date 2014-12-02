from django.conf.urls import patterns, include, url
from django.contrib.auth.forms import AuthenticationForm
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'GAE_Django14.views.home', name='home'),
    # url(r'^GAE_Django14/', include('GAE_Django14.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),


    (r'^$', 'django.views.generic.simple.redirect_to', {'url': '/testapp/', }),
    (r'^testapp/', include('testapp.urls')),

    (r'^accounts/create_user/$', 'testapp.views.create_new_user'),
    (r'^accounts/login/$', 'django.contrib.auth.views.login',
        {'authentication_form': AuthenticationForm,
        'template_name': 'testapp/login.html',}),
    (r'^accounts/profile/$', 'django.views.generic.simple.redirect_to', {'url': '/testapp/', }),
    (r'^accounts/logout/$', 'django.contrib.auth.views.logout',
        {'next_page': '/testapp/',}),
)
