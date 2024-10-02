from rest_framework.routers import DefaultRouter
from .views import BoardViewSet, TaskViewSet, StatusViewSet, TaskHistoryViewSet

router = DefaultRouter()
router.register(r'boards', BoardViewSet)
router.register(r'tasks', TaskViewSet)
router.register(r'statuses', StatusViewSet)
router.register(r'task-history', TaskHistoryViewSet)

urlpatterns = router.urls
