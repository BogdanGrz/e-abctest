from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User


class Post(models.Model):
    author = models.ForeignKey('auth.User', default=4, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    viewed_by = models.TextField(default="")

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def approve_comments(self):
        return self.comments.filter(approved_comment=True)

    def not_approve_comments(self):
        return self.comments.filter(approved_comment=False)

    def get_absolute_url(self):
        return reverse("post_detail",kwargs={'pk':self.pk})

    def add_username(self, username):
        teraz = timezone.now()
        teraz = teraz.strftime("%Y-%m-%d %H:%M")
        if username not in self.viewed_by:
            self.viewed_by += (username + ": " + str(teraz) + "<br>")
            self.save()

    def __str__(self):
        return self.title



class Comment(models.Model):
    post = models.ForeignKey('blog.Post', related_name='comments',on_delete=models.CASCADE)
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def get_absolute_url(self):
        return reverse("post_list")

    def __str__(self):
        return self.text

class Przedszkolak(models.Model):
    rodzic = models.ManyToManyField('auth.User')
    nazwa_skrócona = models.CharField(max_length=20, unique=True)
    Imię = models.CharField(max_length=20)
    Nazwisko = models.CharField(max_length=50)
    grupa = models.ForeignKey('blog.Grupa', default=1, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("post_list")

    class Meta:
        verbose_name_plural = "Przedszkolaki"

class Grupa(models.Model):
    nazwa = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.nazwa

    def get_absolute_url(self):
        return reverse("post_list")

    class Meta:
        verbose_name_plural = "Grupy"
