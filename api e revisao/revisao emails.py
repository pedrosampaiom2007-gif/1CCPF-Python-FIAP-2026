email = "joao.silva@fiap.com.br, maria.souza@gmail.com.br, ana.paula@fiap.com.br"

lista_emails=email.split(",")
lista_limpa=[]

for i in lista_emails:
    lim=i.strip()

    lista_limpa.append(lim)

d=dict()

for j in lista_limpa:

    sep=j.split("@")
    dominio=sep[1]

    if dominio not in d:

     d[dominio]=1
    else:

     d[dominio]+=1




usuario=[]
for k in lista_limpa:

    sepa=k.split("@")
    nome=sepa[0]
    result=usuario.append(nome)

tupla=tuple(usuario)




primeiro=tupla[0]
ultimo=tupla[-1]

primeiro,ultimo=ultimo,primeiro



tupla_nova = (ultimo,) + tupla[1:-1] + (primeiro,)
print("|"*100)
print("-----------------------------------RELATÓRIO---------------------------------")
print("|"*100)

print(f"Há {d["fiap.com.br"]} emails com o domínio da Fiap e {d["gmail.com.br"]} com o domínio de Gmail\n")

print(f"Os usuários são: {tupla}\n")

print(f"Após a troca de ordem, a lista dos usuários ficou assim:{tupla_nova}\n")
