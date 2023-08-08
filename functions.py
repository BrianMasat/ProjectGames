import pandas as pd
import numpy as np
import ast
import pickle 
from collections import Counter
from typing import  Dict, Union


with open('xgb_model.pkl', 'rb') as file:
    loaded_model = pickle.load(file)


rows = []
with open('steam_games.json') as f:
    for line in f.readlines():
        rows.append(ast.literal_eval(line))
df = pd.DataFrame(rows)


# Reemplazar los valores no válidos por NaN
df["release_date"] = pd.to_datetime(df["release_date"], errors='coerce')
# Filtrar el DataFrame para obtener los registros válidos
df_filtered = df.dropna(subset=["release_date"])
# Convertir la columna "release_date" a tipo datetime
df_filtered["release_date"] = pd.to_datetime(df_filtered["release_date"])


# Convertir la columna "sentiment" a tipo string y reemplazar los valores no válidos por nan
df['sentiment'] = df['sentiment'].astype(str)
df['sentiment'] = df['sentiment'].str.replace(r'\d+ user review[s]?', 'nan', regex=True)


# def genero( Año: str ): Se ingresa un año y devuelve un diccionario con los 5 géneros más publicados en el orden correspondiente.
def obtener_generos(year: str) -> Dict[str, int]:
    year_period = pd.to_datetime(year, format='%Y').to_period('Y')
    df_filtered = df[df['release_date'].dt.to_period('Y') == year_period]
    df_filtered = df_filtered.explode('genres')
    
    if df_filtered.empty:
        return "Valor no encontrado"
    
    ventas = df_filtered['genres'].value_counts()
    top_5_generos = ventas.head(5)
    return {year: top_5_generos.to_dict()}

# Ejemplo de uso:
# print(obtener_generos('2018'))


# def juegos( Año: str ): Se ingresa un año y devuelve un diccionario con los juegos lanzados en el año.
def obtener_juegos(year: str) -> Dict[str, int]:
    year_period = pd.to_datetime(year, format='%Y').to_period('Y')
    df_filtered = df[df['release_date'].dt.to_period('Y') == year_period]

    if df_filtered.empty:
        return "Valor no encontrado"
    
    juegos_lanzados = df_filtered['app_name'].tolist()
    juegos_dict = {juego for juego in juegos_lanzados}
    return {year: juegos_dict}
# Ejemplo de uso:
# print(obtener_juegos('2018'))


# def specs( Año: str ): Se ingresa un año y devuelve un diccionario con los 5 specs que más se repiten en el mismo en el orden correspondiente.
def obtener_specs(year: str) -> Dict[str, int]:
    year_period = pd.to_datetime(year, format='%Y').to_period('Y')
    df_filtered = df[df['release_date'].dt.to_period('Y') == year_period]

    if df_filtered.empty:
        return "Valor no encontrado"
    
    df_filtered = df_filtered.explode('specs')
    specs_counter = Counter(df_filtered['specs'])
    top_5_specs = dict(specs_counter.most_common(5))
    return {year: top_5_specs}
# Ejemplo de uso:
# print(obtener_specs('2018'))


# def earlyacces( Año: str ): Cantidad de juegos lanzados en un año con early access.
def obtener_early_access(year: str) -> Dict[str, int]:
    year_period = pd.to_datetime(year, format='%Y').to_period('Y')
    df_filtered = df[df['release_date'].dt.to_period('Y') == year_period]

    if df_filtered.empty:
        return "Valor no encontrado"
    
    count_early_access = df_filtered[df_filtered['early_access'] == True].shape[0]
    return {year: count_early_access}
# Ejemplo de uso:
# print(obtener_early_access('2018'))


#def sentiment( Año: str ): Según el año de lanzamiento, se devuelve un diccionario con la cantidad de registros que se encuentren categorizados con un análisis de sentimiento.
def obtener_sentiment(year: str) -> Dict[str, int]:
    year_period = pd.to_datetime(year, format='%Y').to_period('Y')
    df_filtered = df[df['release_date'].dt.to_period('Y') == year_period]

    if df_filtered.empty:
        return "Valor no encontrado"
    
    sentiment_counts = df_filtered['sentiment'].value_counts()
    sentiment_counts_dict = sentiment_counts.to_dict()
    if 'nan' in sentiment_counts_dict:
        del sentiment_counts_dict['nan']

    return {year: sentiment_counts_dict}
# Ejemplo de uso:
# print(obtener_sentiment('2014'))


# def metascore( Año: str ): Top 5 juegos según año con mayor metascore.
def obtener_metascore(year: str) -> Dict[str, int]:
    year_period = pd.to_datetime(year, format='%Y').to_period('Y')
    df_filtered = df[df["release_date"].dt.to_period('Y') == year_period]
    df_filtered = df_filtered.dropna(subset=['metascore'])

    if df_filtered.empty:
        return "Valor no encontrado"
    
    df_sorted = df_filtered.sort_values(by='metascore', ascending=False)
    top_5_games = df_sorted.head(5)
    metascore_dict = {game['app_name']: game['metascore'] for _, game in top_5_games.iterrows()}

    return {year: metascore_dict}
# Ejemplo de uso:
# print(obtener_metascore('2016'))


# def predicción( genero, earlyaccess = True/False, (Variables que elijas) ): Ingresando estos parámetros, deberíamos recibir el precio y RMSE.
# Cargar el modelo desde el archivo
def price_predictor(variables: str):
    string_numbers = variables.split(', ')
    integer_list = [int(number) for number in string_numbers]
    
    if len(integer_list) == 23:
        price_pred = loaded_model.predict(np.array(integer_list).reshape(1, -1))[0].round(2)
        RMSE = '4.23'
        return {'Price Prediction': str(price_pred), 'RMSE': RMSE}
    elif len(integer_list) < 23:
        return {'Error': 'Se insertaron variables de menos'}
    elif len(integer_list) > 23:
        return {'Error': 'Se insertaron variables demás'}