from django.db import models

# Add Post table in database - to save post data
class Post(models.Model):
    post_slug = models.SlugField(max_length=60)
    post_title = models.CharField(max_length=60)
    post_body = models.TextField()
    def __str__(self):
        return self.post_title

# Add Comment table in database for save comment to database and set a post
# primary_key for it - to get comment for special post
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author =  models.CharField(max_length=80)
    email = models.EmailField()
    text = models.TextField()
    def __str__(self):
        text = self.text
        return '{} - Author:{}'.format(text[0:10]+'...', self.author)
