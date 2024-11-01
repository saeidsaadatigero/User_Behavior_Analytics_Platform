# tracking/views.py
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import UserBehavior
from .serializers import UserBehaviorSerializer

class UserBehaviorViewSet(viewsets.ModelViewSet):
    queryset = UserBehavior.objects.all()
    serializer_class = UserBehaviorSerializer

    @action(detail=False, methods=['get'])
    def recent_activity(self, request):
        """ دریافت آخرین فعالیت کاربران """
        recent = UserBehavior.objects.order_by('-timestamp')[:10]
        serializer = self.get_serializer(recent, many=True)
        return Response(serializer.data)
