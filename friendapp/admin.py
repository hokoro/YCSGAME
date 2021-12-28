from django.contrib import admin

# Register your models here.

from friendapp.models import FriendRequest, FriendList


# 친구 목록 관리자
class FriendListAdmin(admin.ModelAdmin):
    list_filter = ['user']
    list_display = ['user']
    search_fields = ['user']
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
