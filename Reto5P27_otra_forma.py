import pandas as pd

def aplicaciones(url,codDep,codRes):
    """
    Con try probamos si la url está bien y crea el DataFrame con los datos del archivo csv, 
    si es así ejecuta todo el código en el que se crean las listas como lo pide el enunciado
    
    En caso de que la url esté mál o el archivo csv no exista entonces se va a la línea except
    y muestra el mensaje de error: 'Error con la url del archivo de datos
    """
    try:
        # Abrir el archivo .csv, el cual está delimitado por ';'
        data = pd.read_csv(url,delimiter=';') 

        # Filtrar los datos para mostrar solo aquellos que corresponden al codDep indicado como parámetro en la función
        dataf = data[data['CodDep']==codDep]

        # Construir la salida de la función de acuerdo con el codRes (1,2 o 3) indicado como parámetro en la función 
        if codRes == 1:
            # Calcular la suma de las columnas Rendimiento, ExpUs y Latencia
            data1 = dataf[['Rendimiento','ExpUs','Latencia']].sum() # Crea una serie, cuyos índices son: 'Rendimiento','ExpUs','Latencia' y los valores de la columna son las sumas

            # Extraer los valores para cada índice
            latencia = data1['Latencia']
            rendimiento = data1['Rendimiento'] 
            experiencia = data1['ExpUs']

            # Crear la lista con el tiempo total (la suma) de la latencia, el rendimiento y la expereriencia
            resultados =  [latencia, rendimiento, experiencia]

        elif codRes == 2:
            # Calcula el promedio de las columnas Rendimiento, ExpUs y Latencia
            data1 = dataf[['Rendimiento','ExpUs','Latencia']].mean() # Crea una serie, cuyos índices son: 'Rendimiento','ExpUs','Latencia' y los valores de la columna son los promedios

            # Extraer los valores para cada índice
            latencia = data1['Latencia']
            rendimiento = data1['Rendimiento'] 
            experiencia = data1['ExpUs']

            # Crear la lista con el tiempo promedio de la latencia, el rendimiento y la expereriencia (redondeados)
            resultados =  [round(latencia,1), round(rendimiento,1), round(experiencia,1)]

        elif codRes == 3:
            # Calcula el máximo de las columnas Rendimiento, ExpUs y Latencia
            data1 = dataf[['Rendimiento','ExpUs','Latencia']].max() # Crea una serie, cuyos índices son: 'Rendimiento','ExpUs','Latencia' y los valores de la columna son los promedios

            # Extraer los valores para cada índice
            latencia = data1['Latencia']
            rendimiento = data1['Rendimiento'] 
            experiencia = data1['ExpUs']

            # Seleccionar en el DataFrame dataf las filas con los valores máximos de latencia, rendimiento y experiencia
            # con ['App'].values[0] se selecciona el valor de 'App' en los nuevos DataFrame creados (codApp_Lat, codApp_Ren, codApp_Exp)
            codApp_Lat = dataf[dataf['Latencia'] == latencia]['App'].values[0]
            codApp_Ren = dataf[dataf['Rendimiento'] == rendimiento]['App'].values[0]
            codApp_Exp = dataf[dataf['ExpUs'] == experiencia]['App'].values[0]

            resultados =  [codApp_Lat, codApp_Ren, codApp_Exp]
    except:
            resultados = 'Error con la url del archivo de datos'
    return resultados


url = 'https://raw.githubusercontent.com/danieljpadilla2011/publico/main/datosP27.csv'

print(aplicaciones(url,"IDI01",1))
print(aplicaciones(url,"IDI04",2))
print(aplicaciones(url,"IDI06",3))
print(aplicaciones('otro.csv',"IDI06",4))