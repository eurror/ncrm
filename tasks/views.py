from .models import TaskHistory, Status
from rest_framework.exceptions import PermissionDenied
from rest_framework.response import Response
from rest_framework import status as drf_status
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Board, Task, Status, TaskHistory
from .serializers import BoardSerializer, TaskSerializer, StatusSerializer, TaskHistorySerializer


class BoardViewSet(viewsets.ModelViewSet):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer
    permission_classes = [IsAuthenticated]


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    def update(self, request, *args, **kwargs):
        task = self.get_object()
        new_status_id = request.data.get('status')

        # Проверяем, что текущий пользователь назначен на задачу
        if task.assigned_to != request.user:
            raise PermissionDenied("Вы не можете изменять статус этой задачи.")

        # Проверяем, что новый статус отличается от текущего
        if new_status_id and str(task.status.id) != new_status_id:
            new_status = Status.objects.get(id=new_status_id)

            # Проверяем, можно ли изменить статус на новый (с учетом последовательности)
            if not task.can_change_status(new_status):
                return Response({'detail': 'Нельзя изменить статус задачи на выбранный.'},
                                status=drf_status.HTTP_400_BAD_REQUEST)

            # Получаем старый статус для сохранения в истории
            old_status = task.status

            # Обновляем статус задачи
            response = super().update(request, *args, **kwargs)

            # Сохраняем изменения в TaskHistory
            TaskHistory.objects.create(
                task=task,
                old_status=old_status,
                new_status=new_status,
                changed_by=request.user
            )

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
