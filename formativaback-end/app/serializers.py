from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth import get_user_model
from .models import Usuario, Reservar_de_Ambiente, Disciplina


class LoginSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        data['username'] = self.user.username
        data['is_gestor'] = self.user.is_gestor
        data['is_professor'] = self.user.is_professor
        return data

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['id', 'username', 'email', 'password', 'is_gestor', 'is_professor']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        print(validated_data)
        user = get_user_model().objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email', ''),
            password=validated_data['password'],
            is_gestor=validated_data.get('is_gestor', False),
            is_professor=validated_data.get('is_professor', False),
        )
        return user
    

    def update(self, instance, validated_data):
        user = super().update(instance, validated_data)
        try:
            user.set_password(validated_data['password'])
            user.save()
        except KeyError:
            pass
        return user
    

# Reservas
class ReservaAmbientesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservar_de_Ambiente
        fields = '__all__'

# Disciplinas
class DisciplinaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Disciplina
        fields = '__all__'
