from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.models import User

class UserRegisterSerializer(serializers.ModelSerializer):
    '''
    Validates user model fields. 
    If everything is correct, saves the user and returns current user object
    '''
    email = serializers.EmailField(
            required=True,
            validators=[UniqueValidator(queryset=User.objects.all())]
            )
    username = serializers.CharField(
            max_length=32,
            required=True,
            validators=[UniqueValidator(queryset=User.objects.all())]
            )
    password = serializers.CharField(min_length=8, write_only=True)

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'],
             validated_data['password'])
        return user

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')


class UserSerializer(serializers.ModelSerializer):
    '''
    Simple user serializer
    '''
    class Meta:
        model = User 
        fields = ('id', 'username')