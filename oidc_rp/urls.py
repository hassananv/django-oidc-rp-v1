"""
    OpenID Connect relying party (RP) URLs
    ======================================

    This modules defines the URLs allowing to perform OpenID Connect flows on a Relying Party (RP).
    It defines three main endpoints: the authentication request endpoint, the authentication
    callback endpoint and the end session endpoint.

"""

from django.urls import re_path

from . import views


urlpatterns = [
    re_path(r'^auth/request/$', views.OIDCAuthRequestView.as_view(), name='oidc_auth_request'),
    re_path(r'^auth/cb/$', views.OIDCAuthCallbackView.as_view(), name='oidc_auth_callback'),
    re_path(r'^end-session/$', views.OIDCEndSessionView.as_view(), name='oidc_end_session'),
]
