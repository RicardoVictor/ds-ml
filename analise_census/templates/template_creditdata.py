import pandas as pd

# Carregamento do dataset
base = pd.read_csv('../datasets/credit_data.csv')
base.loc[base.age < 0, 'age'] = 40.92

# Separação do dataset em previsores e classe
previsores = base.iloc[:, 1:4].values
classe = base.iloc[:, 4].values

# Tratamento dos valores faltantes com a estratégia da média
from sklearn.preprocessing import Imputer
imputer = Imputer(missing_values='NaN', strategy='mean', axis=0)
imputer = imputer.fit(previsores[:, 1:4])
previsores[:, 1:4] = imputer.transform(previsores[:, 1:4])

# Normalização
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
previsores = scaler.fit_transform(previsores)

from sklearn.cross_validation import train_test_split

# Divisao da base em treinamento e teste
previsores_treinamento, previsores_teste, classe_treinamento, classe_teste = train_test_split(previsores, classe, test_size=0.25, random_state=0)

''' Aqui entram os algorimos de machine learning'''
# > criação do classificador <

classificador.fit(previsores_treinamento, classe_treinamento)
previsoes = classificador.predict(previsores_teste)

from sklearn.metrics import confusion_matrix, accuracy_score
precisao = accuracy_score(classe_teste, previsoes)
matriz = confusion_matrix(classe_teste, previsoes)
