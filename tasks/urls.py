from rest_framework.routers import DefaultRouter
from .views import BoardViewSet, TaskViewSet, StatusViewSet, TaskHistoryViewSet
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.urls import path


schema_view = get_schema_view(
    openapi.Info(
        title="Task Tracking API",
        default_version='v1',
        description="Документация для API системы управления задачами",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

router = DefaultRouter()
router.register(r'boards', BoardViewSet)
router.register(r'tasks', TaskViewSet)
router.register(r'statuses', StatusViewSet)
router.register(r'task-history', TaskHistoryViewSet)

urlpatterns = router.urls
urlpatterns += [
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
