from django.shortcuts import render
from rest_framework import generics
from .models import TeamMember
from .serializers import TeamMemberSerializer

# Create your views here.

class TeamMemberList(generics.ListCreateAPIView):
    queryset = TeamMember.objects.all()
    serializer_class = TeamMemberSerializer

class TeamMemberDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = TeamMember.objects.all()
    serializer_class = TeamMemberSerializer