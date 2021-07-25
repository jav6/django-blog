from django.db import models

class Post(models.Model):
    post_slug = models.SlugField(max_length=60)
    post_title = models.CharField(max_length=60)
    post_body = models.TextField()
    def __str__(self):
        return self.post_title

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author =  models.CharField(max_length=80)
    email = models.EmailField()
    text = models.TextField()
    def __str__(self):
        text = self.text
        return '{} - Author:{}'.format(text[0:10]+'...', self.author)
