import pandas as pd
import matplotlib.pyplot as plt

def distribucion_genero_estrato(data: pd.DataFrame, estrato: int):
#archivo=pd.read_csv('ICFES.csv', usecols=['GENERO', 'ESTRATO'])
    #Filtro para obtener el estrato
    mask = data.ESTRATO == f"Estrato {str(estrato)}"

    sexo_estrato = data[mask]

    #Agrupar según género
    df = sexo_estrato[["GENERO", "ESTRATO"]].groupby("GENERO").count()

    df.plot(kind = "pie", subplots = True, ylabel = "Estudiantes", title = f"Diagrama de torta para el estrato {str(estrato)}", autopct = '%1.1f%%')

    #plt.show()
 
    return df.to_dict()

def diez_mejores(data: pd.DataFrame):

    #Agrupar según departamento
    diez_mejores = round(data[["DEPARTAMENTO", "PUNT_GLOBAL"]].groupby("DEPARTAMENTO").mean().sort_values(by = "PUNT_GLOBAL", ascending = True).tail(10),2)
    diez_mejores.plot(kind = "barh", legend = False, title = "Top 10 Departamentos con mejor promedio")

    #plt.xlabel('Puntaje global promedio')
    #plt.show()
    return diez_mejores.to_dict()

def iniciar_aplicacion(data: pd.DataFrame, estrato: int)->None:

    distribucion = distribucion_genero_estrato(data, estrato)
    mejores = diez_mejores(data)

    diccionarios = {**distribucion, **mejores}

    return diccionarios



#Casos públicos
print(iniciar_aplicacion(pd.read_csv("ICFES.csv"), 4))
print("--------------------------------")
#Casos ocultos
print(iniciar_aplicacion(pd.read_csv("ICFES.csv"), 5))