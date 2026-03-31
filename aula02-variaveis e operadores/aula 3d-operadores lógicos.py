#logica e (and)
verif_email= True
verif_senha = False

verifica_login= verif_senha and verif_email
print(verifica_login)

#logica ou (or)
Logica_ou=False or False or True
print(Logica_ou)

#not
negacap=not True
print(negacap)
if not verifica_login:
    print("loga certo aí...")
else:
    print("entra no programa")