from django.utils.deprecation import MiddlewareMixin
from django.utils import timezone
from datetime import timedelta

class TrackUserActivityMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if request.user.is_authenticated:
            user = request.user
            user.update_last_activity_time()

    def process_response(self, request, response):
        return response

def get_user_online_status(user, interval_minutes=5):
    now = timezone.now()
    if user.last_activity and now - user.last_activity <= timedelta(minutes=interval_minutes):
        return True
    return False
