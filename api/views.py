from django.shortcuts import render
from rest_framework import generics

from .models import Sample
from .serializers import SampleSerializer


class SampleView(generics.ListAPIView):
    queryset = Sample.objects.all()
    serializer_class = SampleSerializer
