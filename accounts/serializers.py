from django.core.validators import validate_email
from rest_framework import serializers
from .models import User
from django.contrib import auth
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.tokens import RefreshToken, TokenError


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=68, min_length=6, write_only=True)
    password2 = serializers.CharField(max_length=68, min_length=6, write_only=True)

    class Meta:
        model = User
        fields = ['email', 'username', 'password', 'password2']

    def validate(self, attrs):
        username = attrs.get('username', '')
        password = attrs.get('password', '')
        password2 = attrs.get('password2', '')
        if password != password2:
            raise serializers.ValidationError('password != password2')
        attrs.pop('password2')
        if not username.isalnum():
            raise serializers.ValidationError(
                self.default_error_messages)
        return attrs

    def create(self, validated_data):
        password = validated_data.pop('password')
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance


class LoginSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=68, min_length=6, write_only=True)
    username = serializers.CharField(max_length=255, min_length=3)
    tokens = serializers.SerializerMethodField()

    def get_tokens(self, obj):
        user = User.objects.get(username=obj['username'])
        return {
            'refresh': user.tokens()['refresh'],
            'access': user.tokens()['access']
        }

    class Meta:
        model = User
        fields = ['password', 'username', 'tokens']

    def validate(self, attrs):
        username = attrs.get('username', '')
        password = attrs.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if not user:
            raise AuthenticationFailed('Invalid credentials, try again')
        if not user.is_active:
            raise AuthenticationFailed('Account disabled, contact admin')
        return {
            'email': user.email,
            'username': user.username,
            'tokens': user.tokens
        }


class LogoutSerializer(serializers.Serializer):
    refresh = serializers.CharField()

    def validate(self, attrs):
        self.token = attrs['refresh']
        return attrs

    def save(self, **kwargs):
        try:
            RefreshToken(self.token).blacklist()
        except TokenError:
            self.fail('bad_token')


class VerifyEmailSerializer(serializers.Serializer):
    email = serializers.EmailField()


class ForgotPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField()


class VerificationCodeCheckSerializer(serializers.Serializer):
    code = serializers.CharField()
    email = serializers.EmailField()


class NewPasswordSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()
    code = serializers.CharField(max_length=68, write_only=True)
    password = serializers.CharField(max_length=68, min_length=6, write_only=True)
    password2 = serializers.CharField(max_length=68, min_length=6, write_only=True)

    class Meta:
        model = User
        fields = ['email', 'code', 'password', 'password2']

    def validate(self, attrs):
        email = attrs.get('email')
        code = attrs.get('code', '')
        user = User.objects.get(email=email)
        print(attrs)
        # if user.verification_code != code:
        #     raise serializers.ValidationError('invalid code for user')
        password = attrs.get('password', '')
        password2 = attrs.get('password2', '')
        if password != password2:
            raise serializers.ValidationError('password != password2')
        attrs.pop('password2')
        attrs.pop('code')
        return attrs

    def create(self, validated_data):
        email = validated_data.get('email')
        user = User.objects.get(email=email)
        user.set_password(validated_data['password'])
        print(user.verification_code)
        user.verification_code = ''
        print(user.verification_code)
        user.save()
        return user


class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        # fields = ['id', 'username', 'first_name', 'last_name', 'email']


class UserUpdateSerializer(serializers.ModelSerializer):

    def validate(self, attrs):
        username = attrs.get('username')
        email = attrs.get('email')
        first_name = attrs.get('first_name')
        last_name = attrs.get('last_name')
        phone = attrs.get('phone')

        try:
            validate_email(email)
        except:
            raise serializers.ValidationError('enter valid email')

        if not username.isalnum():
            raise serializers.ValidationError('enter valid username')

        if not phone.isnumeric() or len(phone)>12:
            raise serializers.ValidationError('phone number is too length or has not numeric symbols')

        if not (first_name.isalpha() and last_name.isalpha() ):
            raise serializers.ValidationError('Your first_name or last_name has not alphabetic symbols')

        return attrs


    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'phone')
        # fields = '__all__'
