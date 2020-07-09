# Analisis de sentimientos utilizando LDA

El LDA o Latent Dirichlet Allocation es un sistema de analisis no supervisado que presumpone que los textos estan compuestos por topicos que le dan relevancia.
Para este ejercicio, se entrena sobre extracciones hechas en tripadvisor, sobre calificaciones a hoteles de la antigua guatemala.

La metodologia seguida, es a dichos textos, limpiarlos, separarlos por palabras (tokenizar) y estandarizar (lematizacion) para entrenar el sistema LDA,
dicho modelo cuenta con 20 topicos, de los cuales hay palabras claves que van desvelando las palabras mas representativas del topico. Es decir, al ingresar
un texto, el modelo regresara el topico mas relevante con sus palabras más representativas.

Para ello de las estructuras resultantes de LDA, se van a extraer el conjunto de topicos probables por palabra, se ordenan los topicos por relevancia, y se 
extrae el topico moda (que más se repite). Y se contrasta con los topicos estadar generados por el entrenamient LDA, para ver sus palabras mas representativas.

# Repo
https://github.com/colombian/pythonLDAmodeltripadvisor

# Para verificar componentes

$ pip install requirements.txt

*Run it inside a python terminal*

# how to train 
$ from src.models.train import *
$ lda_model=train(read_sample())


# how to test

$ __from src.models.predict import *__

$ **model = load_model()**

$ **test = predict(model, 'Best SPA, attention 10/10. Amazing food and experience!! 100% recommended. Massages are great, rooms are clean and location is great. Definitely going to come back! If you want to have the whole Antigua experience don’t hesitate to choose this hotel.')**