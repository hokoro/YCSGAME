from django.contrib import admin

# Register your models here.

from friendapp.models import FriendRequest, FriendList


# 친구 목록 관리자
class FriendListAdmin(admin.ModelAdmin):
    list_filter = ['user'] #관리자 사이드 바 오른쪽 활성화
    list_display = ['user'] #관리자 의 변경 목록 페이지에 표시 되는 부분을 표출
    search_fields = ['user'] #변경 목록 페이지의 검색 기능 활성화
    readonly_fields = ['user']

    class Meta:
        model = FriendList


admin.site.register(FriendList, FriendListAdmin)


# 친구 요청 관리자
class FriendRequestAdmin(admin.ModelAdmin):
    list_filter = ['sender', 'receiver']
    list_display = ['sender', 'receiver']
    search_fields = ['sender__username','sender__email', 'receiver__email','receiver__username']

    class Meta:
        model = FriendRequest


admin.site.register(FriendRequest,FriendRequestAdmin)
