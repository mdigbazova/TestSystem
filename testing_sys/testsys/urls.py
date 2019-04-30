from django.urls import path, re_path, include
from . import views

urlpatterns = [
    path('rest-auth/', include('rest_auth.urls')),
    re_path('^alerts-bodies/$', views.AlertsBodiesList.as_view(), name="alerts_bodies"),
    re_path('^accounts/$', views.AccountsList.as_view(), name="accounts"),
    re_path('^agents/$', views.AgentsList.as_view(), name="agents"),

]
