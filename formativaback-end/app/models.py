from django.db import models

from django.db import models

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.utils import timezone

class Usuario(AbstractUser):
    data_nascimento = models.DateField(blank=True, null=True)
    idade = models.PositiveIntegerField(blank=True, null=True)
    is_gestor = models.BooleanField(default=False)
    is_professor = models.BooleanField(default=False)
    def __str__(self):
        return self.username




class Disciplina(models.Model):
    choices_disciplinas = [
        ('PBE', 'Programação Back-end'),
        ('PWFE', 'Programação web front-end'),
        ('BCD', 'Banco de dados'),
        ('LIMA', 'Linguagem de marcação'),
        ('PRO', 'Projetos'),
        ('ELEB', 'Eletricidade Básica'),
        ('ELET', 'Eletrônica Analógica'),
        ('EDIG', 'Eletrônica Digital'),
        ('AUT', 'Automação Industrial'),
        ('INST', 'Instalações Elétricas'),
        ('ROBO', 'Robótica'),
        ('ECL', 'Circuitos Elétricos'),
        ('PLCL', 'Controladores Lógicos Programáveis'),
        ('MOTO', 'Máquinas e Motores Elétricos'),
        ('DESM', 'Desenho Mecânico'),
        ('MET', 'Metrologia'),
        ('MATE', 'Materiais de Engenharia'),
        ('MECG', 'Mecânica Geral'),
        ('SOLD', 'Soldagem'),
        ('FRES', 'Fresagem e Tornearia'),
        ('CNC', 'Comandos Numéricos Computadorizados'),
        ('CAD', 'Desenho Assistido por Computador (CAD)'),
    ]

    choices_cursos = [
        ('CAD', 'MECATRONICA'),
        ('DS', 'DESENVOLVIMENTO DE SISTEMAS'),
        ('CAI', 'ELETRICA')
    ]
    
    nome = models.CharField(max_length=4, choices=choices_disciplinas)
    curso = models.CharField(max_length=4, choices=choices_cursos)
    carga_horaria = models.PositiveIntegerField(blank=True, null=True)
    descricao = models.TextField(max_length=500)
    professor_disciplina = models.ForeignKey(Usuario, on_delete=models.CASCADE, limit_choices_to={'is_professor': True})


class Reservar_de_Ambiente(models.Model):
    def validador(valor):
        if valor < timezone.now().date():
            raise ValidationError('A data não pode ser no passado')
    
    choices_periodo = [
        ('AM', 'Manhã'),
        ('PM', 'Tarde'),
        ('NI', 'Noturno')
    ]
    
    data_inicio = models.DateField(validators=[validador])
    data_termino = models.DateField(validators=[validador])
    periodo = models.CharField(max_length=2, choices=choices_periodo, blank=True, null=True)
    sala_reservado = models.CharField(max_length=30, blank=True, null=True)
    professor_responsavel = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    disciplina_associada = models.ForeignKey(Disciplina, on_delete=models.CASCADE)

