from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView
from rest_framework.response import Response
from .models import Rate
from .models import Content
from .serializers import ContentSerializer, RateSerializer
from rest_framework import permissions


# Create your views here.
