from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy, reverse
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from accountapp.forms import AccountCreationForm
from accountapp.decorators import account_ownership_required


class AccountCreateView(CreateView):
    model = User  # 모델 지정  = User(장고에서 지정 해주는 모델 계정에 관한 정보가 들어있음)
    form_class = UserCreationForm  # 장고에서 제공하는 사용자 계정 form
    success_url = reverse_lazy('accountapp:login')
    template_name = 'accountapp/create.html'


class AccountDetailView(DetailView):
    model = User
    context_object_name = 'target_user'
    template_name = 'accountapp/detail.html'


has_ownership = [login_required, account_ownership_required]


@method_decorator(has_ownership, 'get')  # 메소드에서 데코레이터를 적용한다 (적용할 데토레이터를 가져와야 한다,어떤 방식의 메소드 를 접근 할지)
@method_decorator(has_ownership, 'post')  # 애초에 클래스 메소드에서 데코레이터를 작동할수 있는 시스템을 만들어야 한다.
class AccountUpdateView(UpdateView):
    model = User
    form_class = AccountCreationForm
    template_name = 'accountapp/update.html'

    success_url = reverse_lazy('mainapp:mainpage')
    # def get_success_url(self):
    # return reverse('accountapp:detail', kwargs={'pk': self.object.pk})


@method_decorator(has_ownership, 'get')  # 메소드에서 데코레이터를 적용한다 (적용할 데토레이터를 가져와야 한다,어떤 방식의 메소드 를 접근 할지)
@method_decorator(has_ownership, 'post')  # 애초에 클래스 메소드에서 데코레이터를 작동할수 있는 시스템을 만들어야 한다.
class AccountDeleteView(DeleteView):
    model = User
    context_object_name = 'target_user'
    success_url = reverse_lazy('mainapp:mainpage')
    template_name = 'accountapp/delete.html'
