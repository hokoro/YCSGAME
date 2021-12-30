from django.conf.urls import url
from django.urls import path

from friendapp.views import FriendSearchView

app_name = 'friendapp'
urlpatterns = [
    path('search/?search=<str:username>',FriendSearchView.as_view(),name='search'),
    # path('request/(?P<username>[\w.@+-]+)',AddFriend.as_view(),name='request'),
]
