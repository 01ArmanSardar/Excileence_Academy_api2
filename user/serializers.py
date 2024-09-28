from rest_framework import serializers
from .models import teacher
from django.contrib.auth.models import User
from rest_framework.validators import ValidationError

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model =teacher
        fields ="__all__"


class userSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username','first_name','last_name','last_name','email')



class RegistrationSerializer(serializers.ModelSerializer):
    confirm_password=serializers.CharField(required=True)

    class Meta:
        model = User
        fields= ['username','first_name','last_name','email','password','confirm_password']

        def save(self):
            username= self.validated_data['username']
            first_name= self.validated_data['first_name']
            last_name= self.validated_data['last_name']
            email= self.validated_data['email']
            password= self.validated_data['password']
            password2= self.validated_data['password2']

            if password != password2:
                raise serializers.ValidationError({'error':'pass does not match'})
            if User.objects.filter(email=email).exists():
                raise serializers.ValidationError({'error':'Email already exits'})
            account= User(usernames=username,email=email,first_name=first_name,last_name=last_name)
            account.set_password(password)
            account.is_active=False
            account.save()
            teacher.objects.create(
                user = account
            )
            return account
    

class userLoginSerializer(serializers.Serializer):
    username=serializers.CharField()
    password=serializers.CharField()


class changePasswordSerializer(serializers.Serializer):
    old_password=serializers.CharField(required=True)
    new_password=serializers.CharField(required=True)
    confirm_password=serializers.CharField(required=True)
    
    def validate(self,data):
        user = self.context.get('user')
        if not user.check_password(data['old_password']):
            raise ValidationError({'old_password':'wrong_password.'})
        if data['new_password'] != data['cofirm_password']:
            raise ValidationError({'new_password':'passwords do not match.'})
        
        return data
        
