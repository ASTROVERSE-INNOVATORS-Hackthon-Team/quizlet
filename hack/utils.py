# utils.py
from .models import Question
import random

def generate_quiz_questions(quiz):
    sample_questions = {
        "math": [
            ("What is 2 + 2?", "4"),
            ("Solve for x: 3x = 12", "x = 4"),
            ("What is the square root of 16?", "4")
        ],
        "science": [
            ("What planet is known as the Red Planet?", "Mars"),
            ("What gas do plants absorb from the atmosphere?", "Carbon Dioxide"),
            ("What is H2O commonly known as?", "Water")
        ]
    }
    
    questions = sample_questions.get(quiz.topic.lower(), [("Default question?", "Default answer")])
    random.shuffle(questions)
    
    for question_text, answer in questions:
        Question.objects.create(quiz=quiz, text=question_text, answer=answer)
