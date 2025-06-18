from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.permissions import AllowAny

from .models import Profile, Address, Contact, Student, Guardian
from .serializers import GetStudentSerializer

# Create your views here.

class GetStudentView(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = GetStudentSerializer
    parser_classes = [FormParser, MultiPartParser]
    permission_classes = [AllowAny] 
    depyth = 2