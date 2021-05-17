from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    """Model definition for Post."""
    title = models.CharField(max_length=100)
    URL = models.URLField(max_length=200)
    poster = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField( auto_now=False, auto_now_add=True)

    class Meta:
        """Meta definition for Post."""
        ordering = ['-created']

        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def __str__(self):
        """Unicode representation of Post."""
        return '{}'.format(self.title)
        

class Vote(models.Model):
    """Model definition for Vote."""
    voter = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="post_votes")


    class Meta:
        """Meta definition for Vote."""

        verbose_name = 'Vote'
        verbose_name_plural = 'Votes'

    def __str__(self):
        """Unicode representation of Vote."""
        return '{} - {}'.format(self.voter, self.post)
        
