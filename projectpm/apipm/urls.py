from django.conf.urls import url
from apipm import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[
    url(r'^api/v1/meters$',views.apimsr),
    url(r'^api/v1/meters/([0-9]+)$',views.apimsr),

    url(r'^api/v1/addmtr$',views.apimsradd),
    url(r'^api/v1/addmtr/',views.apimsradd),

    url(r'^api/v1/sendmtr$',views.apimsrsend),
    url(r'^api/v1/sendmtr/',views.apimsrsend),

    url(r'^api/v1/datacon$',views.apidatacon),
    url(r'^api/v1/datacon/([0-9]+)$',views.apidatacon),

    url(r'^api/v1/maxcon$',views.apimaxcon),
    url(r'^api/v1/maxcon/([0-9]+)$',views.apimaxcon),

    url(r'^api/v1/mincon$',views.apimincon),
    url(r'^api/v1/mincon/([0-9]+)$',views.apimincon),

    url(r'^api/v1/avgcon$',views.apiavgcon),
    url(r'^api/v1/avgcon/([0-9]+)$',views.apiavgcon),

    url(r'^api/v1/totcon$',views.apitotcon),
    url(r'^api/v1/totcon/([0-9]+)$',views.apitotcon)

]
