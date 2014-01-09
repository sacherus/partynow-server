from django.conf.urls import patterns, include, url

from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'hellodjango.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),
                       url(r'^party/', include('party.urls')),
                       url(r'^admin/', include(admin.site.urls)),

)

urlpatterns += patterns('',
                        url(r'^api-auth/', include('rest_framework.urls',
                                                   namespace='rest_framework')),
                        #url(r'^api-token-auth/', 'rest_framework.authtoken.views.obtain_auth_token'),
                        url(r'^oauth2/', include('provider.oauth2.urls', namespace='oauth2')),
)



#login and authentication
#urlpatterns += patterns('',
#    #url(r'^accounts/', include('auth.urls')),
#    #url(r'^accounts/register', 'register'),
#    #url(r'^accounts/login', 'login'),
#    #url(r'^accounts/logout', 'logout'),
#    url(r'^accounts/', include('auth.urls')),
#    #url(r'^accounts/edit', 'edit'),
#
#)
