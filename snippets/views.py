# from django.http import HttpResponse, JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# from rest_framework.parsers import JSONParser
# from snippets.models import Snippet
# from snippets.serializers import SnippetSerializer



# @csrf_exempt
# def snippet_list(request):
#     """
#     List all code snippets, or create a new snippet.
#     """
#     if request.method == 'GET':
#         snippets = Snippet.objects.all()
#         print(snippets)

#         serializer = SnippetSerializer(snippets, many=True)
#         return JsonResponse(serializer.data, safe=False)

#     elif request.method == 'POST':
#         data = JSONParser().parse(request)
#         serializer = SnippetSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)
#         return JsonResponse(serializer.errors, status=400)

# @csrf_exempt
# def snippet_detail(request, pk):
#     """
#     Retrieve, update or delete a code snippet.
#     """
#     try:
#         snippet = Snippet.objects.get(pk=pk)
#     except Snippet.DoesNotExist:
#         return HttpResponse(status=404)

#     if request.method == 'GET':
#         serializer = SnippetSerializer(snippet)
#         return JsonResponse(serializer.data)

#     elif request.method == 'PUT':
#         data = JSONParser().parse(request)
#         serializer = SnippetSerializer(snippet, data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data)
#         return JsonResponse(serializer.errors, status=400)

#     elif request.method == 'DELETE':
#         snippet.delete()
#         return HttpResponse(status=204)

######################################################################################################

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from snippets.models import Snippet
from snippets.serializers import SnippetSerializer



@api_view(['GET', 'POST'])
def snippet_list(request, format=None):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        snippets = Snippet.objects.all()
        print("yes1")
        #print(snippets[1])
        #what it deliver's is an array & that array gets into  
        '''
        <QuerySet [<Snippet: Snippet object (1)>, <Snippet: Snippet object (2)>, 
        <Snippet: Snippet object (3)>, <Snippet: Snippet object (4)>, 
        <Snippet: Snippet object (5)>, <Snippet: Snippet object (6)>,
        <Snippet: Snippet object (8)>, <Snippet: Snippet object (9)>,
        <Snippet: Snippet object (10)>, <Snippet: Snippet object (11)>]>
        '''

        serializer = SnippetSerializer(snippets, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = SnippetSerializer(data=request.data)
        # print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# SnippetSerializer(data={'id': 10, 'title': 'all awesome!!!!!', 'code': 'print("hello, world")', 'linenos': False, 'language': 'python', 'style': 'friendly'}):
"""
#     id = IntegerField(label='ID', read_only=True)
#     title = CharField(allow_blank=True, max_length=100, required=False)
#     code = CharField(style={'base_template': 'textarea.html'})
#     linenos = BooleanField(required=False)
#     language = ChoiceField()"""


@api_view(['GET', 'PUT', 'DELETE'])
def snippet_detail(request, pk, format=None):   
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        snippet = Snippet.objects.get(pk=pk)
    except Snippet.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = SnippetSerializer(snippet)
        print("yes2")
        # print(serializer.data)
        '''{'id': 6, 'title': 'let it go !', 'code': 'print("hello, world")', 'linenos': False, 'language': 'python', 'style': 'friendly'}'''
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = SnippetSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            # print(serializer)
            '''put and post are almost returning same '''
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

