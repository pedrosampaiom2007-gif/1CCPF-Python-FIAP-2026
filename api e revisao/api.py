endpoints = ["/login", "/produtos", "/pedidos"]

status = [
    [200, 200, 401, 200, 500],
    [200, 200, 200, 200, 200],
    [201, 500, 502, 201, 500]
]


def calcular_sucesso(requisicoes):
    sucessos = 0

    for codigo in requisicoes:
        if 200 <= codigo < 300:
            sucessos += 1

    return (sucessos / len(requisicoes)) * 100


def contar_erros(requisicoes):
    erros = 0

    for codigo in requisicoes:
        if codigo >= 400:
            erros += 1

    return erros


def tem_erros_consecutivos(requisicoes):
    for i in range(len(requisicoes) - 1):
        if requisicoes[i] >= 400 and requisicoes[i + 1] >= 400:
            return True

    return False


def classificar(porcentagem, consecutivos):
    if consecutivos:
        return "CRÍTICO"
    elif porcentagem >= 80:
        return "ESTÁVEL"
    else:
        return "INSTÁVEL"


# Programa principal
erros = []

for i in range(len(endpoints)):
    endpoint = endpoints[i]
    requisicoes = status[i]

    porcentagem = calcular_sucesso(requisicoes)
    quantidade_erros = contar_erros(requisicoes)
    consecutivos = tem_erros_consecutivos(requisicoes)

    erros.append(quantidade_erros)

    classificacao = classificar(porcentagem, consecutivos)

    print(
        endpoint,
        f"- {porcentagem:.0f}% de sucesso - {classificacao}"
    )


# Endpoint com mais erros
indice = erros.index(max(erros))

print("Endpoint com mais erros:", endpoints[indice])