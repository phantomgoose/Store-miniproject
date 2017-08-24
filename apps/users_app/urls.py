from django.conf.urls import url
from .views import UsersIndex, UsersLogin, UsersRedirect, UsersLogout

urlpatterns = [
    url(r'^login$', UsersLogin.as_view(), name='users-login'),
    url(r'^logout$', UsersLogout.as_view(), name='users-logout'),
    url(r'^$', UsersIndex.as_view(), name='users-index'),
    url(r'^', UsersRedirect.as_view(), name='users-redirect'),
]