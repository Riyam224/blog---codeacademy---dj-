from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=100)
    title_tag = models.CharField(max_length=20)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    post_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title + ' | ' + str(self.author)

    # redirect page
    def get_absolute_url(self):
        return reverse('detail', args=(str(self.pk)))
        # return reverse('home')
