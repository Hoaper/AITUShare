from django.db import models
from profiles.models import Profile


class MainTopic(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.name}"


class Topic(models.Model):
    main_topic = models.ForeignKey(MainTopic, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=200, null=True)
    text = models.TextField(max_length=2000, default="Topic body")
    author = models.ForeignKey(Profile, on_delete=models.SET_DEFAULT, default="DELETED")
    Closed = models.BooleanField(default=False)
    accepted = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.title}: {self.main_topic} [{self.author.login}]"


class Comment(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=True)
    reply = models.ForeignKey("self", on_delete=models.SET_DEFAULT, default=None, blank=True, null=True)
    author = models.ForeignKey(Profile, on_delete=models.SET_DEFAULT, default="DELETED")
    text = models.TextField(max_length=20000)

    def __str__(self):
        return f"{self.author.login}: {self.text[:30]}..."
