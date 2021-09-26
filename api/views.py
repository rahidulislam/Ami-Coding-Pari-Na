from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from core.models import KhojTheSearch
from .serializers import KhojSerializers
# Create your views here.

class KhojTheSearchAPI(APIView):
    def get(self, request, format=None):
        in_values = KhojTheSearch.objects.filter(user=request.user)
        serilizer = KhojSerializers(in_values, many=True)
        return Response(serilizer.data)

