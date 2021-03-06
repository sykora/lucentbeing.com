'''URL dispatch for lucentbeing.com.'''

from django.conf import settings
from django.conf.urls.defaults import *
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'lucentbeing.core.views.index', name='lucentbeing_index'),
    (r'^admin/', include(admin.site.urls)),
    (r'^blog/', include('djournal.urls')),
)

if settings.DEBUG :
    urlpatterns += patterns('',
        url(
            r'^{STATIC_URL}(?P<path>.*)$'.format(
                STATIC_URL = settings.STATIC_URL.lstrip('/')
            ),
            'django.views.static.serve',
            {'document_root' : settings.STATIC_ROOT, 'show_indexes' : True}
        ),
    )
