"""
    Open Orchestrator Cloud Radio Access Network

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.

"""

from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views
from django.views.static import serve
from operators.forms import LoginForm
from operators.views import home

import settings

urlpatterns = [
    url(r'^operators/', include("operators.urls", namespace='operators')),
    url(r'^vnfs/', include("vnfs.urls", namespace='vnfs')),
    url(r'^scripts/', include("scripts.urls", namespace='scripts')),
    url(r'^images/', include("images.urls", namespace='images')),
    url(r'^scenarios/', include("scenarios.urls", namespace='scenarios')),
    url(r'^ns/', include("ns.urls", namespace='ns')),
    url(r'^ues/', include("ues.urls", namespace='ues')),
    url(r'^pools/', include("pools.urls", namespace='pools')),
    url(r'^vims/', include("vims.urls", namespace='vims')),
    url(r'^schedulers/', include("schedulers.urls", namespace='schedulers')),
    url(r'^keys/', include("keys.urls", namespace='keys')),
    url(r'^alerts/', include("alerts.urls", namespace='alerts')),
    url(r'^bbus/', include("bbus.urls", namespace='bbus')),
    url(r'^admin/', admin.site.urls),
    url(r'^$', home, name="home"),


    url(r'^login/$', views.login, {'template_name': 'base/login.html', 'authentication_form': LoginForm}, name='login'),
    url(r'^logout/$', views.logout, {'next_page': '/'}, name='logout'),
    url(r'^resources/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
]