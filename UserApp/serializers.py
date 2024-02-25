from rest_framework import serializers
from UserApp.models import User,Period

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=('username','password','age','dateofbirth')

class PeriodSerializer(serializers.ModelSerializer):
    class Meta:
        model=Period
        fields=('user','start_date','end_date')