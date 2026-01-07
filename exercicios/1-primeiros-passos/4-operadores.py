ano_nascimento = 1989
ano_formatura = 2010

# Considerando que as variáveis acima correspondem a 'Gerlaine', descubra a idade dela no ano da sua formatura
idade_formatura = ano_formatura - ano_nascimento
print(idade_formatura)

# Escreva expressões comparativas usando os operadores relacionais >, <= e ==. Imprima na tela as respostas
print(ano_formatura > ano_nascimento)
print(ano_nascimento <= ano_formatura)
print(ano_nascimento == ano_formatura)

# Crie expressões comparativas mais complexas utilizando operadores lógicos and, or e not. Imprima na tela as respostas
if(ano_formatura > ano_nascimento and idade_formatura >= 20):
    print(f'O ano de formatura {ano_formatura} é maior que o ano de nascimento {ano_nascimento} e a idade de formatura é maior que 20 - '+str(True))
else:
    print(False)
if(ano_formatura > 2000 or ano_nascimento < 1990):
    print(str(True)+f' Ou o ano de formatura {ano_formatura} é maior que 2000 ou o ano de nascimento {ano_nascimento} é menor que 1990')
else:
    print(False)
