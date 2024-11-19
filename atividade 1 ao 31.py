1) 
# Exibe a mensagem na tela
print("Olá, Mundo!")

resolução 
Olá, Mundo!

2) 
# Exibe a mensagem de boas-vindas
print(f"Olá {nome}, é um prazer te conhecer!")

resolução 
Olá Emilly, é um prazer te conhecer!

3)
# Solicita o nome e o salário do funcionário
nome = input("Nome do Funcionário: ")
salario = float(input("Salário: "))
# Exibe a mensagem formatada
print(f"O funcionário {nome} tem um salário de R${salario:.2f} em Junho.")

resolução 
Nome do Funcionário: 
emilly
Salário: 
1412
O funcionário emilly tem um salário de R$1412.00 em Junho.

4)
# Solicita dois números inteiros ao usuário
numero1 = int(input("Digite um valor: "))
numero2 = int(input("Digite outro valor: "))
# Calcula a soma
soma = numero1 + numero2
# Exibe o resultado
print(f"A soma entre {numero1} e {numero2} é igual a {soma}.")

resolução 
Digite um valor: 
200
Digite outro valor: 
500
A soma entre 200 e 500 é igual a 700.

5) 
# Solicita as duas notas ao usuário
nota1 = float(input("Nota 1: "))
nota2 = float(input("Nota 2: "))
# Calcula a média
media = (nota1 + nota2) / 2
# Exibe o resultado
print(f"A média entre {nota1} e {nota2} é igual a {media:.1f}")

resolução 
Nota 1: 
90
Nota 2: 
20
A média entre 90.0 e 20.0 é igual a 55.0

6) 
# Solicita um número inteiro ao usuário
numero = int(input("Digite um número: "))
# Calcula o antecessor e o sucessor
antecessor = numero - 1
sucessor = numero + 1
# Exibe os resultados
print(f"O antecessor de {numero} é {antecessor}")
print(f"O sucessor de {numero} é {sucessor}")

resolução
Digite um número: 
55
O antecessor de 55 é 54
O sucessor de 55 é 56

7) 
# Solicita um número real ao usuário
numero = float(input("Digite um número: "))
# Calcula o dobro e a terça parte
dobro = numero * 2
terca_parte = numero / 3
# Exibe os resultados
print(f"O dobro de {numero} é {dobro}")
print(f"A terça parte de {numero} é {terca_parte:.5f}")

resolução 
Digite um número: 
70
O dobro de 70.0 é 140.0
A terça parte de 70.0 é 23.33333

8) 
# Solicita a distância em metros ao usuário
metros = float(input("Digite uma distância em metros: "))
# Calcula as conversões
km = metros / 1000           # Quilômetros
hm = metros / 100            # Hectômetros
dam = metros / 10            # Decâmetros
dm = metros * 10             # Decímetros
cm = metros * 100            # Centímetros
mm = metros * 1000           # Milímetros
# Exibe os resultados
print(f"A distância de {metros}m corresponde a:")
print(f"{km}Km")
print(f"{hm}Hm")
print(f"{dam}Dam")
print(f"{dm}dm")
print(f"{cm}cm")
print(f"{mm}mm")

resolução 
Digite uma distância em metros: 
200
A distância de 200.0m corresponde a:
0.2Km
2.0Hm
20.0Dam
2000.0dm
20000.0cm
200000.0mm

9) 
# Solicita a quantidade de dinheiro em reais ao usuário
reais = float(input("Quanto dinheiro você tem na carteira (em R$): "))
# Conversão para dólares
dolares = reais / 3.45
# Exibe o resultado
print(f"Com R${reais:.2f}, você pode comprar US${dolares:.2f}.")

resolução 
Quanto dinheiro você tem na carteira (em R$): 
200
Com R$200.00, você pode comprar US$57.97.

10) 
# Solicita a largura e a altura da parede
largura = float(input("Digite a largura da parede (em metros): "))
altura = float(input("Digite a altura da parede (em metros): "))
# Calcula a área da parede
area = largura * altura
# Calcula a quantidade de tinta necessária (1 litro cobre 2 m²)
quantidade_tinta = area / 2
# Exibe os resultados
print(f"A área a ser pintada é {area} m².")
print(f"A quantidade de tinta necessária é {quantidade_tinta} litros.")

resolução 
Digite a largura da parede (em metros): 
50
Digite a altura da parede (em metros): 
80
A área a ser pintada é 4000.0 m².
A quantidade de tinta necessária é 2000.0 litros.

11)
# Solicita os coeficientes A, B e C da equação do segundo grau
A = float(input("Digite o valor de A: "))
B = float(input("Digite o valor de B: "))
C = float(input("Digite o valor de C: "))
# Calcula o valor de Delta
delta = (B ** 2) - (4 * A * C)
# Exibe o resultado
print(f"O valor de Delta é {delta}.")

resolução 
Digite o valor de A: 
1
Digite o valor de B: 
20
Digite o valor de C: 
80
O valor de Delta é 80.0.

