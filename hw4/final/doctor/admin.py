from django.contrib import admin
from .models import Doctor, Spec, Comment, BaseUser
# Register your models here.
admin.site.register(Doctor)
admin.site.register(Spec)
admin.site.register(Comment)
admin.site.register(BaseUser)