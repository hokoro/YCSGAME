from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView


class AccountCreateView(CreateView):
    model = User  # 모델 지정  = User(장고에서 지정 해주는 모델 계정에 관한 정보가 들어있음)
    form_class = UserCreationForm  # 장고에서 제공하는 사용자 계정 form
    success_url = reverse_lazy('accountapp:login')
    template_name = 'accountapp/create.html'