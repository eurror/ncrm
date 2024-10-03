from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse


class TaskAPITests(APITestCase):
    def test_create_task(self):
        url = reverse('task-list')
        data = {'title': 'New Task', 'status': 1, 'priority': 'high'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_task_list(self):
        url = reverse('task-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
