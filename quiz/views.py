
# Create your views here.
from rest_framework import viewsets

from .models import Quiz, Question
from .serializers import QuizSerializer, QuestionSerializer, GetQuizSerializer


class QuizViewSet(viewsets.ModelViewSet):
    serializer_class = QuizSerializer
    http_method_names = ['get', 'post']

    def get_queryset(self):
        self.queryset = Quiz.objects.all()
        return self.queryset


class QuestionViewSet(viewsets.ModelViewSet):
    serializer_class = QuestionSerializer
    http_method_names = ['get', 'post']

    def get_queryset(self):
        self.queryset = Question.objects.all()
        return self.queryset


class QuizQuestionViewSet(viewsets.ModelViewSet):
    serializer_class = GetQuizSerializer
    http_method_names = ['get']

    def get_queryset(self):
        self.queryset = Quiz.objects.all()
        return self.queryset
