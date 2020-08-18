from sklearn.base import BaseEstimator, TransformerMixin

# All sklearn Transforms must have the `transform` and `fit` methods
class DropColumns(BaseEstimator, TransformerMixin):
    def __init__(self, columns):
        self.columns = columns

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        # Primeiro realizamos a cópia do dataframe 'X' de entrada
        data = X.copy()
        # Retornamos um novo dataframe sem as colunas indesejadas
        return data.drop(labels=self.columns, axis='columns')

#fill ingles
def FillIngles(dataframe):
    print("Preenchendo Ingles")
    ingles_freq = dataframe['INGLES'].value_counts().index[0]
    return dataframe.INGLES.fillna(ingles_freq)

#remove quem não tem atividade nem hora de aula nem nota
def RemoveDesistente(dataframe): 
    print("Removendo desistente")
    dataframe.drop(dataframe[(dataframe['NOTA_DE'] == 0) & (dataframe['NOTA_EM'] == 0) & (dataframe['NOTA_MF'] == 0) & (dataframe['NOTA_GO'] == 0) & (dataframe['H_AULA_PRES'] == 0) & (dataframe['TAREFAS_ONLINE'] == 0)].index, inplace=True)
    return dataframe

#fill nota go
def FillGO(dataframe):
    print("Preenchendo GO")
    dataframe.NOTA_GO.fillna((dataframe['NOTA_DE'] + dataframe['NOTA_EM'] + dataframe['NOTA_MF'])/3)
    return dataframe

#add coluna media geral
def AddMedia(dataframe):
    print("Adicionando Media")
    dataframe['MEDIA_GERAL'] = (dataframe['NOTA_DE'] + dataframe['NOTA_EM'] + dataframe['NOTA_MF'] + dataframe['NOTA_GO'])/4
    return dataframe

#add coluna media_humanas
def AddMediaHumanas(dataframe):
    print("Adicionando Media Humanas")
    dataframe['MEDIA_HUMANAS'] = (dataframe['NOTA_DE'] + dataframe['NOTA_EM'])/2 

#add coluna media_exatas
def AddMediaExatas(dataframe):
    print("Adicionando Media Exatas")
    dataframe['MEDIA_EXATAS'] = (dataframe['NOTA_MF'] + dataframe['NOTA_GO'])/2
    return dataframe
