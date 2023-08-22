from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from server.apps.users.serializers import TokenSerializer, UserLoginSerializer


class AuthUserController(TokenObtainPairView):
    serializer_class = TokenSerializer

    def post(self, request, *args, **kwargs):
        username = request.data.get("username", "")
        password = request.data.get("password", "")
        user = authenticate(username=username, password=password)

        if user:
            login_serializer = self.serializer_class(data=request.data)
            if login_serializer.is_valid():
                user_serializer = UserLoginSerializer(user)

                data = {
                    "token": {
                        "access": login_serializer.validated_data.get("access"),
                        "refresh": login_serializer.validated_data.get("refresh"),
                    },
                    "user": {
                        **user_serializer.data,
                    },
                }

                return Response(data, status=201)
            return Response(
                {"error": "Correo o contraseña incorrectos"},
                status=400,
            )
        return Response(
            {"error": "Correo o contraseña incorrectos"},
            status=400,
        )
