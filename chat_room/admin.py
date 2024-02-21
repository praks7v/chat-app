from django.contrib import admin
from .models import ChatRoom, Message

class MessageInline(admin.TabularInline):
    model = Message
    extra = 0

class ChatRoomAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    inlines = [MessageInline]

class MessageAdmin(admin.ModelAdmin):
    list_display = ('chatroom', 'user', 'content', 'date_added')
    list_filter = ('chatroom', 'user')

admin.site.register(ChatRoom, ChatRoomAdmin)
admin.site.register(Message, MessageAdmin)