from django.db import models
from django.conf import settings
import uuid

class Quiz(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=200)
    description = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="quizzes")
    time_per_question = models.PositiveIntegerField()
    is_published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.title


class Question(models.Model):

    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE,related_name="questions")
    text = models.TextField()
    order = models.PositiveIntegerField()
    points = models.IntegerField()

    class Meta:

        ordering = ["order"]
        constraints = [
            models.UniqueConstraint(
                fields=["quiz", "order"],
                name="unique_quiz_question_order"
            )
        ]

    def __str__(self):
        return f"{self.quiz.title} | Вопрос #{self.order}"


class Answer(models.Model):

    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="answers")
    text = models.TextField()
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.text