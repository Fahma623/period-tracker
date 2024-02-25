from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from UserApp.models import User,Period
from UserApp.serializers import UserSerializer,PeriodSerializer

# Create your views here.

@csrf_exempt
def UserApi(request,id=0):
    if request.method=='GET':
        user = User.objects.all()
        user_serializer=UserSerializer(user,many=True)
        return JsonResponse(user_serializer.data,safe=False)
    
