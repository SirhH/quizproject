from django.db import models

# Create your models here.


class Quiz(models.Model):
    quiz_number = models.PositiveIntegerField()
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


class Question(models.Model):
    question = models.TextField()
    answer1 = models.CharField(max_length=100)
    answer2 = models.CharField(max_length=100)
    answer3 = models.CharField(max_length=100)
    correct = models.PositiveIntegerField()
    answers = [answer1, answer2, answer3]
    quiz = models.ForeignKey(Quiz, related_name='questions', on_delete=models.CASCADE)

    def __str__(self):
        return self.question


class Question2(models.Model):
    question = models.TextField(max_length=100)
    quiz = models.ForeignKey(Quiz, related_name='questions2', on_delete=models.CASCADE)

    def __str__(self):
        return self.question


class Answer(models.Model):
    answer = models.CharField(max_length=100)
    value = models.PositiveIntegerField()
    question = models.ForeignKey(Question2, related_name='answers', on_delete=models.CASCADE)

    def __str__(self):
        return self.answer

