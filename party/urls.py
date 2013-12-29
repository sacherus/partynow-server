from django.conf.urls import patterns, include, url
from views import index, PartyList, PartyDetail, UserList

__author__ = 'sacherus'

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'hellodjango.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    #url(r'^party/', include('party.urls')),
    url(r'^index$', index),
    #url(r'^users/$', UserList.as_view()),
    url(r'^(?P<pk>\d+)$', PartyDetail.as_view(), name='party-detail'),
    url(r'^$', PartyList.as_view()),
)