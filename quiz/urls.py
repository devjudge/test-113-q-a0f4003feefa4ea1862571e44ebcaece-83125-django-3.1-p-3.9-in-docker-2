from rest_framework import routers

from .views import QuizViewSet, QuestionViewSet, QuizQuestionViewSet

router = routers.SimpleRouter(trailing_slash=False)
router.register(r'quiz/?', QuizViewSet, basename='quiz')
router.register(r'questions/?', QuestionViewSet, basename='questions')
router.register(r'quiz-questions/?', QuizQuestionViewSet, basename='quiz-questions')

urlpatterns = router.urls
