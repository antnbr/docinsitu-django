from django.conf import settings
from django.db import models
from django.utils import timezone

class Subject(models.Model):
    question = models.CharField(max_length=200)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.question

class Article(models.Model):
    question = models.ForeignKey(Subject, on_delete=models.CASCADE, null=True)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return "Article à {}".format(self.created_date)

class Snap(models.Model):
    question = models.ForeignKey(Subject, on_delete=models.CASCADE, null=True)
    data = models.ImageField(upload_to='scans')
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return "Snap pour à {}".format(self.created_date)
