from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth.password_validation import validate_password
from rest_framework.fields import CharField
from server.apps.users.models import User
from rest_framework import serializers


class TokenSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user: User):
        token = super().get_token(user)

        return token


class UserLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", 
                  "username", "email", 
                #   "roles", "branch",
                  )
        
class UserCreateSerializer(serializers.ModelSerializer):
    password = CharField(max_length=128, min_length=8, write_only=True)
    confirmPassword = CharField(max_length=128, min_length=8, write_only=True)

    def validate_confirmPassword(self, data):
        if data != self.initial_data["password"]:
            raise serializers.ValidationError("Las contraseñas no coinciden")
        validate_password(data)
        return data

    def create(self, validated_data):
        user: User = User.objects.create_user(
            username=validated_data["username"],
            password=validated_data["password"],
            first_name=validated_data["first_name"],
            last_name=validated_data["last_name"],
            email=validated_data["email"],
        )
        user.save()
        return user

    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "password",
            "confirmPassword",
            "first_name",
            "last_name",
            "email",
        )


class ChangePasswordSerializer(serializers.ModelSerializer):
    currentPassword = CharField(max_length=128, write_only=True)
    newPassword = CharField(max_length=128, min_length=8, write_only=True)
    confirmPassword = CharField(max_length=128, min_length=8, write_only=True)

    def validate_currentPassword(self, value):
        user = self.context["request"].user
        if not user.check_password(value):
            raise serializers.ValidationError("La contraseña no coincide con la actual")
        return value

    def validate_confirmPassword(self, data):
        if data != self.initial_data["newPassword"]:
            raise serializers.ValidationError("Las contraseñas no coinciden")
        validate_password(data, self.context["request"].user)
        return data

    def save(self, **kwargs):
        password = self.validated_data["newPassword"]
        user = self.context["request"].user

        user.set_password(password)
        user.save()
        return user

    class Meta:
        model = User
        fields = ("currentPassword", "newPassword", "confirmPassword")


class ChangePasswordUserSerializer(serializers.Serializer):
    newPassword = CharField(max_length=128, min_length=8, write_only=True)
    confirmPassword = CharField(max_length=128, min_length=8, write_only=True)

    def validate_confirmPassword(self, data):
        from django.contrib.auth.password_validation import validate_password

        if data != self.initial_data["newPassword"]:
            raise serializers.ValidationError("Las contraseñas no coinciden")
        validate_password(data, self.context["request"].user)
        return data
