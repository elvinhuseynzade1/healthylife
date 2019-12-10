from django.db import models
from django.contrib.auth.models import User


tip = (
    ('private', 'private'),
    ('state', 'state')
)


class Clinic(models.Model):
    name = models.CharField(max_length=120)
    address = models.CharField(max_length=120)
    number = models.CharField(max_length=120, blank="True")
    picture = models.ImageField(upload_to="images/")
    tip = models.CharField(max_length=50, choices=tip)
    rating = models.IntegerField(default=0)
    joiners = models.ManyToManyField(User, related_name='voting', blank=True)

    def __str__(self):
        return self.name


class Doctor(models.Model):
    position = models.CharField(max_length=120)
    name = models.CharField(max_length=120)
    surname = models.CharField(max_length=120)
    number = models.CharField(max_length=120, blank="True")
    clinic = models.ForeignKey(Clinic, on_delete=models.CASCADE)
    image=models.ImageField(upload_to='images/',blank=True)
    rating = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Comment(models.Model):
    post = models.ForeignKey(
        'Clinic', on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(auto_now=True)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text
