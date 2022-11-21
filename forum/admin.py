from django.contrib import admin
from .models import Comment, Topic, MainTopic

# Register your models here.
admin.site.register(MainTopic)
admin.site.register(Topic)
admin.site.register(Comment)
