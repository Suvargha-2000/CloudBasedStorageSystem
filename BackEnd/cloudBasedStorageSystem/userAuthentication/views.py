from django.http import HttpResponse
import json
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from django.http import HttpResponse
from rest_framework.throttling import UserRateThrottle

class apiAuthentication(APIView):
    permission_classes = (IsAuthenticated, )
    throttle_scope = 'api_req'

    def post(self , request):
        content = {"something" : "else"}
        return Response(content)
  
    def get(self, request):
        content = {'message': 'You are authenticated User'}
        return Response(content)


class createUser(APIView) : 

    throttle_scope = 'user_creation'

    def post(self , request):
        print("Creating user")
        requestData = json.loads(request.body)
        userName = requestData["userName"]
        password = requestData["password"]
        email = requestData["email"]

        user = User.objects.create_user(userName, email, password)
        user.save()
        return HttpResponse("User Created")
    
class deleteUser(APIView):
    permission_classes = (IsAuthenticated, )

    def post(self , request) : 

        print(request.user)
        # return HttpResponse("HJ")

        userName = request.user
        try:
            u = User.objects.get(username = userName)
            u.delete()
            return Response("The user is deleted")            

        except User.DoesNotExist:   
            return Response("The user not available")      

        except Exception as e: 
            return Response(e)
