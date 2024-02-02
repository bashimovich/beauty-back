from rest_framework import viewsets
from .serializers import *
from saloon.models import *
from rest_framework.filters import SearchFilter, BaseFilterBackend
# from slugify import slugify
from rest_framework.response import Response
# from django.shortcuts import get_object_or_404
from datetime import datetime
from rest_framework.views import APIView
# from django.http import Http404
from rest_framework.decorators import action
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status



class ALLCompanyViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    filter_backends = [SearchFilter]
    search_fields = ['name']

class TOPCompanyViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Company.objects.filter(_type = 'top')
    serializer_class = CompanySerializer

class WTVCompanyViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Company.objects.filter(_type = 'wtv')
    serializer_class = CompanySerializer

class OrderViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class OrderCreateAPIView(APIView):
    def post(self, request):
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
