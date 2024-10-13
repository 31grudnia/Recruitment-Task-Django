from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .tasks import check_pesel_data, check_pesel_control_number


def check_pesel(request):
    return render(request, 'zadanie2.html')

class PeselCheckView(APIView):
    def post(self, request):
        pesel = request.data.get('pesel')
        
        if not pesel:
            return Response({'error': 'Invalid PESEL number'}, status=status.HTTP_400_BAD_REQUEST)
        
        if not pesel.isdigit():
            return Response({'error': 'Invalid PESEL number: not a number'}, status=status.HTTP_400_BAD_REQUEST)
        
        if len(pesel) != 11:
            return Response({'error': 'Invalid PESEL number: not exact 11 digits'}, status=status.HTTP_400_BAD_REQUEST)
        
        task1 = check_pesel_control_number.delay(pesel)
        result1 = task1.get()
        if not result1:
            return Response({'error': 'Invalid PESEL: incorrect control digit'}, status=status.HTTP_400_BAD_REQUEST)

        task2 = check_pesel_data.delay(pesel)
        result2 = task2.get()  

        if task2.successful():
            return Response({
                'task_id': task2.id,
                'birthdate': result2['birthdate'],
                'sex': result2['sex']
            }, status=status.HTTP_200_OK)
        else:
            return Response({
                'task_id': task2.id,
                'error': 'Task failed to process PESEL'
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)