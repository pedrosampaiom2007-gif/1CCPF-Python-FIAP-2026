endpoints = ["/login", "/produtos", "/pedidos"]
status = [
[200, 200, 401, 200, 500],
[200, 200, 200, 200, 200],
[201, 500, 502, 201, 500]
    ]

def valida_erro(numero):
    if numero >=200 and numero<=299:
        return True
    else:
        return False

def identificador(numero,guarda):

    erro1=0
    erro2=0
    erro3=0

    for i in numero[0]:
        if i>299 or i<200:
            erro1+=1
    for i in numero[1]:
        if i>299 or i<200:
            erro2+=1
    for i in numero[2]:
        if i>299 or i<200:
            erro3+=1

    guarda=erro1,erro2,erro3

    return numero,guarda

print(identificador(status,endpoints))











