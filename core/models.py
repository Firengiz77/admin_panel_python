from django.db import models

class Course(models.Model):
    STATUS=(
        ('draft','Draft'),
        ('published','Published')
    )
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField()
    author = models.CharField(max_length=120)
    status = models.CharField(choices=STATUS, default='draft', max_length=11)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title



class Lesson(models.Model):
     title = models.CharField(max_length=100)
     course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True)
     position = models.IntegerField()
     video_url = models.CharField(max_length=2000)
     created_at = models.DateTimeField(auto_now_add=True)
     updated_at = models.DateTimeField(auto_now=True)