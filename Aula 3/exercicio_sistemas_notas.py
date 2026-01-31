
print('SISTEMAS DE NOTAS')
print('....'*10) # pode-se usar multiplicação com letras e simbolos

nome_aluno = input('Nome do aluno: ')

n1_port = float(input('Nota Portugues: '))
n2_mat  = float(input('Nota Matematica: '))              
n3_ing  = float(input('Nota Ingles: '))


media = ((n1_port + n2_mat + n3_ing)/3)

print('Situação do Aluno: ')

aprovado = media >=7
reprovado = media <5
recuperacao = media >=5 and media <7

print('Aprovado', aprovado)
print('Reprovado', reprovado)
print('Recuparação', recuperacao)
