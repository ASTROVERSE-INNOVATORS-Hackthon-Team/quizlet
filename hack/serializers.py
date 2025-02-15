from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Quiz, UserProgress, Question

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email"]


class QuizSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)  # Nested User Data

    class Meta:
        model = Quiz
        fields = ["id", "topic", "difficulty", "user", "created_at"]


class UserProgressSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    quiz = QuizSerializer(read_only=True)

    class Meta:
        model = UserProgress
        fields = ["id", "user", "quiz", "score"]


class QuestionSerializer(serializers.ModelSerializer):
    quiz = serializers.PrimaryKeyRelatedField(queryset=Quiz.objects.all())  # Quiz ID only

    class Meta:
        model = Question
        fields = ["id", "quiz", "question_text", "answer"]
