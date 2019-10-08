from rest_framework import serializers
from .models import TeamMember

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