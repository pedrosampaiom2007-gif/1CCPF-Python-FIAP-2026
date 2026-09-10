from model import model_lead
import control

def add_lead():

    name = input("Digite o nome do usuáro: ")
    email = input("Digite o email do usuário: ")
    company=input("Empresa: ")
    step=input("Etapa de vendas: ")

    #Validar as entradas do usuário
    # depois de validar...vamos modelar os dados

    print(model_lead(name,email,company,step))
    #depois de modelado... vamos enviar esse dict(leads) para o leads.json
    #para salvar,vamos usar o módulo control
    control.create_lead(model_lead(name,email,company,step))

    print("Lead adicionado(func)")
def list_leads():
    leads = control.read_leads()
    if not leads:
        print("nenhum lead ainda")
        return
def main():
    while True:
        print("\n Mini CRM de leads")
        print("\n [1] Adicionar leads")
        print("\n [2] Listar leads")
        print("\n [0] Sair do programa")

        option = int(input("Escolhe uma opção: "))

        if option == 1:
            add_lead()

        elif option == 2:
            list_leads()
        elif option == 0:
            print("\n Até mais...")
            break
        else:
            print("Opção invalida")

if __name__ == "__main__":
    main()