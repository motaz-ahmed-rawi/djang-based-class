from django.db import models

# Create your models here.

class User(models.Model):
    name=models.CharField(max_length=10)
    last_name=models.CharField(max_length=10,null=True,blank=True)
    email = models.EmailField()
    password = models.CharField(max_length=256)
    

    class Meta:
        verbose_name = ("user")
        verbose_name_plural = ("users")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("user_detail", kwargs={"pk": self.pk})

class Note(models.Model):
    title=models.TextField()
    content=models.TextField()
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    date=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    hashed_id = models.CharField(max_length=64, unique=True,null=True)


    

    class Meta:
        verbose_name = ("Note")
        verbose_name_plural = ("Notes")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("Note_detail", kwargs={"pk": self.pk})







