escolha_usuario=444
#0-> sair do programa
#1-> entrar no programa
#>>>>> erro!!
match escolha_usuario:
    case 0:
        print("sair do programa")
    case 1:
        print("entrar no programa")
    case _:
         print("erro!!!")