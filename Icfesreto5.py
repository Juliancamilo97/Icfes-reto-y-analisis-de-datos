import pandas as pd

def iniciar_aplicacion(data: pd.DataFrame, estrato: int)->dict:
    
    doc = pd.read_csv(data)

    distribucion = distribucion_genero_estrato(doc, estrato)
    mejores = diez_mejores(doc)

    diccionarios = {**distribucion, **mejores}

    return diccionarios

def distribucion_genero_estrato(archivo: str, estrato: int):

    mask = archivo.ESTRATO == f"Estrato {str(estrato)}"

    sexo_estrato = archivo[mask]

    #Agrupar según género
    df = sexo_estrato[["GENERO", "ESTRATO"]].groupby("GENERO").count()

 
    return df.to_dict()

def diez_mejores(archivo: str):

    #Agrupar según departamento
    diez_mejores = round(archivo[["DEPARTAMENTO", "PUNT_GLOBAL"]].groupby("DEPARTAMENTO").mean().sort_values(by = "PUNT_GLOBAL", ascending = True).tail(10),2)

    return diez_mejores.to_dict()

print(iniciar_aplicacion("https://raw.githubusercontent.com/FiboDev/Datos/main/icfes.csv", 4))

print(iniciar_aplicacion("https://raw.githubusercontent.com/FiboDev/Datos/main/icfes.csv", 5))

