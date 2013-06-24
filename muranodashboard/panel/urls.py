#    Copyright (c) 2013 Mirantis, Inc.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

from django.conf.urls.defaults import patterns, url

from views import IndexView, Services, CreateEnvironmentView, DetailServiceView
from views import Wizard, EditEnvironmentView
from views import SERVICE_CHECKER
from forms import FORMS
from forms import SERVICE_NAMES


VIEW_MOD = 'openstack_dashboard.dashboards.project.murano.views'
ENVIRONMENT_ID = r'^(?P<environment_id>[^/]+)'

condition_dict_for_wizard = dict(zip(SERVICE_NAMES, SERVICE_CHECKER))


urlpatterns = patterns(
    VIEW_MOD,
    url(r'^environments$', IndexView.as_view(), name='index'),

    url(r'^create/$',
        Wizard.as_view(FORMS, condition_dict=condition_dict_for_wizard),
        name='create'),

    url(r'^create_environment/$', CreateEnvironmentView.as_view(),
        name='create_environment'),

    url(ENVIRONMENT_ID + r'/update_environment$',
        EditEnvironmentView.as_view(),
        name='update_environment'),

    url(ENVIRONMENT_ID + r'/services$', Services.as_view(),
        name='services'),

    url(ENVIRONMENT_ID + r'/(?P<service_id>[^/]+)/$',
        DetailServiceView.as_view(),
        name='service_details')
)
