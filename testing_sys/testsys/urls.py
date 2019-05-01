from django.urls import path, re_path, include
from . import views

urlpatterns = [
    path('rest-auth/', include('rest_auth.urls')),
    re_path('^alerts-bodies/$', views.AlertsBodiesList.as_view(), name="alerts-bodies"),
    re_path('^accounts/$', views.AccountsList.as_view(), name="accounts"),
    re_path('^agents/$', views.AgentsList.as_view(), name="agents"),
    re_path('^alerts-bodies/(?P<alerts_body_id>\d+)/$', views.AlertsBodyDetails.as_view(), name="alerts-body-details"),
    re_path('^accounts/(?P<account_id>\d+)/$', views.AccountDetails.as_view(), name="account-details"),
    re_path ('^agents/(?P<agent_id>\d+)/$', views.AgentDetails.as_view (), name="agent-details"),

]
