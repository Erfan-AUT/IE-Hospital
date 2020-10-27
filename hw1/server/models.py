from django.db import models

class ChatRoom(models.Model):
    name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name


class User(models.Model):
    username = models.CharField(max_length=8, unique=True)
    last_room = models.ForeignKey(ChatRoom, null=True, on_delete=models.SET_NULL)
    last_seen = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.username



class Message(models.Model):
    text = models.CharField(max_length=256)
    room = models.ForeignKey(ChatRoom, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now=True)

    def to_str(self):
        return str(self.timestamp) + " | " + self.user.username + ": " + self.text
