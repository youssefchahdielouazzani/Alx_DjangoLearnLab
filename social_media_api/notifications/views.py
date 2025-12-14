from django.http import JsonResponse
from .models import Notification

def notification_list(request):
    notifications = Notification.objects.all()
    return JsonResponse({'notifications': notifications.count()})

