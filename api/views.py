from django.shortcuts import render
from rest_framework import viewsets
from .serializer import ProgrammerSerializer, studentSerializer
from .models import programmer,student


class ProgrammerViewSet(viewsets.ModelViewSet): 
    queryset = programmer.objects.all()
    serializer_class = ProgrammerSerializer

# Create your views here.

class studentViewSet(viewsets.ModelViewSet):
    queryset = student.objects.all()
    serializer_class = studentSerializer
    