12) 
# Solicita o preço do produto
preco = float(input("Digite o preço do produto: "))
# Calcula o preço promocional com 5% de desconto
desconto = preco * 0.05
preco_promocional = preco - desconto
# Exibe o resultado
print(f"O preço promocional é R${preco_promocional:.2f}.")

resolução 
Digite o preço do produto: 
29.99
O preço promocional é R$28.49.

13) 
# Solicita o salário do funcionário
salario = float(input("Digite o salário do funcionário: "))
# Calcula o novo salário com 15% de aumento
aumento = salario * 0.15
novo_salario = salario + aumento
# Exibe o resultado
print(f"O novo salário com 15% de aumento é R${novo_salario:.2f}.")

resolução 
Digite o salário do funcionário: 
500
O novo salário com 15% de aumento é R$575.00.

14) 
# Solicita a quantidade de Km percorridos e os dias de aluguel
km_percorridos = float(input("Digite a quantidade de Km percorridos: "))
dias_alugados = int(input("Digite a quantidade de dias que o carro foi alugado: "))
# Calcula o preço total
preco_por_dia = 90
preco_por_km = 0.20
custo_total = (dias_alugados * preco_por_dia) + (km_percorridos * preco_por_km)
# Exibe o resultado
print(f"O preço total a pagar é R${custo_total:.2f}.")

resolução
Digite a quantidade de Km percorridos: 
13
Digite a quantidade de dias que o carro foi alugado: 
7
O preço total a pagar é R$632.60.

15) 
# Solicita o número de dias trabalhados
dias_trabalhados = int(input("Digite o número de dias trabalhados no mês: "))
# Cálculo do salário
horas_por_dia = 8
valor_por_hora = 25
salario = dias_trabalhados * horas_por_dia * valor_por_hora
# Exibe o resultado
print(f"O salário do funcionário é R${salario:.2f}.")

resolução 
Digite o número de dias trabalhados no mês: 
20
O salário do funcionário é R$4000.00.

16) 
# Solicita a quantidade de cigarros fumados por dia e quantos anos fumou
cigarros_por_dia = int(input("Quantos cigarros você fuma por dia? "))
anos_fumando = int(input("Quantos anos você fumou? "))
# Calcula a redução de vida em minutos
minutos_perdidos_por_cigarro = 10
total_cigarros = cigarros_por_dia * 365 * anos_fumando
tempo_perdido = total_cigarros * minutos_perdidos_por_cigarro
# Converte para dias
dias_perdidos = tempo_perdido / (60 * 24)
# Exibe o resultado
print(f"Você perderá aproximadamente {dias_perdidos:.2f} dias de vida.")

resolução 
Quantos cigarros você fuma por dia? 
5
Quantos anos você fumou? 
3
Você perderá aproximadamente 38.02 dias de vida.

17) 
velocidade=  float(input("informe a velocidade "))
if velocidade >80 :
    multa = (velocidade - 80) * 5
    print(F"Vlocidade acima de 80 km - Multa R$ {multa:.2f}")

resolução
informe a velocidade 
110
Vlocidade acima de 80 km - Multa R$ 150.00

18) 
ano_nascimento = int(input("Qual o seu ano de nascimento? "))
ano_atual = 2024
idade = ano_atual - ano_nascimento
print(f"Sua idade é {idade} anos.")
if idade >= 18:
    print("Você pode votar!")
else:
    print("Você não pode votar ainda.")

resolução
Qual o seu ano de nascimento? 
1999
Sua idade é 25 anos.
Você pode votar!

19) 
nome = input("Qual o nome do aluno? ")
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
media = (nota1 + nota2) / 2
print(f"A média de {nome} é {media:.2f}.")
if media >= 7:
    print("Bom aproveitamento!")
else:
    print("Não teve um bom aproveitamento.")

resolução

Qual o nome do aluno? 
emilly
Digite a primeira nota: 
10
Digite a segunda nota: 
6
A média de emilly é 8.00.
Bom aproveitamento!

20) 
numero = int(input("Digite um número inteiro: "))
if numero % 2 == 0:
    print("O número é PAR.")
else:
    print("O número é ÍMPAR.")

resolução
Digite um número inteiro: 
10
O número é PAR.

21)
ano = int(input("Digite um ano: "))
if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print(f"{ano} é um ano BISSEXTO.")
else:
    print(f"{ano} não é um ano BISSEXTO.")

resolução
Digite um ano: 
1999
1999 não é um ano BISSEXTO.

22)
ano_nascimento = int(input("Digite o seu ano de nascimento: "))
ano_atual = 2024
idade = ano_atual - ano_nascimento
if idade < 18:
    print(f"Faltam {18 - idade} anos para o seu alistamento militar.")
elif idade > 18:
    print(f"Você já deveria ter se alistado há {idade - 18} anos.")
else:
    print("Você deve se alistar este ano.")

