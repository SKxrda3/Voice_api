from django.urls import path
from .views import add_action, add_keyword, add_question, add_response, get_question_from_phrase,get_response_from_reply  # ai_response_view

urlpatterns = [
    # path('ai-response/', ai_response_view, name='ai-response'),
    path('get_response_from_reply/', get_response_from_reply, name='get_response_from_reply'),
    path('get_question_from_phrase/', get_question_from_phrase, name='get_question_from_phrase'),
    path('add-action/', add_action, name='add_action'),
    path('add-keyword/', add_keyword, name='add_keyword'),
    path('add-question/', add_question, name='add_question'),
    path('add-response/', add_response, name='add_response'),
]
