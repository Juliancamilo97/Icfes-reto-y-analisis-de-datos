import pandas as pd


def creacion_data():
    archivo ='accidentes.csv'
    data = pd.read_csv(archivo)
    #print(datos_validos30.iloc[0:100])
    return data


def accidente(data: pd.DataFrame):
    resultados = dict()
    filtro_carrera30 = data [data['SITIO_EXACTO_ACCIDENTE'].str.contains("CALLE_30_", case= False)]
    datos_validos30 =filtro_carrera30.fillna({'CANT_HERIDOS_EN_SITIO_ACCIDENTE':0, 
    'CANT_MUERTOS_EN _SITIO_ACCIDENTE':0, 'CANTIDAD_ACCIDENTES':0})
    #filtro_clase_accidente30 = datos_validos30.groupby('CLASE_ACCIDENTE').count()
    filtro_clase_accidente30 = datos_validos30.groupby('CLASE_ACCIDENTE').agg(
        {'SITIO_EXACTO_ACCIDENTE':'count'})
    
    
    filtro_max_clase_accidente30 = filtro_clase_accidente30.loc[filtro_clase_accidente30.idxmax()]
    
    max_tupla_clase = (filtro_clase_accidente30.idxmax().iloc[0],
    filtro_clase_accidente30.max().iloc[0])

    resultados ['clase_mas_accidente'] = max_tupla_clase
    filtro_clase30_diccionario = filtro_clase_accidente30.to_dict()
    
    valor_max_heridos = max (datos_validos30.CANT_HERIDOS_EN_SITIO_ACCIDENTE)
    filtro = datos_validos30[datos_validos30.CANT_HERIDOS_EN_SITIO_ACCIDENTE==valor_max_heridos]
    resultados['accidentes_gravedad'] = filtro_clase30_diccionario['SITIO_EXACTO_ACCIDENTE']
    resultados['cantidad_max_heridos'] =(filtro.iloc[0]['CANT_HERIDOS_EN_SITIO_ACCIDENTE'],
    filtro.iloc[0]['FECHA_ACCIDENTE'] )

    print( resultados )


    


data = creacion_data()
accidente(data)