resolução
Digite o seu ano de nascimento: 
2006
Você deve se alistar este ano.

23) 
nome = input("Qual o seu nome? ")
sexo = input("Qual o seu sexo (M/F)? ").upper()
valor_compras = float(input("Qual o valor das suas compras? R$"))
if sexo == "F":
    desconto = 0.13
    print(f"Você é mulher, então o desconto é de 13%.")
else:
    desconto = 0.05
    print(f"Você é homem, então o desconto é de 5%.")
valor_com_desconto = valor_compras * (1 - desconto)
print(f"Valor com desconto: R${valor_com_desconto:.2f}")

resolução
Qual o seu nome? 
emilly
Qual o seu sexo (M/F)? 
f
Qual o valor das suas compras? R$
10000
Você é mulher, então o desconto é de 13%.
Valor com desconto: R$8700.00

24)
distancia = float(input("Qual a distância da viagem em Km? "))
if distancia <= 200:
    preco = distancia * 0.50
else:
    preco = distancia * 0.45
print(f"O preço da passagem é R${preco:.2f}")

resolução
Qual a distância da viagem em Km? 
200
O preço da passagem é R$100.00

25) 
a = float(input("Digite o comprimento do primeiro segmento de reta: "))
b = float(input("Digite o comprimento do segundo segmento de reta: "))
c = float(input("Digite o comprimento do terceiro segmento de reta: "))

if a + b > c and a + c > b and b + c > a:
    print("Esses segmentos podem formar um triângulo.")
else:
    print("Esses segmentos NÃO podem formar um triângulo.")

resolução
Digite o comprimento do primeiro segmento de reta: 
10
Digite o comprimento do segundo segmento de reta: 
90
Digite o comprimento do terceiro segmento de reta: 
5
Esses segmentos NÃO podem formar um triângulo.

26)
n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))

if n1 > n2:
    print("O primeiro valor é o maior.")
elif n1 < n2:
    print("O segundo valor é o maior.")
else:
    print("Não existe valor maior, os dois são iguais.")

resolução
Digite o primeiro número: 
10
Digite o segundo número: 
6
O primeiro valor é o maior.

27) 
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
media = (nota1 + nota2) / 2

if media < 5:
    print("REPROVADO")
elif media < 7:
    print("RECUPERAÇÃO")
else:
    print("APROVADO")

resolução
Digite a primeira nota: 
10
Digite a segunda nota: 
10
APROVADO

28) 
largura = float(input("Digite a largura do terreno (em metros): "))
comprimento = float(input("Digite o comprimento do terreno (em metros): "))
area = largura * comprimento
print(f"A área do terreno é {area} m².")
if area < 100:
    print("Classificação: TERRENO POPULAR")
elif area <= 500:
    print("Classificação: TERRENO MASTER")
else:
    print("Classificação: TERRENO VIP")

resolução
Digite a largura do terreno (em metros): 
450
Digite o comprimento do terreno (em metros): 
500
A área do terreno é 225000.0 m².
Classificação: TERRENO VIP

29) 
nome = input("Digite o nome do funcionário: ")
salario = float(input("Digite o salário atual: R$"))
anos_trabalho = int(input("Quantos anos trabalha na empresa? "))
if anos_trabalho <= 3:
    aumento = 0.03
elif anos_trabalho <= 10:
    aumento = 0.125
else:
    aumento = 0.20
novo_salario = salario * (1 + aumento)
print(f"O novo salário de {nome} é R${novo_salario:.2f}")

resolução
Digite o nome do funcionário: 
emilly
Digite o salário atual: R$
20000
Quantos anos trabalha na empresa? 
10
O novo salário de emilly é R$22500.00

30) 
a = float(input("infome o valor do lado1= "))
b = float(input("infome o valor do lado2= "))
c = float(input("infome o valor do lado3= "))    
if a<b+c and b<a+c and c<a+b :
    print("os valores informados formam um trianculo")
    if a==b and a==c :
        print("equilátero")
    elif a!=b and a!=c and b!=c :
        print ("escaleno")
    else : 
        print("isósceles")
else :
    print("os valores informados não formam um trianculo")

resolução
infome o valor do lado1= 
10
infome o valor do lado2= 
50
infome o valor do lado3= 
60
os valores informados não formam um trianculo

31)
import random
opcoes = ["Pedra", "Papel", "Tesoura"]
jogador = input("Escolha Pedra, Papel ou Tesoura: ").capitalize()
computador = random.choice(opcoes)
print(f"Computador escolheu: {computador}")
if jogador == computador:
    print("Empate!")
elif (jogador == "Pedra" and computador == "Tesoura") or \
     (jogador == "Papel" and computador == "Pedra") or \
     (jogador == "Tesoura" and computador == "Papel"):
    print("Você venceu!")
else:
    print("Você perdeu!")

resolução
Escolha Pedra, Papel ou Tesoura: 
pedra
Computador escolheu: Tesoura
Você venceu!

32) 
