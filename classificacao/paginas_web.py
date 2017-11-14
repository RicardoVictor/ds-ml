import csv

''' Codigo para classificar usuario em paginas web entre comprou e nao comprou '''

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


dados, marcacoes = carregar_acessos()

print(dados)
print(marcacoes)