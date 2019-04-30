from django.urls import path, re_path, include
from . import views

urlpatterns = [
    path('rest-auth/', include('rest_auth.urls')),
    re_path('^AlertBodies/$', views.AlertBodiesList.as_view(), name = "AlertBodies")
]
