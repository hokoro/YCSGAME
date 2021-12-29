from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.

# 유저 한명당 하나의 친구 목록 모델 만들기
class FriendList(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user') #User = 웹사이트 계정에 모든 정보를 담고 있고 그것과 연결 할려고 1대1 필드를 사용

    friends = models.ManyToManyField(User, blank=True, related_name='friends')

    def __str__(self):
        return self.user.username

    def add_friend(self, account):
        # 친구 관계가 성립이 안될경우만 추가를 하는 구조
        if not account in self.friends.all():
            self.friends.add(account)

    def remove_friend(self, account):
        # 친구 관계 가 성립이 될때만 친구 제거 기능이 발동 해야함
        if account in self.friends.all():
            self.friends.remove(account)

    # remover = 제거를 하는 사람 removee = 제거를 당한 사람
    def unfriend(self, removee):
        # 친구 관계 였다가 친구를 끊는 과정

        remover_friend_list = self  # 관계를 끊은 사람

        # remover 가  친구 목록에서 친구 제거
        remover_friend_list.remove_friend(removee)

        # removee 가 친구 목록에서 친구 제거 = 양쪽 관계를 모두 끊어야 하기 떄문에

        # 1.removee 에 친구 목록 조회
        friend_list = FriendList.objects.get(user=removee)
        friend_list.remove_friend(self.user)

    # 상호 친구관계를 확인 하는 함수
    def is_mutual_friend(self, friend):

        # 친구 관계 여부 확인
        if friend in self.friends.all():
            return True
        return False


# 친구 요청 모델 만들기
class FriendRequest(models.Model):
    """
    친구 요청 모델의 핵심 파라미터 는
    1. Sender = 친구 요청 을 보내는 사람
    2. Receiver = 친구 요청 을 받는 사람
    """

    # 한명의 발신자 가 잠재적으로 여러명에게  보낼수 있으므로 외래 키로 작성  = 일대다 관계 를 성립 된다.
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sender')
    # 수신자
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='recevier')

    # 친구 요청 활성화 여부 True 일때만 친구 요청 가능
    is_active = models.BooleanField(blank=True, null=False, default=True)

    # 계정이 생성 되고 최초 저장시 time 을 기록 = 친구 요청 이 이루어진 시간
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.sender.username

    def accept(self):
        """
        친구 요청이 받아 들여지고 있는 상황
        이떄 친구 요청이 받아 들여지면 수신자와 발신자가 둘다 친구 목록이 업데이트 되어야 한다.
        """
        # 수신자 의 친구 목록 리스트
        recevier_friend_list = FriendList.objects.get(user=self.receiver)

        # 수신자 의 친구 목록이 있는 지 확인 한 다음 수행
        if recevier_friend_list:
            recevier_friend_list.add_friend(self.sender)
            sender_friend_list = FriendList.objects.get(user=self.sender)
            # 발신자 리스트 가 존재 하면 수신자를 발신자 친구 목록 에 추가 하여 업데이트
            if sender_friend_list:
                sender_friend_list.add_friend(self.receiver)
                # 친구 관계가 성립 이 되면 더이상 친구 요청을 보낼수 없기 때문에
                self.is_active = False
                self.save()

    def decline(self):
        """
        친구 신청을 거절 하는 함수
        거절 하는 구조는 is_active 를 False 로 바꾸고  거절
        """
        self.is_active = False
        self.save()

    def cancel(self):
        """
        친구 신청을 취소 하는 함수
        마찬가지로 is active 를 False 로 바꾸는구조
        취소와 거절이 차이가 없지만 알림 시스템을 만들면 차이가 발생한다.
        """
        self.is_active = False
        self.save()


