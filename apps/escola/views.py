from django.http import JsonResponse
from rest_framework import viewsets
from apps.escola.models import Aluno, Curso
from apps.escola.serializer import AlunoSerializer, CursoSerializer

class AlunosViewSet(viewsets.ModelViewSet):
    """Exibindo todos os alunos e alunas"""

    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer

class CursosViewSet(viewsets.ModelViewSet):
    """Exibindo todos os Cursos"""

    queryset = Curso.objects.all()
    serializer_class = CursoSerializer