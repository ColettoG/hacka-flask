import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error

def main():

    # Se ainda não carregou os dados
    # df = pd.read_csv('/content/drive/MyDrive/Hackathons/starkbank/ndvi_yield_dataset.csv')
    df = pd.read_csv(filepath_or_buffer='./ndvi_yield_dataset.csv')


    # Definindo as variáveis independentes (features) e dependentes (target)
    X = df[['NDVI_Mean', 'NDVI_Max', 'Precipitation_mm', 'Temperature_C']]
    y = df['Yield_ton_per_ha']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Inicializar o modelo Random Forest
    model = RandomForestRegressor(n_estimators=100, random_state=42)

    # Treinar o modelo
    model.fit(X_train, y_train)

    # Fazer previsões no conjunto de teste
    y_pred = model.predict(X_test)

    # cortar primeira resposta
    y_pred = y_pred[1:][0]  
    return y_pred

if __name__ == '__main__':
    main()