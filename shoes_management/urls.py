from django.conf.urls import url

from . import views

urlpatterns = [
    #url(r'^$', RedirectView.as_view(url='/accounts/login', permanent=True)),
    url(r'^ventas/$', views.solds, name='ventas'),
    url(r'^ventas/(?P<pk>\d+)$', views.soldItems, name='bill-detail'),
]
