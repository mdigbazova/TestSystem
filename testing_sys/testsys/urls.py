from django.urls import path, re_path, include

from . import views


urlpatterns = [
    path('rest-auth/', include('rest_auth.urls')),
    path('register/', views.RegisterUser.as_view(), name='register'),
    path('api-auth/', include('rest_framework.urls')),
    re_path('^alerts-bodies/$', views.AlertsBodiesList.as_view(), name="alerts-bodies"),
    re_path('^accounts/$', views.AccountsList.as_view(), name="accounts"),
    re_path('^agents/$', views.AgentsList.as_view(), name="agents"),
    re_path('^comments/$', views.CommentsList.as_view(), name="comments"),
    re_path('^alerts-bodies/(?P<alerts_body_id>\d+)/$', views.AlertsBodyDetails.as_view(), name="alerts-body-details"),
    re_path('^accounts/(?P<account_id>\d+)/$', views.AccountDetails.as_view(), name="account-details"),
    re_path ('^agents/(?P<agent_id>\d+)/$', views.AgentDetails.as_view (), name="agent-details"),
    #re_path ('^comments/(?P<comment_id>\d+)/$', views.CommentDetails.as_view(), name="comment-details"),
    #re_path('^users/comments/$', views.UserList.as_view(), name='user-details'),
    re_path ('^alerts-bodies/(?P<alerts_body_id>\d+)/comments/(?P<comment_id>\d+)/$', views.CommentDetails.as_view(), name="comment-details"),
]
