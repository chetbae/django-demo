from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100)
    post_text = models.TextField()
    topic = models.CharField(max_length=20)
    public = models.BooleanField()

    def __str__(self) -> str:
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment_text = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.comment_text

