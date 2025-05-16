from django.shortcuts import render
from .models import Reservar_de_Ambiente, Usuario, Disciplina
from .serializers import (
    LoginSerializer,
    UsuarioSerializer,
    ReservaAmbientesSerializer,
    DisciplinaSerializer
)

from rest_framework.generics import (
    ListCreateAPIView,
    CreateAPIView,
    RetrieveUpdateDestroyAPIView
)
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView
from .permissions import IsGestor, IsProfessor


# -------------------- loginnnnnnnnnnnnnnnnnnnn --------------------

class Login(TokenObtainPairView):
    serializer_class = LoginSerializer


# -------------------- usuariosssssssssssssssssssss --------------------

class UsuarioCreateAPIView(CreateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer


class ProfessorListCreateApiView(ListCreateAPIView):
    queryset = Usuario.objects.filter(is_professor=True)
    serializer_class = UsuarioSerializer
    permission_classes = [IsAuthenticated, IsGestor]

    def get_queryset(self):
        queryset = super().get_queryset()
        nome = self.request.query_params.get('nome')
        if nome:
            queryset = queryset.filter(username__icontains=nome)
        return queryset


class ProfessorRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    permission_classes = [IsAuthenticated, IsGestor]


# -------------------- reservassssss --------------------

class ReservadeAmbientesListCreateApiView(ListCreateAPIView):
    serializer_class = ReservaAmbientesSerializer
    permission_classes = [IsAuthenticated, IsGestor | IsProfessor]

    def get_queryset(self):
        user = self.request.user
        if user.is_gestor:
            return Reservar_de_Ambiente.objects.all()
        elif user.is_professor:
            return Reservar_de_Ambiente.objects.filter(professor_responsavel=user)
        return Reservar_de_Ambiente.objects.none()


class ReservaRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = ReservaAmbientesSerializer
    permission_classes = [IsAuthenticated, IsGestor | IsProfessor]

    def get_queryset(self):
        user = self.request.user
        if user.is_gestor:
            return Reservar_de_Ambiente.objects.all()
        elif user.is_professor:
            return Reservar_de_Ambiente.objects.filter(professor_responsavel=user)
        return Reservar_de_Ambiente.objects.none()


# -------------------- disciplinaaaaaaaaaaas --------------------

class DisciplinaListCreateAPIView(ListCreateAPIView):
    serializer_class = DisciplinaSerializer
    def get_permissions(self):
         if self.request.method == 'GET':
            return [IsAuthenticated()]
         return [IsAuthenticated(), IsGestor()]

    def get_queryset(self):
        user = self.request.user
        if user.is_gestor:
            return Disciplina.objects.all()
        elif user.is_professor:
            return Disciplina.objects.filter(professor_disciplina=user)
        return Disciplina.objects.none()

    def perform_create(self, serializer):
        user = self.request.user
        if user.is_professor:
            serializer.save(professor_disciplina=user)
        else:
            serializer.save()


class DisciplinaRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = DisciplinaSerializer

    def get_permissions(self):
         if self.request.method == 'GET':
            return [IsAuthenticated()]
         return [IsAuthenticated(), IsGestor()]

    def get_queryset(self):
        user = self.request.user
        if user.is_gestor:
            return Disciplina.objects.all()
        elif user.is_professor:
            return Disciplina.objects.filter(professor_disciplina=user)
        return Disciplina.objects.none()
