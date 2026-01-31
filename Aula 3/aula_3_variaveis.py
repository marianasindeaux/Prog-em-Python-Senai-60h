
#### AULA 3 - Variaveis e Constantes

# Sinal de = é uma atribuição

# variaveis - letras minusculas (dados que podem ser alterados)

numero = 100

numero = 150

print(numero)

# concatenar - juntar variaveis (usar sempre virgula para juntar os valores)

nome = 'mariana'
sobrenome = 'sindeaux'

print(nome , sobrenome)

# funções casting -  str | float |  int |  bool (altera o tipo de dado)

nome = 'Carla'
idade = 25
cidade  =  'Guarulhos'
estado = 'SP'
curso = 'Python60'
casada_ = True 
dado = bool(nome)
print(dado)

print('nome:', nome)
print('idade:', idade)
print('cidade:', cidade)
print('estado:', estado)
print('curso:', curso)

dado_3 =  float(idade)
print(dado_3)


dado_4 = int(casada_)
print(dado_4)


# Operadores Aritmeticos

print(100 +  200) # Adição
print(10 - 100) # Subtração
print(10 * 100) # Multiplicação
print(10 / 100) # Divisão
print(10 // 100) # Divisão Inteira
print(10 ** 10) # Potencia
print(10 % 100) # Modulo (resto da conta de divisão


# Operadores Logicos

n1 = 10
n2 = 5

print(n1  >  n2) # maior
print(n1  <  n2) # Menor
print(n1  >= n2) # Maior ou igual
print(n1  <= n2) # Menor ou igual
print(n1  !=  n2) # Diferente
print(n1 == n2) # Igual

# Ordem de Processamento

#Parentes
#Exponenciação
#Multiplicação
#Divisão
#Adição
#Subtração

# Pular linhas

# - print vazio

nome: Mariana

print('Seja bem vindo: ', nome)
print()
print( 'cadastre seus dados: ')

# - usar f''' ( tudo oq tiver dentro das aspas será processado igual)
print(f'''

Seja bem vindo, {nome}

Cadastre seus dados:

''')



