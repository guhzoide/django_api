from django.contrib import admin
from apps.escola.models import Aluno, Curso, Matricula

class ListandoAlunos(admin.ModelAdmin):
    list_display = ('id', 'nome', 'rg', 'cpf', 'data_nascimento')
    list_display_links = ('id', 'nome')
    search_fields = ('nome',)
    list_per_page = 20

admin.site.register(Aluno, ListandoAlunos)

class ListandoCursos(admin.ModelAdmin):
    list_display = ('id', 'nome_curso', 'codigo_curso', 'descricao', 'nivel')
    list_display_links = ('id', 'nome_curso')
    search_fields = ('nome_curso', 'codigo_curso', 'nivel')
    list_per_page = 20

admin.site.register(Curso, ListandoCursos)

class ListandoMatriculas(admin.ModelAdmin):
    list_display = ('id', 'aluno', 'curso', 'periodo')
    list_display_links = ('id', 'aluno')
    list_per_page = 20

admin.site.register(Matricula, ListandoMatriculas)