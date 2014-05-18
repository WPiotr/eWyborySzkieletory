from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'eWybory.views.home', name='home'),
    # url(r'^eWybory/', include('eWybory.foo.urls')),
    # Uncomment the admin/doc line below to enable admin documentation:
    #url(r'^admin/doc/$', include('django.contrib.admindocs.urls')),
    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
    (r'^$','MainApp.views.index'),
    (r'^election/electionView/(?P<election>\d+)/$','MainApp.views.electionView'),
    (r'^election/activeList/$','MainApp.views.activeElections'),
    (r'^election/inactiveList/$','MainApp.views.inactiveElections'),
    (r'^user/profile/$','MainApp.views.profile'),
    (r'^user/register/$','MainApp.views.register'),
    (r'^user/registerUser/$','MainApp.views.registerUser'),
    (r'^views/aboutUs/$','MainApp.views.aboutUs'),
    (r'^accounts/login/$','MainApp.views.login'),
    (r'^accounts/logout/$', 'django.contrib.auth.views.logout',{'next_page': '/'}),
    (r'^user/editProfile/$','MainApp.views.editProfile'),
)
