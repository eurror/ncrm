from rest_framework.exceptions import PermissionDenied
from rest_framework.response import Response
from rest_framework import status as drf_status
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend

from .models import Board, Task, Status, TaskHistory
from .serializers import BoardSerializer, TaskSerializer, StatusSerializer, TaskHistorySerializer
from .tasks import send_status_change_notification


class BoardViewSet(viewsets.ModelViewSet):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer
    permission_classes = [IsAuthenticated]


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['status', 'created_at', 'priority']

    def update(self, request, *args, **kwargs):
        task = self.get_object()
        new_status_id = request.data.get('status')

        if task.assigned_to != request.user:
            raise PermissionDenied("Вы не можете изменять статус этой задачи.")

        if new_status_id and str(task.status.id) != new_status_id:
            new_status = Status.objects.get(id=new_status_id)

            if not task.can_change_status(new_status):
                return Response({'detail': 'Нельзя изменить статус задачи на выбранный.'},
                                status=drf_status.HTTP_400_BAD_REQUEST)

            old_status = task.status

            response = super().update(request, *args, **kwargs)

            TaskHistory.objects.create(
                task=task,
                old_status=old_status,
                new_status=new_status,
                changed_by=request.user
            )
            send_status_change_notification.delay(
                task.title, task.status.name, task.assigned_to.email)

            return response
        else:
            return Response({'detail': 'Статус задачи не изменился.'}, status=drf_status.HTTP_400_BAD_REQUEST)

class StatusViewSet(viewsets.ModelViewSet):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer
    permission_classes = [IsAuthenticated]


class TaskHistoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = TaskHistory.objects.all()
    serializer_class = TaskHistorySerializer
    permission_classes = [IsAuthenticated]
