from django.db import models
from django.utils.six import python_2_unicode_compatible

# Create your models here.


@python_2_unicode_compatible
class Topic(models.Model):
    """
    话题
    """
    content = models.CharField(max_length=200)

    created = models.DateTimeField(auto_now_add=True)

    user = models.ForeignKey('auth.User',related_name='topics_of', on_delete=models.CASCADE())





















