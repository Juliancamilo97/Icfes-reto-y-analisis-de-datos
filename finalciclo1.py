import pandas as pd

data= pd.read_csv('titanic3.csv')

def pasajero(data: pd.DataFrame)->dict:
    mask= data['survived']==1
    dataf= data[mask]
    mask2= dataf[dataf.home_dest.notnull()]
    #resultado= dataf[['name','age','sex','ticket','home_dest']]
    resultado2=mask2[['name','age','sex','ticket','home_dest']]
    
    return resultado2.to_dict()

print(pasajero(data))