#
# BitBake Toaster Implementation
#
# Copyright (C) 2013        Intel Corporation
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 2 as
# published by the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

from django.conf.urls import patterns, include, url
from django.views.generic.simple import redirect_to

urlpatterns = patterns('bldviewer.views',
        url(r'^builds/$', 'build', name='all-builds'),
        url(r'^build/(?P<build_id>\d+)/task/$', 'task', name='task'),
        url(r'^build/(?P<build_id>\d+)/packages/$', 'bpackage', name='bpackage'),
        url(r'^build/(?P<build_id>\d+)/package/(?P<package_id>\d+)/files/$', 'bfile', name='bfile'),
        url(r'^build/(?P<build_id>\d+)/target/(?P<target_id>\d+)/packages/$', 'tpackage', name='tpackage'),
        url(r'^build/(?P<build_id>\d+)/configuration/$', 'configuration', name='configuration'),
        url(r'^layers/$', 'layer', name='all-layers'),
        url(r'^layerversions/(?P<layerversion_id>\d+)/recipes/.*$', 'layer_versions_recipes', name='layer_versions_recipes'),
        url(r'^$', redirect_to, {'url': 'builds/'}),
)
