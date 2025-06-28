from django.test import TestCase
from django.urls import reverse
from .models import Todo
from datetime import date


# Create your tests here.
class Test(TestCase):
    def test_post_todo_create_creates_object(self):
        data = {
            "title": "Aprender Django",
            "description": "Crear una app de tareas",
            "due_date": date.today().isoformat(),  # formato YYYY-MM-DD
            "completed": False,
        }
        response = self.client.post(reverse("todo_create"), data)

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("todo_list"))
        self.assertEqual(Todo.objects.count(), 1)
        self.assertEqual(Todo.objects.first().title, "Aprender Django")
