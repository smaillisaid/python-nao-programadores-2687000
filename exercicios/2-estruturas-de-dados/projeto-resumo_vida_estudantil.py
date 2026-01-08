# Nesse exercício coletaremos dados de uma estudante, armazenaremos em um dicionário e imprimiremos na tela esse dados em um formato amigável.
estudante = {}
# 1. Solicite a estudante os seguintes dados: nome, ano que conheceu o LinkedIn, ano atual e os cursos realizados no LinkedIn Learning separados por virgula em ordem cronológica
estudante['nome'] = input("Informe seu nome: ")
estudante['ano_conheceu_LinkedIn'] = int(input("Informe o ano quem que você conheceu o LinkedIn: "))
estudante['ano_atual'] = int(input("Informe o ano atual: "))
cursos_realizados = input("Informe os cursos realizados no LinkedIn Learning, separados por vírgual e em ordem cronológica: ")
# 2. Armazene esses dados em um dicionário
estudante['cursos_realizados'] = cursos_realizados.split(', ')
print(estudante.values())
# 3. Imprima na tela uma string com as informações de nome, ano_conheceu_linkedin, total de anos transcurridos, total de cursos realizados e (apenas) o primeiro e último curso.
print(f"O estudante {estudante['nome']} conhece o LinkedIn desde {estudante['ano_conheceu_LinkedIn']}, totalizando {estudante['ano_atual'] - estudante['ano_conheceu_LinkedIn']} anos. Durante este tempo, realizou um total de {len(estudante['cursos_realizados'])} cursos, onde o primeiro curso realizado foi {estudante['cursos_realizados'][0]} e o último curso realizado, até o momento, foi {estudante['cursos_realizados'][-1]}.")