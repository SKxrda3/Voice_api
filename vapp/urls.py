from django.urls import path
from .views import get_question_from_phrase,get_response_from_reply  # ai_response_view

urlpatterns = [
    # path('ai-response/', ai_response_view, name='ai-response'),
    path('get_response_from_reply/', get_response_from_reply, name='get_response_from_reply'),
    path('get_question_from_phrase/', get_question_from_phrase, name='get_question_from_phrase'),
]
