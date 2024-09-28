from django.shortcuts import render,redirect
from .serializers import TeacherSerializer,RegistrationSerializer,userLoginSerializer,changePasswordSerializer,userSerializer
from .models import teacher
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from rest_framework.status import HTTP_400_BAD_REQUEST,HTTP_204_NO_CONTENT,HTTP_200_OK
from rest_framework.decorators import api_view
from rest_framework import viewsets,generics
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate,login,logout
from django.utils.http import urlsafe_base64_decode,urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from rest_framework.response import Response
from django.utils.encoding import force_bytes
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string


class TeacherViewset(viewsets.ModelViewSet):
    queryset = teacher.objects.all()
    serializer_class = TeacherSerializer
    def get_queryset(self):
        queryset = super().get_queryset()
        user_id = self.request.query_params.get("user_id")
        if user_id:
            queryset = queryset.filter(user = user_id)
        return queryset
    
    def put(self,request):
        user_id = self.request.query_params.get("user_id")
        if user_id:
            data = teacher.objects.get(user=user_id)
            serializers = TeacherSerializer(data, data=request.data)
            print(serializers)
            print("inside user_id before serializers")
            if serializers.is_valid():
                serializers.save()
                return Response(serializers.data)
            return Response(serializers.errors, status=HTTP_400_BAD_REQUEST)


class UserViewSet(APIView):
    # queryset = TeacherModel.objects.all()
    serializer_class = userSerializer    
    def get_queryset(self,request,pk):
        queryset = super().get_queryset()
        queryset = queryset.filter(pk = pk)
        return queryset 
    def get(self,request,pk):
        data = User.objects.get(pk=pk)
        serializer = userSerializer(data)
        return Response(serializer.data)
    def put(self,request,pk):
        data = User.objects.get(pk=pk)
        serializers = userSerializer(data, data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
    
class UserRegistrationApiview(APIView):
    serializer_class = RegistrationSerializer
    def post(self,request):
        serializer = self.serializer_class(data=request.data)
        
        if serializer.is_valid():
            user = serializer.save()
            token = default_token_generator.make_token(user)
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            print('uid',uid)
            confirm_link = f"https://Excileence_Academy_api.onrender.com//user/active/{uid}/{token}"
            email_subject = "Confirm your email"
            email_body = render_to_string('confirm_email.html',{'confirm_link':confirm_link})
            email = EmailMultiAlternatives(email_subject,'',to=[user.email])
            email.attach_alternative(email_body,'text/html')
            email.send()
            return Response('Check Your mail for confirmation')
        return Response(serializer.errors)
def activate(request,uid64,token):
    try:
        uid = urlsafe_base64_decode(uid64).decode()
        user = User._default_manager.get(pk=uid)
    except(User.DoesNotExist):
        user = None
    if user is not None and default_token_generator.check_token(user,token):
        user.is_active = True
        user.save()
        return redirect ('http://127.0.0.1:5500/login.html')

    else:
        return redirect('register')


class UserLoginApiView(APIView):
    def post(self,request):
        serializer = userLoginSerializer(data = self.request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']

            user = authenticate(username=username,password=password)

            if user:
                token,_ = Token.objects.get_or_create(user=user)
                login(request,user)
                return Response({'token':token.key,'user_id' : user.id})
            else:
                return Response({'error':'Invalid Credential'})
        return Response(serializer.errors)

class UserLogoutView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def post(self,request):
        request.user.auth_token.delete()
        logout(request)
        return Response({'message': 'Logout successful.',}, status=HTTP_204_NO_CONTENT)


class ChangePasswordView(APIView):
    def put(self, request):
        user_id = request.data.get("user_id")
        users = User.objects.get(pk=user_id)
        serializer = changePasswordSerializer(data=request.data, context={'user': users})
        if serializer.is_valid():
            users.set_password(serializer.validated_data['new_password'])
            users.save()
            return Response({'message': 'Password changed successfully.'})
        print("before return error")
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
