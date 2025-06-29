from django.test import TestCase
from django.urls import reverse
from .models import Todo
from datetime import date


# Create your tests here.
class Test(TestCase):

    def setUp(self):
        self.todo = Todo.objects.create(
            title="Tarea de prueba",
            description="Descripción de prueba",
            due_date=date.today(),
            completed=False,
        )

    def test_get_delete_view(self):
        url = reverse("todo_delete", args=[self.todo.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Tarea de prueba")

    def test_post_delete_view(self):
        url = reverse("todo_delete", args=[self.todo.pk])
        response = self.client.post(url)

        # Verifica redirección
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("todo_list"))

        # Verifica que se haya eliminado
        self.assertFalse(Todo.objects.filter(pk=self.todo.pk).exists())
