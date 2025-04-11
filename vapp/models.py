from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Action(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='actions')

    def __str__(self):
        return self.name


class Keyword(models.Model):
    phrase = models.CharField(max_length=100)
    action = models.ForeignKey(Action, on_delete=models.CASCADE, related_name='keywords')

    def __str__(self):
        return self.phrase


class Question(models.Model):
    keyword = models.ForeignKey(Keyword, on_delete=models.CASCADE, related_name='questions')
    text = models.TextField()

    def __str__(self):
        return f"Q: {self.text}"


class Response(models.Model):
    keyword = models.ForeignKey(Keyword, on_delete=models.CASCADE, related_name='responses')
    text = models.TextField()

    def __str__(self):
        return f"R: {self.text}"
