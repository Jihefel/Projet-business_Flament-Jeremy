from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField()
    image = models.CharField(max_length=100)

    class Meta:
        db_table = 'articles'

    def __str__(self):
        return self.title


class Project(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    image = models.CharField(max_length=100)

    class Meta:
        db_table = 'projects'

    def __str__(self):
        return self.title
