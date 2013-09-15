from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
     url(r'^$', 'myNotesBackend.views.home', name='home'),
     url(r'^login', 'myNotesBackend.views.login'),
     url(r'^auth', 'myNotesBackend.views.auth_view'),
     url(r'^logout', 'myNotesBackend.views.logout'),
     url(r'^addnote', 'myNotesBackend.views.addnote'),
     url(r'^registration', 'myNotesBackend.views.registration'),
     url(r'^register', 'myNotesBackend.views.register'),
     url(r'^deletenote', 'myNotesBackend.views.delete_note'),

    # Uncomment the admin/doc line below to enable admin documentation:
    #url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    #url('', include('django.contrib.auth.urls')),
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
