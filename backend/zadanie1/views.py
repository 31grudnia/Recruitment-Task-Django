from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import render, redirect
from django.urls import reverse

from .serializers import TextFileUploadSerializer
from .tasks import shuffle_text


def upload_page(request):
    return render(request, 'zadanie1.html')


def result_page(request):
    error = request.GET.get('error', '')
    shuffled_text = request.GET.get('shuffled_text', '')
    context = {
        'error': error,
        'shuffled_text': shuffled_text
    }
    return render(request, 'zadanie1-result.html', context)


class FileUploadView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = TextFileUploadSerializer(data=request.data)
        if serializer.is_valid():
            file = serializer.validated_data.get('file', None)

            if not file:
                return redirect(reverse('result-page') + '?error=No file uploaded.')

            print(f"File size: {file.size}")  
            
            if not file.size:
                return redirect(reverse('result-page') + '?error=The uploaded file is empty.')

            if not file.name.endswith('.txt'):
                return redirect(reverse('result-page') + '?error=Invalid file.')

            contents = file.read().decode('utf-8')

            if not contents.strip():
                return redirect(reverse('result-page') + '?error=The uploaded file is empty.')

            task = shuffle_text.delay(contents)
            result = task.get()
            return redirect(reverse('result-page') + f'?shuffled_text={result}')
        
        return redirect(reverse('result-page') + '?error=Invalid file.')
