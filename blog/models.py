from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    #categories = models.ManyToManyField('Category', related_name='posts')
    categories = models.ForeignKey('Category', on_delete=models.CASCADE)
    memmo = models.TextField(blank=True)

    def __str__(self):
        return f"{self.title} {self.body} {self.created_on} {self.last_modified} {self.categories} {self.memmo}"


class Comment(models.Model):
    author = models.CharField(max_length=60)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey('Post', on_delete=models.CASCADE, related_name="comments")


class Headliner(models.Model):
    name = models.CharField(max_length=20)
    adr = models.URLField(max_length=60)


class Contacts(models.Model):
    name = models.CharField(max_length=60)
    email = models.CharField(max_length=60)
    phone = models.IntegerField()

    def __str__(self):
        return f"{self.name} {self.email} {self.phone}"
