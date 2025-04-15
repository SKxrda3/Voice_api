from rest_framework.decorators import api_view
from rest_framework.response import Response as DRFResponse
from .models import Keyword
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response as DRFResponse
from .models import Action, Keyword, Question, Response
from .serializers import ActionSerializer, KeywordSerializer, QuestionSerializer, ResponseSerializer

# @api_view(['GET'])
# def ai_response_view(request):
#     phrase = request.GET.get('phrase', '').lower()
    
#     try:
#         keyword = Keyword.objects.get(phrase__iexact=phrase)
#         action_name = keyword.action.name
#         question_text = keyword.questions.first().text if keyword.questions.exists() else "No question found."
#         response_text = keyword.responses.first().text if keyword.responses.exists() else "No response found."

#         data = {
#             "keyword": keyword.phrase,
#             "action": action_name,
#             "question": question_text,
#             "response": response_text,
#         }
#         return DRFResponse(data)
    
#     except Keyword.DoesNotExist:
#         return DRFResponse({"error": "Keyword not found."}, status=404)

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


@api_view(['POST'])

def get_question_from_phrase(request):
    print("🔥 View hit")  # Check if this prints

    try:
        print("DEBUG DATA:", request.data)
        print("Raw body:", request.body)
    except Exception as e:
        print("❌ Error while printing data:", str(e))

        
    print("DEBUG DATA:", request.data)
    # print(request.data)
    print("Raw body:", request.body)
    # print("Parsed data:", request.data)
    phrase = request.data.get('phrase', '').lower()
    try:  
        keyword = Keyword.objects.get(phrase__iexact=phrase)
        action_name = keyword.action.name
        question = keyword.questions.first().text if keyword.questions.exists() else "No question found."

        return DRFResponse({
            "keyword": keyword.phrase,
            "action": action_name,
            "question": question
        })
    except Keyword.DoesNotExist:
        return DRFResponse({"error": "Keyword not found."}, status=404)

@api_view(['POST'])  # Change to POST
def get_response_from_reply(request):
    user_reply = request.data.get('phrase', '').lower()  
    try:
        keyword = Keyword.objects.get(phrase__iexact=user_reply)
        response = keyword.responses.first().text if keyword.responses.exists() else "No response found."
        return DRFResponse({
            "keyword": keyword.phrase,
            "response": response
        })
    except Keyword.DoesNotExist:
        return DRFResponse({"error": "Keyword not found."}, status=404)

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

