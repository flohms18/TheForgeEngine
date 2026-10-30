from django.db import models
from tinymce.models import HTMLField

# Create your models here.


class Tag (models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(unique=True)

    def __str__(self):
            return self.name

class Post(models.Model):
    title = models.CharField(max_length=300,null=False)
    slug = models.SlugField(unique=True,null=False)
    content = HTMLField()
    is_listed = models.BooleanField(
           default=True,
           help_text='Check to hide the post'
    )
    published_date = models.DateField()
    tags = models.ManyToManyField(Tag, related_name="tags", blank=True)

    def __str__(self):
                return self.title


class Project(models.Model):
    STATUS_CHOICES = [("prod", "En production"), ("beta", "Bêta"), ("rd", "R&D")]

    title = models.CharField(max_length=300,null=False)
    slug = models.SlugField(unique=True,null=False)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="rd")
    sources = models.CharField(max_length=300, blank=True)
    processing = models.CharField(max_length=300, blank=True)
    usage = models.CharField(max_length=200)
    stack = models.CharField(max_length=300, blank=True)
    github_url = models.URLField(blank=True)
    is_listed = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    def _split(self, value):
        return [s.strip() for s in value.split(",") if s.strip()]

    def sources_list(self):
        return self._split(self.sources)

    def processing_list(self):
        return self._split(self.processing)

    def stack_list(self):
        return self._split(self.stack)
