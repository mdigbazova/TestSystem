from django.urls import path, re_path, include
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.schemas import get_schema_view

from . import views

from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='Pastebin API')
#schema_view = get_schema_view(title='Pastebin API')

urlpatterns = [
    re_path('^schema/', schema_view),
    re_path('^register/', views.RegisterUser.as_view(), name='register'), #register functionality
    re_path('^alerts-bodies/$', views.AlertsBodiesList.as_view(), name="alerts-bodies"),
    re_path('^accounts/$', views.AccountsList.as_view(), name="accounts"),
    re_path('^agents/$', views.AgentsList.as_view(), name="agents"),
    re_path('^comments/$', views.CommentsList.as_view(), name="comments"),
    re_path('^alerts-bodies/(?P<pk>\d+)/$', views.AlertsBodyDetails.as_view(), name="alerts-body-details"),
    re_path('^accounts/(?P<pk>\d+)/$', views.AccountDetails.as_view(), name="account-details"),
    re_path('^agents/(?P<pk>\d+)/$', views.AgentDetails.as_view(), name="agent-details"),
    re_path('^alerts-bodies/(?P<pk>\d+)/comments/(?P<comment_id>\d+)/$', views.CommentDetails.as_view(), name="comment-details"),
    path('', views.api_root),
]

urlpatterns = format_suffix_patterns(urlpatterns)
