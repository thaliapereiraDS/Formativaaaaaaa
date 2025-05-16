from django.urls import path
from .views import (
    Login,
    UsuarioCreateAPIView,
    ProfessorListCreateApiView,
    ProfessorRetrieveUpdateDestroy,
    ReservaRetrieveUpdateDestroyAPIView,
    ReservadeAmbientesListCreateApiView,
    DisciplinaListCreateAPIView,
    DisciplinaRetrieveUpdateDestroyAPIView
)

urlpatterns = [
    path('login/', Login.as_view(), name='login'), 

    # Usuários
    path('usuarios/', UsuarioCreateAPIView.as_view(), name='criar_usuario'), 
    path('professor/', ProfessorListCreateApiView.as_view(), name='listar_criar_professor'),
    path('professor/<int:pk>/', ProfessorRetrieveUpdateDestroy.as_view(), name='editar_professor'), 

    # Reservas
    path('reservas/', ReservadeAmbientesListCreateApiView.as_view(), name='listar_criar_reservas'),
    path('reservas/<int:pk>/', ReservaRetrieveUpdateDestroyAPIView.as_view(), name='reserva_detalhe'),# get, put,PATCH, DELETE

    # Disciplinas
    path('disciplinas/', DisciplinaListCreateAPIView.as_view(), name='listar_criar_disciplinas'), 
    path('disciplinas/<int:pk>/', DisciplinaRetrieveUpdateDestroyAPIView.as_view(), name='disciplina_detalhe'),
]
