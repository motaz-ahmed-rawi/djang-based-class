from django.db import models

from django.contrib.auth.models import User as AuthUser

class Note(models.Model):
    title = models.TextField(null=True)
    content = models.TextField()
    user = models.ForeignKey(AuthUser, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    hashed_id = models.CharField(max_length=64, unique=True, null=True)
    status=models.ForeignKey("Status", null=True,on_delete=models.CASCADE)

    class Meta:
        verbose_name = ("Note")
        verbose_name_plural = ("Notes")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("Note_detail", kwargs={"pk": self.pk})


class Status(models.Model):
    status_text = models.TextField()

    

    class Meta:
        verbose_name = ("Status")
        verbose_name_plural = ("Statuss")

    def __str__(self):
        return self.status_text

    def get_absolute_url(self):
        return reverse("Status_detail", kwargs={"pk": self.pk})




