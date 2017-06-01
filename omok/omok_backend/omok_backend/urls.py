"""omok_backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from back import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^rooms/$', views.RoomList.as_view()),
    url(r'^rooms/(?P<pk>[0-9]+)/$', views.RoomDetail.as_view()),
    url(r'^rooms/(?P<pk>[0-9]+)/history/$', views.HistoryList),
    url(r'^rooms/(?P<pk>[0-9]+)/players/$', views.room_players_list),
    url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
    url(r'^api-auth/', include('rest_framework.urls',
        namespace='rest_framework')),
]
