<span>https://github.com/BrianMasat/ProjectGames/blob/main/imagenes/henrylogo.png</span><span>)</span>
<h1 style="color:red"><center> Machine Learning Operations Engineer(MLOps)</center></h1>
<h2 style="color:red"><center> Proyecto Individual N°1</center></h2>

<span>![</span><span>Imagen</span><span>]</span><span>(</span><span>https://github.com/BrianMasat/ProjectGames/blob/main/imagenes/mlops.png</span><span>)</span>

<h1>Introducción al proyecto:</h1>

En este emocionante proyecto, nos sumergiremos en el fascinante mundo de Machine Learning Operations, abordando un procedimiento completo que incluye tres etapas principales: Ingeniería de Datos, Análisis Exploratorio y Transformación de los Datos, y Modelado con Técnicas de Machine Learning.

En la primera etapa, implementaremos técnicas de Ingeniería de Datos para el desarrollo de una API que permitirá disponibilizar los datos para su posterior consumo y consulta. Crearemos consultas específicas para obtener información relevante, como los géneros más ofrecidos, los juegos lanzados en un año determinado y otras consultas interesantes relacionadas con el análisis de sentimiento y metascore de los juegos.

En la segunda etapa, nos sumergiremos en la fase de Data Preprocessing y Exploration, donde limpiaremos y exploraremos los datos para prepararlos adecuadamente para la predicción. El Análisis Exploratorio de los Datos (EDA) será un paso crucial para entender las relaciones entre las variables y detectar posibles patrones y anomalías.

En la tercera y última etapa, llegaremos al corazón de este proyecto: el Modelo de Predicción. Aquí entrenaremos nuestro algoritmo de machine learning para que pueda realizar predicciones precisas sobre los precios de los juegos en Steam. Tomaremos en cuenta características como género, año, especificaciones y otras variables relevantes para lograr una predicción precisa.

Sin embargo, no solo se trata de la implementación técnica; también es esencial comunicar los resultados de manera efectiva. Por ello, crearemos un video donde mostraremos el funcionamiento de las consultas en nuestra API, demostrando los objetivos logrados por nuestro modelo.

En este desafiante proyecto, aprenderemos a afrontar situaciones reales en el mundo de Machine Learning Operations, desde la preparación y análisis de los datos hasta la implementación de modelos de predicción en una API accesible. ¡Te invito a acompañarme en este emocionante recorrido por el mundo del análisis y predicción de precios de juegos en Steam!


<span>![</span><span>Imagen</span><span>]</span><span>(</span><span>https://github.com/BrianMasat/ProjectGames/blob/main/imagenes/descripci%C3%B3n.png</span><span>)</span>


<h1>Evaluación de cumplimiento de los objetivos:</h1>

 ■ Transformaciones en las bases de datos: [Link al Notebook](https://github.com/BrianMasat/ProjectGames/blob/main/EDA_MLOps.ipynb)<br>
 ■ Fuente de datos: [Link al DataSet](https://github.com/BrianMasat/ProjectGames/blob/main/steam_games.json) <br>
 ■ Deployment: [Link al Render](https://projectgames-dataengineering.onrender.com) <br>
 ■ Video: [Link al Video]() <br>


<h1>Requerimientos:</h1>
En esta sección, establecemos los principales requerimientos y objetivos para el desarrollo del proyecto.

<h3>Transformaciones de Datos:</h3>
Para este MVP, no es necesario realizar transformaciones directas en el dataset, pero se trabajará en leer el dataset con el formato correcto para su posterior procesamiento.

<h3>Desarrollo de la API:</h3>
El objetivo es disponibilizar los datos de la empresa mediante el framework FastAPI. Se implementarán 6 funciones para los endpoints que serán consumidos en la API, cada una con un decorador correspondiente (@app.get('/')). Las consultas propuestas son las siguientes:

<h4>■  def genero(year: str):</h4> Se ingresa un año y devuelve una lista con los 5 géneros más ofrecidos en el orden correspondiente.

<h4>■ def juegos(year: str):</h4> Se ingresa un año y devuelve una lista con los juegos lanzados en ese año.

<h4>■ def specs(year: str):</h4> Se ingresa un año y devuelve una lista con los 5 specs que más se repiten en el mismo en el orden correspondiente.

<h4>■ def earlyacces(year: str):</h4> Devuelve la cantidad de juegos lanzados en un año con early access.

<h4>■ def sentiment(year: str):</h4> Según el año de lanzamiento, devuelve una lista con la cantidad de registros que se encuentren categorizados con un análisis de sentimiento.

<h4>■ def metascore(year: str):</h4> Devuelve el Top 5 de juegos según el año con el mayor metascore.

<h3>Análisis Exploratorio de los Datos (EDA):</h3>
Realizaremos un Análisis Exploratorio de los Datos (EDA) para comprender las relaciones entre las variables y detectar posibles patrones y anomalías.

<h3>Modelo de Predicción:</h3>
Desarrollaremos un modelo de predicción que tome en cuenta características como género, early access, y otras variables relevantes para predecir con precisión los precios de los juegos en Steam. La función predicción
<h4>■ def predicción(genero, earlyaccess=True/False, (Variables que elijas))</h4> permitirá ingresar estos parámetros y obtener el precio y el RMSE (Root Mean Squared Error) como resultado.

<h3>Video de Presentación:</h3>
Crearemos un video donde mostraremos el funcionamiento de las consultas en nuestra API, así como una explicación del modelo utilizado para las predicciones. El video, de máximo 7 minutos de duración, será una oportunidad para comunicar de manera efectiva los resultados alcanzados en el proyecto y presentar los logros obtenidos en cada una de las etapas mencionadas. <br> <br>

<h1>Criterios de evaluación:</h1>

<span>![</span><span>Imagen</span><span>]</span><span>(</span><span>https://github.com/BrianMasat/ProjectGames/blob/main/imagenes/MVP_MLops.png</span><span>)</span>

 <h1>Deployment:</h1> 
 Para realizar el deploy de esta aplicación, se utilizó la plataforma Render. Render es una plataforma en la nube que facilita el despliegue y el hosting de aplicaciones web y API de forma sencilla y escalable.


<h1>Contribuciones:</h1>

Este proyecto es de código abierto y está abierto a contribuciones y sugerencias. Si desea contribuir, siga las siguientes instrucciones:

■ Haga un fork del repositorio: Haga una copia del repositorio en su propia cuenta de GitHub.

■ Cree una nueva rama: Cree una nueva rama en su fork para trabajar en su característica o corrección específica.

■ Realice sus cambios: Realice los cambios necesarios en la nueva rama, asegurándose de seguir las mejores prácticas de codificación y documentación.

■ Realice un pull request: Una vez que haya completado sus cambios, envíe un pull request a la rama principal del repositorio original. Espere la revisión y aprobación del equipo.

<h1>Licencia:</h1>
Este proyecto está licenciado bajo la licencia Apache License Version 2.0 [Link to License](http://www.apache.org/licenses/)