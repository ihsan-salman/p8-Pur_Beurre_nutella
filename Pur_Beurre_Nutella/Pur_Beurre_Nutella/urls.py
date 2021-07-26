"""Pur_Beurre_Nutella URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path
from django.contrib.auth.views import LogoutView

from mes_aliments import views


handler404 = 'mes_aliments.views.page_not_found'
hander500 = 'mes_aliments.views.server_error'

urlpatterns = [
    url(r'^$', views.index, name='home'),
    url(r'^mes_substituts/', views.product, name='find_substitute'),
    url(r'^mon_compte/', views.my_account, name='mon_compte'),
    url(r'^mes_favoris/', views.my_favorite, name='my_favorite'),
    url(r'^mon_produit/(?P<pk>\d+)/$', views.detail_product,
        name='my_product'),
    url(r'^create/', views.create, name='create'),
    path('login/', views.CustomLoginView.as_view(), name='login'),
    url(r'^logout/$', LogoutView.as_view(), {'next_page':
        settings.LOGOUT_REDIRECT_URL}, name='logout'),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
