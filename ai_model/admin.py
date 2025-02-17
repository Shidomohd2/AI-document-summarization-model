from django.contrib import admin
from .models import DocumentSession, ChatMessage

@admin.register(DocumentSession)
class DocumentSessionAdmin(admin.ModelAdmin):
    list_display = ('session_key', 'user', 'created_at')

@admin.register(ChatMessage)
class ChatMessageAdmin(admin.ModelAdmin):
    list_display = ('session', 'content', 'page_number', 'is_user', 'timestamp')