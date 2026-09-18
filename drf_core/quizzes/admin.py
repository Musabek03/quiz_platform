from django.contrib import admin
from .models import Question, Quiz, Answer


@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):

    list_display = ("title",  "author", "is_published", "created_at")
    list_filter = ("created_at", "is_published")



@admin.register(Question)
class Question(admin.ModelAdmin):

    list_display = ("quiz", "text", "order", "points")


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):

    list_display = ("question", "text", "is_correct")


