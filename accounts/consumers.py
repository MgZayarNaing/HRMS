import json
from channels.generic.websocket import WebsocketConsumer
from django.utils import timezone
from .models import CustomUser

class UserActivityConsumer(WebsocketConsumer):
    def connect(self):
        if self.scope["user"].is_authenticated:
            self.user = self.scope["user"]
            self.accept()
            self.send_user_status()
        else:
            self.close(code=4001)

    def disconnect(self, close_code):
        if hasattr(self, 'user'):
            self.user.update_last_logout_time()

    def receive(self, text_data):
        if hasattr(self, 'user'):
            self.user.update_last_activity_time()
            self.send_user_status()

    def send_user_status(self):
        users = CustomUser.objects.all()
        user_status = {}
        for user in users:
            user_status[user.id] = self.is_user_online(user)
        self.send(text_data=json.dumps(user_status))

    def is_user_online(self, user, interval_minutes=5):
        now = timezone.now()
        if user.last_activity and now - user.last_activity <= timezone.timedelta(minutes=interval_minutes):
            return True
        return False
