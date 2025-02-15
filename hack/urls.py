from django.urls import path
from .views import QuizListCreateView, QuestionListView, UserProgressView

urlpatterns = [
    path('quiz/', QuizListCreateView.as_view(), name='quiz-list-create'),
    path('quiz/<int:id>/questions/', QuestionListView.as_view(), name='quiz-questions'),
    path('progress/', UserProgressView.as_view(), name='user-progress'),
]
