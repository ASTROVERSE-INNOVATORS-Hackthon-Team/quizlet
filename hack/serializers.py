from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Quiz, UserProgress, Question,Choice

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

class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = ["id", "choice_text", "is_correct"]

class QuestionSerializer(serializers.ModelSerializer):
    quiz = serializers.PrimaryKeyRelatedField(queryset=Quiz.objects.all())  # Returns quiz ID
    choices = ChoiceSerializer(many=True,required=False)  # Include multiple choices

    class Meta:
        model = Question
        fields = ["id", "quiz", "question_text", "choices"]  # Removed "answer"

    def to_representation(self, instance):
        """Customize response to hide correct choices for non-admin users."""
        data = super().to_representation(instance)
        request = self.context.get('request')

        # Hide correct answers if user is not staff
        if request and request.user and not request.user.is_staff:
            for choice in data["choices"]:
                choice.pop("is_correct", None)

        return data
    def create(self, validated_data):
        """Handles nested creation of choices when adding a question."""
        choices_data = validated_data.pop('choices', [])
        question = Question.objects.create(**validated_data)
        for choice in choices_data:
            Choice.objects.create(question=question, **choice)
        return question