from django.contrib import admin

from server.models import User, Message, ChatRoom

admin.site.register(User)
admin.site.register(Message)
admin.site.register(ChatRoom)
