from django.core.mail import send_mail
from rest_framework import generics, status, views, permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from .models import User
from .serializers import RegisterSerializer, LoginSerializer, LogoutSerializer, VerifyEmailSerializer, \
    VerificationCodeCheckSerializer


# Create your views here.

class RegisterView(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request):
        user = request.data
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        user_data = serializer.data
        return Response(user_data, status=status.HTTP_201_CREATED)


class LoginAPIView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class LogoutAPIView(generics.GenericAPIView):
    serializer_class = LogoutSerializer

    # permission_classes = (permissions.IsAuthenticated,)  # Elbekdan so'rimiz

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_204_NO_CONTENT)




class VerifyEmail(generics.GenericAPIView):
    serializer_class = VerifyEmailSerializer

    def post(self, request):
        email = request.data.get('email')
        if email in User.objects.values_list('email', flat=True):
            user = User.objects.get(email='user@example.com')

            # send mail to user.email
            # send_mail(
            #     'Verification code',
            #     f'{user.verification_code}',
            #     'from@example.com',
            #     [f'{email}'],
            #     fail_silently=False,
            # )

            return Response({f'{email}': 'exists',
                             'message': 'Please check your email adress for verification code'},
                            status=status.HTTP_200_OK)
        else:
            return Response({f'{email}': 'does not exist',
                             'message': 'Please make sure that you entered correct email adress'},
                            status=status.HTTP_400_BAD_REQUEST)


class VerificationCodeCheck(generics.GenericAPIView):
    serializer_class = VerificationCodeCheckSerializer

    def post(self, request):
        user = request.user
        if request.data.get('code') == user.verification_code:
            user.email_verified = True
            return Response({'user': 'verified'}, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'incorrect code'}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def password_reset(request):
    data = request.data
    if data['password'] == data['password_confirm']:
        user = request.user
        user = User.objects.get(id=user.id)
        user.password = data['password']
        return Response({"message": "You successfully changed your password"}, status=200)
    else:
        return Response({"message": "Please chech that the new password and password confirmation are the same"},
                        status=400)
