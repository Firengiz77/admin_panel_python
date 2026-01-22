from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

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



class Person(models.Model):
    last_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    classes = models.ManyToManyField('Classes',blank = True)

    class Meta:
        verbose_name_plural = "People"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"   



class Classes(models.Model):
    name = models.CharField(max_length=100)
    year = models.IntegerField()

    class Meta:
        unique_together = ('name','year')

    def __str__(self):
        return f"{self.name}"  


class Grade(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    classes = models.ForeignKey(Classes, on_delete=models.CASCADE)
    grade = models.PositiveIntegerField(
    validators=[MinValueValidator(0), MaxValueValidator(100)]
     )

    def __str__(self):
        return f"{self.person} - {self.classes} - {self.grade}" 