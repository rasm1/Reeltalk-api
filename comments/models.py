from django.db import models
from django.contrib.auth.models import User
from posts.models import Post


class Comment(models.Model):
    """
    Comment model, related to User and Post
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    content = models.TextField()
    movie_spoilers = models.BooleanField(
        verbose_name='Does this post contain spoilers?', default=False)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.content
