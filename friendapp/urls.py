
from django.urls import path

from friendapp import views
from friendapp.views import FriendSearchView, FriendListView, send_friend_request, accept_friend_request

app_name = 'friendapp'
urlpatterns = [
    path('search/?search=<str:username>',FriendSearchView.as_view(),name='search'),
    path('list/<int:pk>',FriendListView.as_view(),name='list'),
]
