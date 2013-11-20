from django.conf.urls import patterns, include, url
 
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples: 
     url(r'^index/', 'sitelojas.views.index', name='index'),
     url(r'^produtos/', include('produtos.urls')),
     url(r'^login/$', 'django.contrib.auth.views.login',{'template_name': 'login.html' }),
     url(r'^logout/$', 'django.contrib.auth.views.logout_then_login',{'login_url': '/login/'}),

    # url(r'^sitelojas/', include('sitelojas.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
