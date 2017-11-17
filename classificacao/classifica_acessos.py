from sklearn.naive_bayes import MultinomialNB
import csv

''' Codigo para classificar usuarios em paginas web entre comprou e nao comprou '''

# a abordagem utilizada foi:
# 90% para treino e 10% para teste 
# taxa e acerto encontrada: 88.89%

def carregar_acessos():
    
    X = []
    Y = []

    arquivo = open('acesso.csv', 'r')
    leitor = csv.reader(arquivo)
    next(leitor)

    for acessou_home,acessou_faq,acessou_area_de_contato,comprou in leitor:
        X.append([int(acessou_home),int(acessou_faq),int(acessou_area_de_contato)])
        Y.append(int(comprou))
    
    return X, Y


X, Y = carregar_acessos()

dados_treino = X[:90]
marcacoes_treino = Y[:90]

dados_teste = X[-9:]
marcacoes_teste = Y[-9:]

modelo = MultinomialNB()
modelo.fit(dados_treino, marcacoes_treino)

predicoes = modelo.predict(dados_teste)

quantidade_acertos = len([i for i in range(len(predicoes)) if predicoes[i] == marcacoes_teste[i]])

print('quantidade acertos:', quantidade_acertos)
print('quantidade casos:', len(dados_teste))
print('taxa de acerto:', quantidade_acertos*100/len(dados_teste))

