from django.contrib import admin

from .models import Board, Task, TaskHistory, Status

admin.site.register(Board)
admin.site.register(Status)
admin.site.register(Task)
admin.site.register(TaskHistory)
