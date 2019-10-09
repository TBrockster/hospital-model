from django.shortcuts import render
from rest_framework import generics
from .models import TeamMember, Team
from .serializers import TeamMemberSerializer, TeamSerializer

from rest_framework.response import Response
from rest_framework.views import APIView
# from .logic import Nurse, Surgeon, AdminAssistant, Team

# Create your views here.

class TeamMemberList(generics.ListCreateAPIView):
    queryset = TeamMember.objects.all()
    serializer_class = TeamMemberSerializer

class TeamMemberDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = TeamMember.objects.all()
    serializer_class = TeamMemberSerializer

class TeamList(APIView):
    def get(self, request):
        teams = Team.objects.all()
        serializer = TeamSerializer(teams, many=True)
        return Response({'teams': serializer.data})

"""
    def post(self, request):
        # turn incoming request to object
        serializer = TeamSerializer(request)
        # map attached teamMember list to teamMembers class from .logic.py
        roster = []
        for teamMember in serializer.teamMembers
            if teamMember.type == 'Nurse':
                roster.append(Nurse(first_name = teamMember.firstName, 
                                    last_name = teamMember.lastName, 
                                    specialities = teamMember.specialities, 
                                    biography = teamMember.biography))
            elif teamMember.type == 'Surgeon':
                roster.append(Surgeon(first_name = teamMember.firstName, 
                                      last_name = teamMember.lastName, 
                                      specialities = teamMember.specialities, 
                                      biography = teamMember.biography))
            elif teamMember.type == 'Admin Assistant':
                roster.append(AdminAssistant(first_name = teamMember.firstName, 
                                             last_name = teamMember.lastName, 
                                             specialities = teamMember.specialities, 
                                             biography = teamMember.biography))
        # create a team to check validity
        trial_team = Team('Trial Team')
        for teamMember in roster
            Team.add_member(teamMember)
        # check that team is valid
        # reject if not valid
        if trial_team.validity_check() == False:
            raise Exception('Error: Team is not valid.')
        else:
        # save and return expected response if valid
          serializer.save()
          return Response(serializer.data)
"""

class TeamDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
