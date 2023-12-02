from rest_framework import renderers, status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import RamSerializer
from .models import Ram
import psutil
from datetime import date


class RamInfoView(APIView):

    def get(self, request):
        ram_info = psutil.virtual_memory()
        data = {
            'avaliable_ram' : ram_info[1] / (1024 * 1024), 
            'date' : date.today()
        }
        serializer = RamSerializer(data)
        return Response(serializer.data, status=status.HTTP_201_CREATED)