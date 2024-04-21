from django.db import models

# Create your models here.
class Post(models.Model):
    title=models.CharField( max_length=50)
    content=models.TextField(max_length=2000)
    created_at=models.DateTimeField(auto_now_add=True,null=False)
    updated_at = models.DateTimeField(auto_now=True, null=False)
    models.ImageField(upload_to='post-img/')

    

    class Meta:
        verbose_name = ("post")
        verbose_name_plural = ("posts")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"pk": self.pk})

