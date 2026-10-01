class Disciplina:
    def __init__(self, nome, professor):
        self.nome = nome
        self.professor = professor

    def exibir_info(self):
        print(f"Disciplina: {self.nome} | professor: {self.professor}")

    # TEMPORÁRIO
# prompt_ia = disciplina("Prompt & IA",  "Jorge")
# cs = disciplina("Computer Science","Mauricio ")
# print(prompt_ia.exibir_info())
# prompt_ia.exibir_info()
