from django.db import models

from django.contrib.auth.models import User as AuthUser

class Note(models.Model):
    title = models.TextField()
    content = models.TextField()
    user = models.ForeignKey(AuthUser, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    hashed_id = models.CharField(max_length=64, unique=True, null=True)

    class Meta:
        verbose_name = ("Note")
        verbose_name_plural = ("Notes")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("Note_detail", kwargs={"pk": self.pk})




