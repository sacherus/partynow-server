from django.conf.urls import patterns, include, url
from party.views import join, organizer
from views import index, PartyList, PartyDetail, UserList, UserDetail, my_user_data

__author__ = 'sacherus'

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'hellodjango.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    #url(r'^party/', include('party.urls')),
    url(r'^index$', index),
    url(r'^users/$', UserList.as_view()),
    url(r'^(?P<pk>\d+)/join$', join),
    url(r'^(?P<pk>\d+)/organize$', organizer),
    url(r'^(?P<pk>\d+)$', PartyDetail.as_view(), name='party-detail'),
    url(r'^users/(?P<pk>\d+)$', UserDetail.as_view(), name='user-detail'),
    url(r'^users/me$', my_user_data),
    url(r'^$', PartyList.as_view()),
    url(r'^users/register', 'party.views.create_auth'),
)