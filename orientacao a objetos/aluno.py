# aluno.py

from disciplina import Disciplina
class Aluno:
    def __init__(self, nome, rm, curso):
        self.nome = nome
        self.rm = rm
        self.curso = curso
        self.disciplinas = []       #[Disciplina,disciplina,:]
        self.notas_por_disciplinas = {} #[nome da disciplina":[nota,nota,

    def matriculas(self, disciplina: Disciplina):
        self.disciplinas.append(disciplina)
        self.notas_por_disciplinas.setdefault(disciplina.nome, [])

    # ATRIBUIR  NOTAS DE CADA DISCIPLINA AO ALUNO
    def adicionar_nota(self, disciplina: Disciplina, nota: float):
        self.notas_por_disciplinas[disciplina.nome].append(nota)

    def calcula_media(self,d:Disciplina) -> float:
        notas = self.notas_por_disciplinas.get(d.nome,[])
        if not notas:
            return 0
        return sum(notas)/len(notas)

    def calcular_media_g(self)->float:
        medias=[]
        for d in self.disciplinas:
            media_d=self.calcula_media(d)
            medias.append(media_d)

        return sum(medias)/len(medias)