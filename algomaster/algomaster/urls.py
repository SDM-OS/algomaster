from django.conf.urls import patterns, include, url
from django.contrib import admin
import content.views as views
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'algomaster.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', views.landing,),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^algorithms/', include('content.urls')),
)
