from django.conf.urls import patterns, include, url
from tastypie.api import Api
from spotmanager.api import EntryResource, UserResource

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

v1_api = Api(api_name='v1')
v1_api.register(UserResource())
v1_api.register(EntryResource())

#from myapp.api import EntryResource
#entry_resource = EntryResource()

urlpatterns = patterns('',
    (r'^location/', include('spotmanager.urls')),
    (r'^api/', include(v1_api.urls)),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
