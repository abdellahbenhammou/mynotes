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
     url(r'^filterbytag', 'myNotesBackend.views.filter_by_tag'),
     url(r'^gettags', 'myNotesBackend.views.get_tags'),


     url(r'^mynotes/$', 'myNotesBackend.views.home', name='home'),
     url(r'^mynotes/login', 'myNotesBackend.views.login'),
     url(r'^mynotes/auth', 'myNotesBackend.views.auth_view'),
     url(r'^mynotes/logout', 'myNotesBackend.views.logout'),
     url(r'^mynotes/addnote', 'myNotesBackend.views.addnote'),
     url(r'^mynotes/registration', 'myNotesBackend.views.registration'),
     url(r'^mynotes/register', 'myNotesBackend.views.register'),
     url(r'^mynotes/deletenote', 'myNotesBackend.views.delete_note'),
     url(r'^mynotes/filterbytag', 'myNotesBackend.views.filter_by_tag'),
     url(r'^mynotes/gettags', 'myNotesBackend.views.get_tags'),
     url(r'^mynotes/validateusername', 'myNotesBackend.views.validate_user'),
    # Uncomment the admin/doc line below to enable admin documentation:
    #url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    #url('', include('django.contrib.auth.urls')),
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
