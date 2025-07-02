from django.db import models
from ckeditor.fields import RichTextField
from .utils import resize_image
from django.db import models
from datetime import date

from parler.models import TranslatableModel, TranslatedFields

# Create your models here.

class Todo(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    due_date = models.DateField()
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class Newsfeed(TranslatableModel):
    translations = TranslatedFields(
         title = models.CharField(verbose_name="Título", max_length=200),
        description = RichTextField(verbose_name="Contenido", blank=True, null=True)
    )

    cover_img = models.ImageField(verbose_name="Imagen de Portada", null=True, blank=True, upload_to="newsfeed/images/")
    date = models.DateField(verbose_name="Fecha", default=date.today)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    def save(self, *args, **kwargs):
        if self.cover_img and hasattr(self.cover_img, 'file') and not self._state.adding:
            # Solo redimensionar si la imagen es nueva (no redimensionar cada vez)
            if not self.pk:
                # Es un nuevo objeto
                self.cover_img = resize_image(self.cover_img, max_width=500)
            else:
                old = type(self).objects.get(pk=self.pk)
                if old.cover_img != self.cover_img:
                    self.cover_img = resize_image(self.cover_img, max_width=500)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Newsfeed"
        verbose_name_plural = "Newsfeed"

    def __str__(self):
        return self.safe_translation_getter('title', any_language=True) or " "