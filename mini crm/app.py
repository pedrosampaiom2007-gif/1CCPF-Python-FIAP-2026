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

    print(f"# | {"Nome":<15}| {"E-mail":<15} | Empresa")

    for i, lead in enumerate(leads):
        print(f"{i:02d} | {lead["name"]:<10} | {lead["email"]:<10} | {lead["company"]:<10}")
def search_leads():
    query= input("Buscar por: ").strip().lower()
    if not query:
        print("nenhuma busca arrogantchi")
        return

    # envia a query para o control realizar a busca no leads.json

    leads_finded= control.read_leads_search(query)

    print(f"# | {"Nome":<15}| {"E-mail":<15} | Empresa")

    for i, lead in leads_finded:
        print(f"{i:02d} | {lead["Name"]:<10} | {lead["email"]:<10} | {lead["company"]:<10}")



def export_leads():
    path_csv= control.export_csv()
    if path_csv is None:
        print("Não foi possível exportar os leads")
    else:
        print(f"Exportado para {path_csv}")
        return

def main():
    while True:
        print("\n Mini CRM de leads")
        print("\n [1] Adicionar leads")
        print("\n [2] Listar leads")
        print("\n [3] Buscar (nome/e-mail/empresa)")
        print("\n [4] Exportar CSV")
        print("\n [0] Sair do programa")

        option = input("Escolhe uma opção: ")

        if option == '1':
            add_lead()

        elif option == '2':
            list_leads()
        elif option == '3':
            search_leads()
        elif option == '4':
            export_leads()
        elif option == '0':
            print("\n Até mais...")
            break
        else:
            print("Opção invalida")

if __name__ == "__main__":
    main()