from django.db import models
from django.contrib.auth.models import User

class DocumentSession(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    session_key = models.CharField(max_length=40)
    file = models.FileField(upload_to='chat_docs/')
    pages = models.JSONField(default=list)
    created_at = models.DateTimeField(auto_now_add=True)

class ChatMessage(models.Model):
    session = models.ForeignKey(DocumentSession, on_delete=models.CASCADE)
    content = models.TextField()
    page_number = models.IntegerField(null=True)
    is_user = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)