from sklearn.naive_bayes import MultinomialNB

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

nao_sei1 = [1, 1, 1]
nao_sei2 = [1, 0, 0]
nao_sei3 = [0, 0, 0]

teste = [nao_sei1, nao_sei2, nao_sei3]

print(modelo.predict(teste))