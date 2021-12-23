#폼 형식을 변경하기 위해
from django.contrib.auth.forms import UserCreationForm


class AccountCreationForm(UserCreationForm): #usercreation form 상속
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs) #부모 에 초기화 접근하기 위해 super 사용

        self.fields['username'].disabled = True  #사용자 id 칸을 False 로 변경
        '''
        update 에서 id 를 못쓰게 만드는 새로운 폼을 만들었다.
        '''