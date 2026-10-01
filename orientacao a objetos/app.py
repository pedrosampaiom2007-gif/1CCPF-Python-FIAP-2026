# app.py

from aluno import Aluno
from disciplina import Disciplina

# criar/ instanciar
aluno1 = Aluno("joão", "123456", "Ciencia da computação")

## criar/ instanciar 2 disciplinas
sers = Disciplina("Soluçoes Renovaveis", "André")
dsa = Disciplina("Data structures", "Erick")

# Matricular o aluno nas disciplinas
aluno1.matriculas(sers)
aluno1.matriculas(dsa)
# print(aluno1.disciplinas[0].professor)

#atribuir notas de cada disciplina ao aluno
aluno1.adicionar_nota(sers,10)
aluno1.adicionar_nota(sers,8)
aluno1.adicionar_nota(dsa,8)
aluno1.adicionar_nota(dsa,6)

print(aluno1.calcula_media(dsa))