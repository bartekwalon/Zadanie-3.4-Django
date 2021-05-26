from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    author_id = models.ForeignKey(
        'posts.Author',
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    def __str__(self):
        return f"title: {self.title}, content: {self.content}, created: {self.created}, modified: {self.modified}," \
               f"author_id: {self.author_id}"


class Author(models.Model):
    nick = models.CharField(max_length=20, unique=True)
    email = models.EmailField(unique=True)
    bio = models.TextField(max_length=500, blank=True, null=True)

    def __str__(self):
        return f"nick: {self.nick}, email: {self.email}, bio: {self.bio}"

