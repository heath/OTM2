from __future__ import print_function
from __future__ import unicode_literals
from __future__ import division

from django.conf.urls import patterns, include, url

from treemap.views import index, trees, tree_detail, settings

urlpatterns = patterns(
    '',
    url(r'^$', index),
    url(r'^trees/$', trees),
    url(r'^trees/(?P<tree_id>\d+)/$', tree_detail),
    url(r'^config/settings.js$', settings)
)