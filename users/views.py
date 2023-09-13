# DRF 에 필요한 함수, 클래스 호출
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status, permissions
from users.serializers import UserSerializer, CustomTokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate



# 이메일 인증 전에는 is_active를 비활성화
# user.is_active = False
# user = serializer.save()
class SignupView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({"message": "가입완료!"}, status=status.HTTP_201_CREATED)
        else:
            return Response({"message": f"${serializer.errors}"}, status=status.HTTP_400_BAD_REQUEST)


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer
"""
def login(request):
    if request.method == "GET":
        return render(request, 'login.html')
    elif request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            loginsession(request, user)
            return redirect('users:user')
        else:
            return HttpResponse("username 또는 password를 잘못 입력하였거나, 존재하지 않는 아이디 입니다.")
"""

class MockView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request):
        print(request.user)
        user = request.user
        user.is_admin = True
        user.save()
        return Response("get 요청!")
