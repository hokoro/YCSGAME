from django.contrib.auth.models import User
from django.views.generic.detail import SingleObjectMixin, DetailView
from django.views.generic.list import MultipleObjectMixin
from rest_framework.views import APIView
from django.shortcuts import render
from django.views.generic import ListView
# Create your views here.
from friendapp.models import Friend
from profileapp.models import Profile


class FriendSearchView(ListView):
    model = Profile
    context_object_name = 'profile_search_result'
    template_name = 'friendapp/search.html'

    def get_context_data(self,  **kwargs):
        context = super().get_context_data(**kwargs)
        user_name = self.request.GET.get('profile_name','')
        context['profile_search_result'] = Profile.objects.filter(nickname=user_name)
        return context

# class FriendRequestView(APIView):
#     def get(self, request, username):
#         friend = User.objects.get(username=username)
#         current_user = request.user.username
#         f = Friend(friend_A=current_user, friend_B=friend, friend_status=1)
#         f.save()
