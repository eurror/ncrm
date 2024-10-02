from django.db import models
from django.contrib.auth.models import User


class Board(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Status(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Task(models.Model):
    board = models.ForeignKey(
        Board, related_name='tasks', on_delete=models.CASCADE
    )
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    status = models.ForeignKey(
        Status, on_delete=models.SET_NULL, null=True)
    assigned_to = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True
    )
    priority = models.IntegerField(default=1)
    due_date = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def can_change_status(self, new_status):
        status_order = ['To Do', 'In Progress', 'Done']
        current_index = status_order.index(self.status.name)
        new_index = status_order.index(new_status.name)

        return new_index >= current_index

    def __str__(self):
        return self.title


class TaskHistory(models.Model):
    task = models.ForeignKey(
        Task, related_name='history', on_delete=models.CASCADE)
    old_status = models.ForeignKey(
        Status, related_name='old_statuses', on_delete=models.SET_NULL, null=True)
    new_status = models.ForeignKey(
        Status, related_name='new_statuses', on_delete=models.SET_NULL, null=True)
    changed_at = models.DateTimeField(auto_now_add=True)
    changed_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"Task '{self.task.title}' changed from {self.old_status} to {self.new_status}"
