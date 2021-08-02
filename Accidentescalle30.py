import pandas as pd
import operator

def accidente(data: pd.DataFrame)->dict:
    data= pd.read_csv(data)
    mask= data['SITIO_EXACTO_ACCIDENTE'].str.contains('CALLE_30')
    df_baq_c30= data[mask]
    df_baq_c30_grav_acc= df_baq_c30[['GRAVEDAD_ACCIDENTE','CANTIDAD_ACCIDENTES']].groupby(by='GRAVEDAD_ACCIDENTE').count().sort_values(by='CANTIDAD_ACCIDENTES', ascending=False)
    df_baq_c30_grav_acc=df_baq_c30_grav_acc.to_dict()
    df_baq_c30_clase_acc= df_baq_c30[['CANTIDAD_ACCIDENTES', 'CLASE_ACCIDENTE']].groupby(by='CLASE_ACCIDENTE').count().sort_values(by='CANTIDAD_ACCIDENTES', ascending=False)
    clase_mas_acc = (max(df_baq_c30_clase_acc.to_dict()['CANTIDAD_ACCIDENTES'].items(), key=operator.itemgetter(1))[0],df_baq_c30_clase_acc.to_dict()['CANTIDAD_ACCIDENTES'][max(df_baq_c30_clase_acc.to_dict()['CANTIDAD_ACCIDENTES'].items(), key=operator.itemgetter(1))[0]])
    df_baq_c30_cant_heridos= df_baq_c30[['CANT_HERIDOS_EN_SITIO_ACCIDENTE', 'SITIO_EXACTO_ACCIDENTE', 'FECHA_ACCIDENTE']].groupby('CANT_HERIDOS_EN_SITIO_ACCIDENTE').max().sort_values(by='CANT_HERIDOS_EN_SITIO_ACCIDENTE', ascending=False, na_position='last')
    cantidad_max_heridos= max(df_baq_c30_cant_heridos.index)
    return {'clase_mas_accidente': clase_mas_acc, 'accidentes_gravedad': df_baq_c30_grav_acc, 'cantidad_max_heridos':(cantidad_max_heridos, df_baq_c30_cant_heridos.loc[max(df_baq_c30_cant_heridos.index)]['FECHA_ACCIDENTE'].split()[0])}
    
print(accidente(pd.read_csv('accidentes.csv')))