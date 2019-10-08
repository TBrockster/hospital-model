from rest_framework import serializers
from .models import TeamMember, Team

class TeamMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamMember
        fields = ('profilePicture',
                  'firstName',
                  'lastName',
                  'type',
                  'onLeave',
                  'specialities',
                  'biography',
        )

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ('teamName',
                  'teamMember',)