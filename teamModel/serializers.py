from rest_framework import serializers
from .models import TeamMember, Team

class TeamMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamMember
        fields = ('id',
                  'profilePicture',
                  'firstName',
                  'lastName',
                  'type',
                  'onLeave',
                  'specialities',
                  'biography',
        )

class TeamSerializer(serializers.ModelSerializer):
    teamMembers = TeamMemberSerializer(many=True)

    class Meta:
        model = Team
        fields = ('id',
                  'teamName',
                  'teamMembers')