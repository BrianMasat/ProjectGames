from fastapi import FastAPI, Response
from df import obtener_generos, obtener_juegos, obtener_specs, obtener_early_access, obtener_sentiment, obtener_metascore

app = FastAPI(title="Steam Games API",
              description="Proyecto individual 1",
              version="1.0.0")




@app.get('/')
async def root():
    return Response(content='<h2 style="text-align: center">Respuesta de Steam Games API exitosa</h2>', media_type='text/html')




# Request 1
@app.get('/generos/{year}')
async def generos(year: str):
    result = obtener_generos(year)
    return result




# Request 2
@app.get('/juegos/{year}')
async def juegos(year: str):
    result = obtener_juegos(year)
    return result




# Request 3
@app.get('/specs/{year}')
async def specs(year: str):
    result = obtener_specs(year)
    return result




# Request 4
@app.get('/early_access/{year}')
async def early_access(year: str):
    result = obtener_early_access(year)
    return result




# Request 5
@app.get('/sentiment/{year}')
async def sentiment(year: str):
    result = obtener_sentiment(year)
    return result




# Request 6
@app.get('/metascore/{year}')
async def metascore(year: str):
    result = obtener_metascore(year)
    return result




# Start the FastAPI server
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)






