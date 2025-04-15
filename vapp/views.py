from rest_framework.decorators import api_view
from rest_framework.response import Response as DRFResponse
from .models import Keyword
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response as DRFResponse
from .models import Action, Keyword, Question, Response
from .serializers import ActionSerializer, KeywordSerializer, QuestionSerializer, ResponseSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import JSONParser, FormParser, MultiPartParser

import logging
logger = logging.getLogger(__name__)


# @api_view(['GET'])
# def get_response_from_reply(request):
#     user_reply = request.GET.get('phrase', '').lower()

#     try:
#         keyword = Keyword.objects.get(phrase__iexact=user_reply)
#         response = keyword.responses.first().text if keyword.responses.exists() else "No response found."

#         return DRFResponse({
#             "keyword": keyword.phrase,
#             "response": response
#         })
#     except Keyword.DoesNotExist:
#         return DRFResponse({"error": "Keyword not found."}, status=404)



# @api_view(['POST'])
# def get_question_from_phrase(request):
#     print("🔥 View hit")

#     # Debugging request content
#     print("📦 request.content_type:", request.content_type)
#     try:
#         print("📨 request.data:", request.data)
#         print("📨 Raw body:", request.body.decode('utf-8'))
#     except Exception as e:
#         print("❌ Error while reading body:", str(e))

#     #upper ke debugging ke liye hai Extract and validate phrase
#     phrase = request.data.get('phrase', '').strip().lower()
#     if not phrase:
#         return DRFResponse(
#             {"error": "Missing 'phrase' in request body."},
#             status=status.HTTP_400_BAD_REQUEST
#         )

#     # Fetch keyword and related data
#     try:
#         keyword = Keyword.objects.get(phrase__iexact=phrase)
#         action_name = keyword.action.name
#         question = (
#             keyword.questions.first().text if keyword.questions.exists()
#             else "No question found."
#         )

#         return DRFResponse({
#             "keyword": keyword.phrase,
#             "action": action_name,
#             "question": question
#         })

#     except Keyword.DoesNotExist:
#         return DRFResponse(
#             {"error": "Keyword not found."},
#             status=status.HTTP_404_NOT_FOUND
#         )

class GetQuestionFromPhraseView(APIView):
    parser_classes = [JSONParser]

    def post(self, request):
        phrase = request.data.get('phrase', '').strip().lower()
        if not phrase:
            return DRFResponse(
                {"error": "Missing 'phrase' in request body."},
                status=status.HTTP_400_BAD_REQUEST
            )   

        try:
            keyword = Keyword.objects.get(phrase__iexact=phrase)
            action_name = keyword.action.name
            question = (
                keyword.questions.first().text if keyword.questions.exists()
                else "No question found."
            )

            return DRFResponse({
                "keyword": keyword.phrase,
                "action": action_name,
                "question": question
            })

        except Keyword.DoesNotExist:
            return DRFResponse(
                {"error": "Keyword not found."},
                status=status.HTTP_404_NOT_FOUND
            )

# @api_view(['POST'])  # Change to POST
# def get_response_from_reply(request):
#     user_reply = request.data.get('phrase', '').lower()  
#     try:
#         keyword = Keyword.objects.get(phrase__iexact=user_reply)
#         response = keyword.responses.first().text if keyword.responses.exists() else "No response found."
#         return DRFResponse({
#             "keyword": keyword.phrase,
#             "response": response
#         })
#     except Keyword.DoesNotExist:
#         return DRFResponse({"error": "Keyword not found."}, status=404)

# class GetResponseFromReply(APIView):
#     def post(self, request):
#         try:
#             user_reply = request.data.get('phrase', '').strip().lower()
#         except Exception as e:
#             return Response({"error": "Invalid JSON."}, status=status.HTTP_400_BAD_REQUEST)

#         if not user_reply:
#             return Response(
#                 {"error": "Missing 'phrase' in request body."},
#                 status=status.HTTP_400_BAD_REQUEST
#             )

#         try:
#             keyword = Keyword.objects.get(phrase__iexact=user_reply)
#             response = (
#                 keyword.responses.first().text if keyword.responses.exists()
#                 else "No response found."
#             )
#             return Response({
#                 "keyword": keyword.phrase,
#                 "response": response
#             })

#         except Keyword.DoesNotExist:
#             return Response({"error": "Keyword not found."}, status=status.HTTP_404_NOT_FOUND)


class GetResponseFromReply(APIView):
    def post(self, request):
        try:
            user_reply = request.data.get('phrase', '').strip().lower()
        except Exception:
            return DRFResponse({"error": "Invalid JSON."}, status=400, content_type="application/json")

        if not user_reply:
            return DRFResponse({"error": "Missing 'phrase'."}, status=400, content_type="application/json")

        try:
            keyword = Keyword.objects.get(phrase__iexact=user_reply)
            response = (
                keyword.responses.first().text if keyword.responses.exists()
                else "No response found."
            )
            return DRFResponse({
                "keyword": keyword.phrase,
                "response": response
            }, content_type="application/json")

        except Keyword.DoesNotExist:
            return DRFResponse({"error": "Keyword not found."}, status=404, content_type="application/json")

@api_view(['POST'])
def add_action(request):
    serializer = ActionSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return DRFResponse(serializer.data, status=status.HTTP_201_CREATED)
    return DRFResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def add_keyword(request):
    serializer = KeywordSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return DRFResponse(serializer.data, status=status.HTTP_201_CREATED)
    return DRFResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def add_question(request):
    serializer = QuestionSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return DRFResponse(serializer.data, status=status.HTTP_201_CREATED)
    return DRFResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def add_response(request):
    serializer = ResponseSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return DRFResponse(serializer.data, status=status.HTTP_201_CREATED)
    return DRFResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

