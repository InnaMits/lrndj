from django.conf.urls import include, url
import django.contrib.auth.views
from django.contrib import admin
#from lrndj import views


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('lrndj.urls')),
    #url(r'^accounts/', include('registration.backends.hmac.urls')),
    url(r'^accounts/login/$', django.contrib.auth.views.login, name='login'),
    url(r'^accounts/logout/$', django.contrib.auth.views.logout, name='logout', kwargs={'next_page': '/'}),
]
