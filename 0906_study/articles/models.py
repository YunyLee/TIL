from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=10) # 길이제한 필수인자
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

