from django.conf.urls import patterns, include, url

from views import AlgoListView, AlgoDetailed

urlpatterns = patterns('',
    
    #url(r'^tag/(?P<slug>[-\w]+)/$)', TagIndexView.as_view(), name="tagged"),
    url(r'^explore/', AlgoListView.as_view()),
    url(r'^explore/(?P<pk>[-_\w]+)/$', AlgoDetailed.as_view()),

    
)
