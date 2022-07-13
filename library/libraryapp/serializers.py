from rest_framework import serializers
from django.contrib.auth import authenticate
from django.contrib.auth.models import update_last_login
from django.contrib.auth.models import User,Group
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from .models import Book
class RegistrationSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(max_length=128, write_only=True)
    group = serializers.CharField(max_length=100, write_only=True)
    

    def create(self,validated_data):
        print(validated_data)
        print("pppppppppppp")
        user = User.objects.create_user(email =validated_data['email'],username=validated_data['email'],     password = validated_data['password']  )
        group = Group.objects.get_or_create(name=validated_data['group'])
        user.groups.add(group[0].id)
        return user
class BookViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ["book_name","status"]

    def create(self, validated_data):
        
        book = Book.objects.create(**validated_data)
        return book
    def update(self,instance, validated_data):
        
      
        instance.book_name = validated_data.get('book_name', instance.book_name)
        instance.status = validated_data.get('status', instance.status) 
        instance.save()
        return instance   


class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["first_name","last_name","username","email"]

    def create(self, validated_data):
        
       
        member = User.objects.create(**validated_data)
        group = Group.objects.get_or_create(name="Member")
        member.groups.add(group[0].id)
        return member
    def update(self,instance, validated_data):
        
      
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.username =  validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)
        instance.save()
        return instance   

class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(max_length=128, write_only=True)
    access = serializers.CharField(read_only=True)
    refresh = serializers.CharField(read_only=True)
    role = serializers.CharField(read_only=True)

    def create(self, validated_date):
        pass

    def update(self, instance, validated_data):
        pass

    def validate(self, data):
        print(data)
        print("PPPPP")
        email = data['email']
        password = data['password']
        user = authenticate(username=email, password=password)
        print(user)
        print("oooooooo") 
        if user is None:
            raise serializers.ValidationError("Invalid login credentials")

      
        refresh = RefreshToken.for_user(user)
        refresh_token = str(refresh)
        access_token = str(refresh.access_token)

        update_last_login(None, user)
        for i in user.groups.all(): 
            role = i.name 
        validation = {
            'access': access_token,
            'refresh': refresh_token,
            'email': user.email,
            'role': role,
        }

        return validation
    


    