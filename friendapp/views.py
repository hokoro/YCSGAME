from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView
# Create your views here.
from rest_framework.views import APIView

from friendapp.models import Friend, Friend_request
from profileapp.models import Profile


@login_required
def send_friend_request(request, user_id):
    from_user = request.user
    to_user = User.objects.get(id=user_id)
    friend_request, created = Friend_request.objects.get_or_create(from_user=from_user, to_user=to_user)
    if created:
        return HttpResponse("friend request sent")
    else:
        return HttpResponse("friend request was already sent")


@login_required
def accept_friend_request(request, request_id):
    friend_request = Friend_request.objects.get(id=request_id)
    if friend_request.to_user == request.user:
        friend_request.to_user.friends.add(friend_request.from_user)
        friend_request.from_user.friends.add(friend_request.to_user)
        friend_request.delete()
        return HttpResponse("friend request accepted")
    else:
        return HttpResponse("friend request not accepted")


class FriendSearchView(ListView):
    model = Profile
    context_object_name = 'profile_search_result'
    template_name = 'friendapp/search.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        search_name = self.request.GET.get('profile_name', '')
        context['profile_search_result'] = Profile.objects.filter(nickname=search_name)
        return context


class FriendListView(ListView):
    model = Profile
    context_object_name = 'profile_friend_result'
    template_name = 'friendapp/list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        context['profile_friend_result'] = Friend.objects.filter(user_id=user)
        return context
