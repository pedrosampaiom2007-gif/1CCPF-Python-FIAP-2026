from sqlalchemy.sql.operators import truediv

num1 = 5
num2 = 2
print(type(num1),type(num2))
resultado=num1 / num2
print(resultado, type(resultado))

#OPERADORES DE ATRIBUIÇÃO
num=15
print()# pular ums linha

num= num +2
print(num)

num-=2 #acumulador
print(num)

#OPERADORES RELACIONAIS
print()
print(6<2)

idade=21
print(idade== 20) # esses dois iguais servem para falar se essa informação é true ou false

logado= True
print(logado,type(logado))

maior_idade=idade>=18
print(maior_idade,type(maior_idade))

#strings

nome1= "marcos"
nom2= "Marcos"

print(nome1.upper)
