from django.db import models

# Create your models here.
class Post(models.Model):
  title = models.CharField(max_length=100)
  published = models.DateTimeField()
  image = models.ImageField(upload_to='media/')
  #image = models.ImageField(upload_to='post_images/', blank=True, null=True)
  body = models.TextField()

  #日本語
  def __str__(self):
    return self.title

  def summary(self):
    return self.body[:100]
