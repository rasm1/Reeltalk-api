from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

class Post(models.Model):
    """
    Post model, related to 'owner', i.e. a User instance.
    Default image set so that we can always reference image.url.
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    movie_title = models.CharField(max_length=255)
    image = CloudinaryField('images/')
    
    movie_spoilers = models.BooleanField(
        verbose_name='Does this post contain spoilers?', default=False)
    movie_positives = models.CharField(max_length=255, blank=True, null=True)
    movie_negatives = models.CharField(max_length=255, blank=True, null=True)
    
    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.id} {self.title}'