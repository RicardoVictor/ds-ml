from sklearn.naive_bayes import MultinomialNB

''' Exemplo de codigo para classificar animais entre cachorro e porco '''

# e gordinho? tem perna curta? faz auau?
porco1 =    [1, 1, 0]
porco2 =    [1, 1, 0]
porco3 =    [1, 1, 0]
cachorro1 = [1, 1, 1]
cachorro2 = [0, 0, 1]
cachorro3 = [0, 1, 1]

dados = [porco1, porco2, porco3, cachorro1, cachorro2, cachorro3]

# porco = 1, cachorro = -1
marcacoes = [1, 1, 1, -1, -1, -1]

modelo = MultinomialNB()
modelo.fit(dados, marcacoes)

nao_sei_1 = [1, 1, 1]
nao_sei_2 = [1, 0, 0]
nao_sei_3 = [0, 0, 1]

testes = [nao_sei_1, nao_sei_2, nao_sei_3]
marcacoes_teste = [-1, 1, 1]

resultado = modelo.predict(testes)
erros = resultado - marcacoes_teste

total_de_elementos = len(testes)
total_de_acertos = len([erro for erro in erros if erro==0])
total_de_erros = len([erro for erro in erros if erro!=0])

print('minhas marcacoes:', marcacoes_teste)
print('resultado:', resultado)
print('erros:', erros)
print('taxa de erro:', 100*total_de_erros/total_de_elementos, '%')
print('taxa de acerto:', 100*total_de_acertos/total_de_elementos, '%')