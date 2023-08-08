from fastapi import FastAPI, Response
from functions import obtener_generos, obtener_juegos, obtener_specs, obtener_early_access, obtener_sentiment, obtener_metascore, price_predictor

app = FastAPI(title='Steam Games API',
              description='Proyecto individual 1',
              version='1.0.0')


# Test request
@app.get('/')
async def root():
    return Response(content='<h2 style="text-align: center">Respuesta de Steam Games API exitosa</h2>', media_type='text/html')


# Request 1
@app.get('/generos/{year}')
async def generos(year: str):
    try:
        result = obtener_generos(year)
        return result
    except Exception as e:
        return {'error': str(e)}
    

# Request 2
@app.get('/juegos/{year}')
async def juegos(year: str):
    try:
        result = obtener_juegos(year)
        return result
    except Exception as e:
        return {'error': str(e)}
    

# Request 3
@app.get('/specs/{year}')
async def specs(year: str):
    try:
        result = obtener_specs(year)
        return result
    except Exception as e:
        return {'error': str(e)}


# Request 4
@app.get('/early_access/{year}')
async def early_access(year: str):
    try:
        result = obtener_early_access(year)
        return result
    except Exception as e:
        return {'error': str(e)}


# Request 5
@app.get('/sentiment/{year}')
async def sentiment(year: str):
    try:
        result = obtener_sentiment(year)
        return result
    except Exception as e:
        return {'error': str(e)}


# Request 6
@app.get('/metascore/{year}')
async def metascore(year: str):
    try:
        result = obtener_metascore(year)
        return result
    except Exception as e:
        return {'error': str(e)}


# Request 7
@app.get('/prediction/{variables}')
async def predictor(variables: str):
    try:
        result = price_predictor(variables)
        return result
    except Exception as e:
        return {'error': str(e)}
