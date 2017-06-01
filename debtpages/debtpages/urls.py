"""debtpages URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
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
from debtpages_rest import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^debts/$', views.DebtList.as_view()),
    url(r'^debts/(?P<pk>[0-9]+)/$', views.DebtDetail.as_view()),
    url(r'^users/$', views.UserList.as_view()),
    url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
    url(r'^usersum/$', views.UserSumList.as_view()),
    url(r'^usersum/(?P<pk>[0-9]+)/$', views.UserSumDetail.as_view()),
    url(r'^api-auth/', include('rest_framework.urls',
        namespace='rest_framework')),
]
