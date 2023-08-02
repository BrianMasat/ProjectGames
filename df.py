import pandas as pd
import ast
from collections import Counter
from typing import  Dict

rows = []

with open('steam_games.json') as f:
    for line in f.readlines():
        rows.append(ast.literal_eval(line))


df = pd.DataFrame(rows)
df.head()

print(df)



# Reemplazar los valores no válidos por NaN
df["release_date"] = pd.to_datetime(df["release_date"], errors='coerce')

# Filtrar el DataFrame para obtener los registros válidos
df_filtered = df.dropna(subset=["release_date"])

# Convertir la columna "release_date" a tipo datetime
df_filtered["release_date"] = pd.to_datetime(df_filtered["release_date"])





df['sentiment'] = df['sentiment'].astype(str)
df['sentiment'] = df['sentiment'].str.replace(r'\d+ user review[s]?', 'nan', regex=True)





# def genero( Año: str ): Se ingresa un año y devuelve un diccionario con los 5 géneros más publicados en el orden correspondiente.
def obtener_generos(year: str) -> Dict[str, int]:
    # Convertir el año en un objeto de tipo Period con frecuencia anual ('Y')
    year_period = pd.to_datetime(year, format='%Y').to_period('Y')

    # Filtrar el DataFrame para obtener los registros del año especificado
    df_filtered = df[df['release_date'].dt.to_period('Y') == year_period]

    # "Aplanar" la columna "genres" para convertir cada lista de géneros en filas separadas
    df_filtered = df_filtered.explode('genres')

    # Contar el número de registros por género
    ventas = df_filtered['genres'].value_counts()

    # Obtener los 5 géneros más vendidos
    top_5_generos = ventas.head(5)

    return {year: top_5_generos.to_dict()}

# Ejemplo de uso:
# print(obtener_generos('2018'))





# def juegos( Año: str ): Se ingresa un año y devuelve un diccionario con los juegos lanzados en el año.
def obtener_juegos(year: str) -> Dict[str, int]:
    # Convertir el año en un objeto de tipo Period con frecuencia anual ('Y')
    year_period = pd.to_datetime(year, format='%Y').to_period('Y')
    
    # Filtrar el DataFrame para obtener los registros del año especificado
    df_filtered = df[df['release_date'].dt.to_period('Y') == year_period]

    # Obtener la lista de nombres de juegos lanzados en el año
    juegos_lanzados = df_filtered['app_name'].tolist()

    # Crear el diccionario con la lista de nombres de juegos como valores
    # y asignar 1 como valor para cada juego (esto indica que el juego fue lanzado una vez)
    juegos_dict = {juego for juego in juegos_lanzados}

    return {year: juegos_dict}

# Ejemplo de uso:
# print(obtener_juegos('2018'))





# def specs( Año: str ): Se ingresa un año y devuelve un diccionario con los 5 specs que más se repiten en el mismo en el orden correspondiente.
def obtener_specs(year: str) -> Dict[str, int]:
    # Convertir el año en un objeto de tipo Period con frecuencia anual ('Y')
    year_period = pd.to_datetime(year, format='%Y').to_period('Y')
    
    # Filtrar el DataFrame para obtener los registros del año especificado
    df_filtered = df[df['release_date'].dt.to_period('Y') == year_period]

    # "Aplanar" la columna "specs" para convertir cada lista de specs en filas separadas
    df_filtered = df_filtered.explode('specs')

    # Contar la frecuencia de cada spec en el DataFrame
    specs_counter = Counter(df_filtered['specs'])

    # Obtener los 5 specs más comunes
    top_5_specs = dict(specs_counter.most_common(5))

    return {year: top_5_specs}

# Ejemplo de uso:
# print(obtener_specs('2018'))





# def earlyacces( Año: str ): Cantidad de juegos lanzados en un año con early access.
def obtener_early_access(year: str) -> Dict[str, int]:
    # Convertir el año en un objeto de tipo Period con frecuencia anual ('Y')
    year_period = pd.to_datetime(year, format='%Y').to_period('Y')
    
    # Filtrar el DataFrame para obtener los registros del año especificado
    df_filtered = df[df['release_date'].dt.to_period('Y') == year_period]

    # Contar la cantidad de juegos con "early access"
    count_early_access = df_filtered[df_filtered['early_access'] == True].shape[0]

    return {year: count_early_access}

# Ejemplo de uso:
# print(obtener_early_access('2018'))





#def sentiment( Año: str ): Según el año de lanzamiento, se devuelve un diccionario con la cantidad de registros que se encuentren categorizados con un análisis de sentimiento.
    # Ejemplo de retorno: {Mixed = 182, Very Positive = 120, Positive = 278}
def obtener_sentiment(year: str) -> Dict[str, int]:
    # Convertir el año en un objeto de tipo Period con frecuencia anual ('Y')
    year_period = pd.to_datetime(year, format='%Y').to_period('Y')
    
    # Filtrar el DataFrame para obtener los registros del año especificado
    df_filtered = df[df['release_date'].dt.to_period('Y') == year_period]

    # Contar la cantidad de registros para cada valor de sentimiento
    sentiment_counts = df_filtered['sentiment'].value_counts()

    # Eliminar el valor 'nan' del diccionario
    sentiment_counts_dict = sentiment_counts.to_dict()
    if 'nan' in sentiment_counts_dict:
        del sentiment_counts_dict['nan']

    return {year: sentiment_counts_dict}

# Ejemplo de uso:
# print(obtener_sentiment('2014'))





# def metascore( Año: str ): Top 5 juegos según año con mayor metascore.
def obtener_metascore(year: str) -> Dict[str, int]:
    # Convertir el año en un objeto de tipo Period con frecuencia anual ('Y')
    year_period = pd.to_datetime(year, format='%Y').to_period('Y')
    
    # Filtrar el DataFrame para obtener los registros del año especificado
    df_filtered = df[df["release_date"].dt.to_period('Y') == year_period]

    # Eliminar los registros con valores 'NaN' en la columna 'metascore'
    df_filtered = df_filtered.dropna(subset=['metascore'])

    # Ordenar los registros en orden descendente según el valor del metascore
    df_sorted = df_filtered.sort_values(by='metascore', ascending=False)

    # Seleccionar los 5 primeros registros (los que tienen el metascore más alto)
    top_5_games = df_sorted.head(5)

    # Crear un diccionario que contenga el nombre del juego como clave y el valor del metascore como valor
    metascore_dict = {game['app_name']: game['metascore'] for _, game in top_5_games.iterrows()}

    return {year: metascore_dict}

# Ejemplo de uso:
# print(obtener_metascore('2016'))