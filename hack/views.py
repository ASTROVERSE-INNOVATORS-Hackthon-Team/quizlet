from django.utils.decorators import method_decorator
from .utils import generate_quiz_questions
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from .models import Quiz, Question, UserProgress
from .serializers import QuizSerializer, QuestionSerializer, UserProgressSerializer

@method_decorator(csrf_exempt, name='dispatch')  # Apply CSRF exemption (if needed)
class QuizListCreateView(generics.ListCreateAPIView):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]  # Allow public GET, restrict POST

    def perform_create(self, serializer):
        quiz = serializer.save(user=self.request.user)  # Save and assign to quiz
        generate_quiz_questions(quiz)  

class QuestionListView(generics.ListAPIView):
    serializer_class = QuestionSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        quiz_id = self.kwargs['quiz_id']
        return Question.objects.filter(quiz_id=quiz_id)


class UserProgressView(generics.ListCreateAPIView):
    serializer_class = UserProgressSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return UserProgress.objects.filter(user=self.request.user)  # Show only the user's progress

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)  # Automatically set user to authenticated user
